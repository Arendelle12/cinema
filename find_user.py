import tkinter as tk
import psycopg2
from config import config
import login
from queries import select_all

class FindWindow:
    def __init__(self, first_name, last_name):
        self.root = tk.Tk()
        self.root.title('Users')
        self.validationError = tk.StringVar()
        self.first_name = first_name
        self.last_name = last_name
        self.window()
        self.root.mainloop()

    def back(self):
        self.root.destroy()
        login.InputWindow()

    def window(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        error_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        error_frame.grid(row=1, column=0, pady=10)

        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=2, column=0, pady=10)

        label1 = tk.Label(top_frame, text = 'FIRST NAME', fg='#29a329')
        label1.grid(row=0, column=0, padx=10, pady=5)
        
        label2 = tk.Label(top_frame, text = 'LAST NAME', fg='#29a329')
        label2.grid(row=0, column=1, padx=10, pady=5)

        label3 = tk.Label(top_frame, text = 'EMAIL', fg='#29a329')
        label3.grid(row=0, column=2, padx=10, pady=5)

        label4 = tk.Label(top_frame, text = 'PHONE NUMBER', fg='#29a329')
        label4.grid(row=0, column=3, padx=10, pady=5)

        data = None
        if self.first_name is None and self.last_name is None:
            data = select_all("""SELECT first_name, last_name, email, phone_number FROM customers;""")
        elif self.first_name is not None and self.last_name is None:
            f_value = self.first_name + '%'
            data = select_all("""SELECT first_name, last_name, email, phone_number FROM customers WHERE first_name LIKE %s;""", (f_value,))
        elif self.first_name is None and self.last_name is not None:
            l_value = self.last_name + '%'
            data = select_all("""SELECT first_name, last_name, email, phone_number FROM customers WHERE last_name LIKE %s;""", (l_value,))
        else:
            f_value = self.first_name + '%'
            l_value = self.last_name + '%'
            data = select_all("""SELECT first_name, last_name, email, phone_number FROM customers WHERE first_name LIKE %s AND last_name LIKE %s;""", (f_value, l_value))

        if not data:
            self.validationError.set('No matching users')  
        else: 
            for index, record in enumerate(data):
                col = 0
                for r in record:
                    tk.Label(top_frame, text=r).grid(row=index+1, column=col, padx=10)
                    col += 1

        back_button = tk.Button(bottom_frame, text="Go back", command = self.back, bg = '#ffd11a', activebackground='#e6b800')
        back_button.grid(row=0, column=0, padx=20, pady=5)

        label5 = tk.Label(error_frame, textvariable = self.validationError, fg="red")
        label5.grid(row=0, column=0)


# if __name__ == "__main__":
#     win = FindWindow('Kedr')