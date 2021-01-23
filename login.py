import tkinter as tk
import psycopg2
from config import config
import re
from queries import insert_data, update_data, select_one
import movies

class InputWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Welcome')
        self.name_pattern = re.compile("^[A-Z][a-z]+$")
        self.email_pattern = re.compile("^[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        self.phone_pattern = re.compile("[0-9]{9}")
        self.validationError = tk.StringVar()
        self.window()
        self.root.mainloop()

    def add_user(self):
        self.validationError.set('')
        first_name = self.entry1.get()
        last_name = self.entry2.get()
        email = self.entry3.get()
        phone_number = self.entry4.get()

        if len(email) == 0:
            email = None
        if len(phone_number) == 0:
            phone_number = None

        if not bool(self.name_pattern.match(first_name)):
            self.validationError.set('First name must start with capital letter followed by lowercase letters')
        elif not bool(self.name_pattern.match(last_name)):
            self.validationError.set('Last name must start with capital letter followed by lowercase letters')
        elif email is not None and not bool(self.email_pattern.match(email)):
            self.validationError.set("E-mail doesn't match pattern")
        elif phone_number is not None and not bool(self.phone_pattern.match(phone_number)):
            self.validationError.set("Phone number must contain 9 digits")
        else:
            sql = """INSERT INTO customers
                    VALUES(nextval('customer_id_seq'),%s,%s,%s,%s);"""
            values = (first_name, last_name, email, phone_number)
            insert_data(sql, values)

    def log_in(self):
        self.validationError.set('')
        first_name = self.entry1.get()
        last_name = self.entry2.get()
        sql_find = """SELECT customer_id FROM customers WHERE first_name = %s AND last_name = %s;"""
        customer_data = select_one(sql_find, (first_name, last_name))
        
        
        if customer_data is None:
            self.validationError.set('User does not exist')
        else:
            self.root.destroy()
            movies.ShowMovies(customer_data[0])
        # print(type(customer_data[0]))
        

    def update_user(self):
        self.validationError.set('')

        first_name = self.entry1.get()
        last_name = self.entry2.get()

        query = """SELECT customer_id
                FROM customers
                WHERE first_name = %s AND last_name = %s;"""
        
        customer_data = select_one(query, (first_name, last_name))

        if customer_data is None:
            self.validationError.set('User does not exist')
        else:
            email = self.entry3.get()
            phone_number = self.entry4.get()

            if len(email) == 0:
                email = None
            if len(phone_number) == 0:
                phone_number = None

            if email is not None and not bool(self.email_pattern.match(email)):
                self.validationError.set("E-mail doesn't match pattern")
            elif phone_number is not None and not bool(self.phone_pattern.match(phone_number)):
                self.validationError.set("Phone number must contain 9 digits")
            else:
                sql = """UPDATE customers
                SET email = %s, phone_number = %s
                WHERE first_name = %s AND last_name = %s;"""
                values = (email, phone_number, first_name, last_name)
                update_data(sql, values)
                self.validationError.set("User updated")

    def window(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        middle_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        middle_frame.grid(row=1, column=0)

        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=2, column=0, pady=10)

        error_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        error_frame.grid(row=3, column=0, pady=10)

        add_info = tk.Label(top_frame, text = "To add user: write personal data and click ADD USER button", fg="#29a329")
        add_info.grid(row=0, column=0, padx=10, pady = 10)

        update_info = tk.Label(top_frame, text = "To update email or phone: write users first name and last name and click UPDATE USER button", fg="#ff9900")
        update_info.grid(row=1, column=0, padx=10, pady = 10)

        login_info = tk.Label(top_frame, text = "To log in: write users first name and last name and click LOG IN button", fg="#3399ff")
        login_info.grid(row=2, column=0, padx=10, pady = 10)

        label1 = tk.Label(middle_frame, text = 'FIRST NAME *', fg="red")
        label1.grid(row=0, column=0, pady=5)
        
        self.entry1 = tk.Entry(middle_frame)
        self.entry1.grid(row=1, column=0, pady=5)

        label2 = tk.Label(middle_frame, text = 'LAST NAME *', fg="red")
        label2.grid(row=2, column=0, pady=5)

        self.entry2 = tk.Entry(middle_frame)
        self.entry2.grid(row=3, column=0, pady=5)

        label3 = tk.Label(middle_frame, text = 'EMAIL')
        label3.grid(row=4, column=0, pady=5)

        self.entry3 = tk.Entry(middle_frame)
        self.entry3.grid(row=5, column=0, pady=5)

        label4 = tk.Label(middle_frame, text = 'PHONE NUMBER')
        label4.grid(row=6, column=0, pady=5)

        self.entry4 = tk.Entry(middle_frame)
        self.entry4.grid(row=7, column=0, pady=5)

        
        # napis na przycisku - fg=
        # tlo bez myszki - bg=
        # tlo z myszka - activebackground=
        add_button = tk.Button(bottom_frame, text="Add user", command = self.add_user, bg = '#47d147', activebackground='#29a329')
        add_button.grid(row=0, column=0, padx=20, pady=10)

        login_button = tk.Button(bottom_frame, text="Log In", command = self.log_in, bg = '#80bfff', activebackground='#3399ff')
        login_button.grid(row=0, column=1, padx=20, pady=10)

        update_button = tk.Button(bottom_frame, text="Update user", command = self.update_user, bg = '#ffd11a', activebackground='#e6b800')
        update_button.grid(row=0, column=2, padx=20, pady=10)

        label5 = tk.Label(error_frame, textvariable = self.validationError)
        label5.grid(row=0, column=0)

        

if __name__ == "__main__":
    win = InputWindow()
