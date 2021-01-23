import tkinter as tk
from tkinter import ttk
import psycopg2
from config import config
import my_orders 
from queries import select_one, insert_data

BG = "#0099e6"

class AddOrder:
    def __init__(self, customer_id, screening_id):
        self.root = tk.Tk()
        self.root.title('Add order')
        self.customer_id = customer_id
        self.screening_id = screening_id
        self.addOrderError = tk.StringVar()
        self.add()
        self.root.mainloop()

    def add_user_order(self):
        rN = int(self.regularNumber.get())
        sN = int(self.studentNumber.get())
        fN = int(self.familyNumber.get())
        print(type(fN), ": ", fN)
        if fN != 0 and fN < 4:
            self.addOrderError.set('Family only for groups of 4 or bigger')
        # Sprawdzenie, czy jest w sali tyle miejsc
        # jesli nie, komunikat 
        #self.addOrderError.set('Not enough seats. Please choose different screening!')
        # jesli tak, dodaj najpierw nowe zamowienie
        else: 
            order_sql = """INSERT INTO orders VALUES(nextval('order_id_seq'),%s);"""
            insert_data(order_sql, (self.customer_id, ))
            # potem do zamowienia dodaj bilety
            if rN != 0:

                # ticket_id NUMERIC(3) PRIMARY KEY,
                # type_of_ticket VARCHAR(10) NOT NULL DEFAULT 'regular',
                # price NUMERIC(6, 2) NOT NULL CONSTRAINT chk_price CHECK(price > 0),
                # percent_discount NUMERIC(3) CONSTRAINT chk_percent_discount CHECK(percent_discount BETWEEN 0 AND 100),
                # number_of_seat NUMERIC(2) NOT NULL CONSTRAINT chk_seat CHECK(number_of_seat > 0),
                # order_id NUMERIC(3) NOT NULL,
                # discount_id NUMERIC(3),
                # screening_id NUMERIC(3) NOT NULL,

                regular_sql = """INSERT INTO tickets VALUES(nextval('ticket_id_seq'),%s,%s,%s,%s,%s,%s,%s);"""
                for i in range(rN):
                    insert
            self.addOrderError.set('Tickets added to order')

    def show(self):
        self.root.destroy()
        my_orders.ShowOrders(self.customer_id)

    def add(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)
        middle_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        middle_frame.grid(row=1, column=0)
        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=2, column=0)
        error_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        error_frame.grid(row=3, column=0)

        sql = """SELECT title, screening_date, screening_time FROM screenings WHERE screening_id = (%s);"""
        id_value = (self.screening_id, )
        screening_info = select_one(sql, id_value)


        titleLabel = tk.Label(top_frame, text=screening_info[0], bg=BG, fg="white", width=20)
        titleLabel.grid(row=0, column=0)
        dateLabel = tk.Label(top_frame, text=screening_info[1], bg=BG, fg="white", width=20)
        dateLabel.grid(row=0, column=1)
        scr_time = "{:d}:{:02d}".format(screening_info[2].hour, screening_info[2].minute)
        timeLabel = tk.Label(top_frame, text=scr_time, bg=BG, fg="white", width=20)
        timeLabel.grid(row=0, column=2)

        ticketLabel = tk.Label(middle_frame, text="Tickets", fg='red', width=20)
        ticketLabel.grid(row=0, column=0)
        priceLabel = tk.Label(middle_frame, text="Price", fg='red', width=20)
        priceLabel.grid(row=0, column=1)
        selectLabel = tk.Label(middle_frame, text="Select number", fg='red', width=20)
        selectLabel.grid(row=0, column=2)

        regularLabel = tk.Label(middle_frame, text="Regular", width=20)
        regularLabel.grid(row=1, column=0)
        studentLabel = tk.Label(middle_frame, text="Student", width=20)
        studentLabel.grid(row=2, column=0)
        familyLabel = tk.Label(middle_frame, text="Family", width=20)
        familyLabel.grid(row=3, column=0)

        regularPrice = tk.Label(middle_frame, text="30", width=20)
        regularPrice.grid(row=1, column=1)
        studentPrice = tk.Label(middle_frame, text="15", width=20)
        studentPrice.grid(row=2, column=1)
        familyPrice = tk.Label(middle_frame, text="21", width=20)
        familyPrice.grid(row=3, column=1)

        self.regularNumber = tk.IntVar()
        self.studentNumber = tk.IntVar()
        self.familyNumber = tk.IntVar()
        self.regularNumber = tk.Spinbox(middle_frame, from_=0, to=10, width=3)
        self.regularNumber.grid(row=1, column=2)
        self.studentNumber = tk.Spinbox(middle_frame, from_=0, to=10, width=3)
        self.studentNumber.grid(row=2, column=2)
        self.familyNumber = tk.Spinbox(middle_frame, from_=0, to=10, width=3)
        self.familyNumber.grid(row=3, column=2)

        addButton = tk.Button(bottom_frame, text="Add", bg="#33ff33", activebackground="#00e600", command=self.add_user_order)
        addButton.grid(row=0, column=0, padx=20)

        ordersButton = tk.Button(bottom_frame, text="Show orders", bg="#33ff33", activebackground="#00e600", command=self.show)
        ordersButton.grid(row=0, column=1, padx=20)

        errorLabel = tk.Label(error_frame, textvariable = self.addOrderError, fg="red")
        errorLabel.grid(row=0, column=0)

if __name__ == "__main__":
    app = AddOrder(6, 2)  