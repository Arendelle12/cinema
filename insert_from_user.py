import tkinter as tk

class InputWindow:
    def __init__(self):
        self.root = tk.Tk()
        
        self.box = tk.Canvas(self.root, width = 400, height = 400)
        self.box.pack()
        self.entry1 = tk.Entry(self.root)
        self.entry2 = tk.Entry(self.root)
        self.entry3 = tk.Entry(self.root)
        self.entry4 = tk.Entry(self.root)
        self.validationError = tk.StringVar()
        self.window()

    def get_input(self):
        first_name = self.entry1.get()
        last_name = self.entry2.get()
        email = self.entry3.get()
        phone_number = self.entry4.get()

        if len(first_name) == 0:
            print("Fn is none")
            self.validationError.set('First name cannot be empty')
        elif len(last_name) == 0:
            self.validationError.set('Last name cannot be empty')

        print(first_name, last_name, email, phone_number)

    def window(self):
        label1 = tk.Label(self.root, text = 'FIRST NAME *', fg="red")
        self.box.create_window(200, 40, window = label1)
        
        self.box.create_window(200, 70, window = self.entry1)

        label2 = tk.Label(self.root, text = 'LAST NAME *', fg="red")
        self.box.create_window(200, 110, window = label2)

        self.box.create_window(200, 140, window = self.entry2)

        label3 = tk.Label(self.root, text = 'EMAIL')
        self.box.create_window(200, 180, window = label3)

        self.box.create_window(200, 210, window = self.entry3)

        label4 = tk.Label(self.root, text = 'PHONE NUMBER')
        self.box.create_window(200, 250, window = label4)

        self.box.create_window(200, 280, window = self.entry4)

        button1 = tk.Button(text="OK", command = self.get_input, bg = 'blue', fg = 'white')
        self.box.create_window(200, 320, window = button1)

        label5 = tk.Label(self.root, textvariable = self.validationError)
        self.box.create_window(200, 360, window = label5)

        self.root.mainloop()

win = InputWindow()