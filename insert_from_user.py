import tkinter as tk
import psycopg2
from config import config
import re

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

    def get_input(self):
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
        # if len(first_name) == 0:
        #     print("Fn is none")
        #     self.validationError.set('First name cannot be empty')
        # elif not bool(name_pattern.match(first_name)):
        #     self.validationError.set('First name must start with capital letter followed by lowercase letters')
        # elif len(last_name) == 0:
        #     self.validationError.set('Last name cannot be empty')
        # elif not bool(name_pattern.match(last_name)):
        #     self.validationError.set('Last name must start with capital letter followed by lowercase letters')
        # else:
        #     if len(email) == 0:
        #         email = None
        #     if len(phone_number) == 0:
        #         phone_number = None
        #     else

            # return first_name, last_name, email, phone_number
            # def insert_customer(first_name, last_name, email, phone_number):
    # """ insert values into tables """

            sql = """INSERT INTO customers
                    VALUES(nextval('customer_id_seq'),%s,%s,%s,%s);"""
            conn = None
            try:
                # read database configuration
                params = config()
                # connect to the PostgreSQL database
                conn = psycopg2.connect(**params)
                # create a new cursor
                cur = conn.cursor()
                # execute the INSERT statement
                cur.execute(sql, (first_name, last_name, email, phone_number))
                # commit the changes to the database
                conn.commit()
                # close communication with the database
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
        

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