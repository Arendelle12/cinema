import tkinter as tk
import psycopg2
from config import config
import re
from queries import insert_data, update_data

class InputWindow:
    def __init__(self):
        self.root = tk.Tk()
        
        self.box = tk.Canvas(self.root, width = 400, height = 400)
        self.box.pack()
        self.root.title('Sign in')
        self.entry1 = tk.Entry(self.root)
        self.entry2 = tk.Entry(self.root)
        self.entry3 = tk.Entry(self.root)
        self.entry4 = tk.Entry(self.root)
        self.validationError = tk.StringVar()
        self.window()

    def add_user(self):
        self.validationError.set('')
        name_pattern = re.compile("^[A-Z][a-z]+$")
        email_pattern = re.compile("^[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        phone_pattern = re.compile("[0-9]{9}")

        first_name = self.entry1.get()
        last_name = self.entry2.get()
        email = self.entry3.get()
        phone_number = self.entry4.get()

        if len(email) == 0:
            email = None
        if len(phone_number) == 0:
            phone_number = None

        if not bool(name_pattern.match(first_name)):
            self.validationError.set('First name must start with capital letter \n followed by lowercase letters')
        elif not bool(name_pattern.match(last_name)):
            self.validationError.set('Last name must start with capital letter \n followed by lowercase letters')
        elif email is not None and not bool(email_pattern.match(email)):
            self.validationError.set("E-mail doesn't match pattern")
        elif phone_number is not None and not bool(phone_pattern.match(phone_number)):
            self.validationError.set("Phone number must contain 9 digits")
        else:
            sql = """INSERT INTO customers
                    VALUES(nextval('customer_id_seq'),%s,%s,%s,%s);"""
            values = (first_name, last_name, email, phone_number)
            insert_data(sql, values)

    def log_in(self):
        print("Logowanie")

    def update_user(self):
        self.validationError.set('')
        name_pattern = re.compile("^[A-Z][a-z]+$")
        email_pattern = re.compile("^[A-Za-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
        phone_pattern = re.compile("[0-9]{9}")

        first_name = self.entry1.get()
        last_name = self.entry2.get()
        email = self.entry3.get()
        phone_number = self.entry4.get()

        if len(email) == 0:
            email = None
        if len(phone_number) == 0:
            phone_number = None

        if not bool(name_pattern.match(first_name)):
            self.validationError.set('First name must start with capital letter \n followed by lowercase letters')
        elif not bool(name_pattern.match(last_name)):
            self.validationError.set('Last name must start with capital letter \n followed by lowercase letters')
        elif email is not None and not bool(email_pattern.match(email)):
            self.validationError.set("E-mail doesn't match pattern")
        elif phone_number is not None and not bool(phone_pattern.match(phone_number)):
            self.validationError.set("Phone number must contain 9 digits")
        else:
            sql = """UPDATE customers
            SET email = %s, phone_number = %s
            WHERE first_name = %s AND last_name = %s;"""
            values = (email, phone_number, first_name, last_name)
            update_data(sql, values)

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

        button1 = tk.Button(text="Add user", command = self.add_user, bg = '#c299ff', activebackground='#b380ff', fg='#3d0099')
        self.box.create_window(100, 320, window = button1)

        button2 = tk.Button(text="Log In", command = self.log_in, bg = '#c299ff', activebackground='#b380ff', fg = '#3d0099')
        self.box.create_window(200, 320, window = button2)

        button3 = tk.Button(text="Update user", command = self.update_user, bg = '#c299ff', activebackground='#b380ff', fg = '#3d0099')
        self.box.create_window(300, 320, window = button3)

        label5 = tk.Label(self.root, textvariable = self.validationError)
        self.box.create_window(200, 360, window = label5)

        self.root.mainloop()

win = InputWindow()