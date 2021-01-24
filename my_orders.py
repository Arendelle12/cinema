import tkinter as tk
from queries import select_all
import movies
import login 
import tickets
from queries import delete_data

BG = "#66ccff"
FG = "#00334d"

class ShowOrders:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.orders_id = []
        self.show()
        
    def movies(self):
        self.root.destroy()
        movies.ShowMovies(self.customer_id)

    def tickets(self):
        order_id = None
        for v in self.checkbuttons_variables:
            if v.get() != 0:
                order_id = v.get()
                break

        if order_id is not None:
            self.root.destroy()
            tickets.ShowTickets(self.customer_id, order_id)

    def delete(self):
        sql = """DELETE FROM orders WHERE order_id = %s;"""
        delete_id = []
        for v in self.checkbuttons_variables:
            delete_id.append(v.get())

        for order_id in delete_id:
            if order_id != 0:
                value = (order_id, )
                delete_data(sql, value)

        self.root.destroy()
        self.show()

    def log_out(self):
        self.root.destroy()
        login.InputWindow()

    def show(self):
        self.root = tk.Tk()
        self.root.title('My orders')

        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        checkLabel = tk.Label(top_frame, text="Check", width=11, bg=BG, fg=FG)
        checkLabel.grid(row=0, column=0)
        titleLabel = tk.Label(top_frame, text="Title", width=20, bg=BG, fg=FG)
        titleLabel.grid(row=0, column=1)
        numberLabel = tk.Label(top_frame, text="Number of tickets", width=20, bg=BG, fg=FG)
        numberLabel.grid(row=0, column=2)
        priceLabel = tk.Label(top_frame, text="Price", width=20, bg=BG, fg=FG)
        priceLabel.grid(row=0, column=3)
        dateLabel = tk.Label(top_frame, text="Date", width=20, bg=BG, fg=FG)
        dateLabel.grid(row=0, column=4)
        timeLabel = tk.Label(top_frame, text="Time", width=20, bg=BG, fg=FG)
        timeLabel.grid(row=0, column=5)

        values = (self.customer_id, )
        sql = """SELECT s.title, COUNT(ticket_id), SUM(price), s.screening_date, s.screening_time 
                FROM tickets AS t INNER JOIN orders AS o ON t.order_id = o.order_id INNER JOIN screenings AS s ON t.screening_id = s.screening_id 
                WHERE customer_id = (%s) 
                GROUP BY t.order_id, s.screening_date, s.screening_time, s.title
                ORDER BY s.title, s.screening_date, s.screening_time;"""

        id_sql = """SELECT t.order_id 
                FROM tickets AS t INNER JOIN orders AS o ON t.order_id = o.order_id INNER JOIN screenings AS s ON t.screening_id = s.screening_id 
                WHERE customer_id = (%s) 
                GROUP BY t.order_id, s.screening_date, s.screening_time, s.title
                ORDER BY s.title, s.screening_date, s.screening_time;"""

        ord_id = select_all(id_sql, values)
        for indx, oid in enumerate(ord_id):
            self.orders_id.append(oid[0])

        self.checkbuttons_variables = []

        records = select_all(sql, values)
        for index, record in enumerate(records):
            var = tk.IntVar()
            tk.Checkbutton(top_frame, variable=var, onvalue=self.orders_id[index]).grid(row=index+1, column=0, pady=3)
            self.checkbuttons_variables.append(var)
            col = 1
            for r in record:
                tk.Label(top_frame, text=r).grid(row=index+1, column=col, pady=3)
                col += 1

        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=1, column=0)

        moviesButton = tk.Button(bottom_frame, text="Show movies", bg="#ffff4d", activebackground="#ffa31a", command=self.movies)
        moviesButton.grid(row=0, column=0, padx=30, pady=15)

        ticketsButton = tk.Button(bottom_frame, text="Show tickets", bg="#33cc33", activebackground="#29a329", command=self.tickets)
        ticketsButton.grid(row=0, column=1, padx=30, pady=15)

        deleteButton = tk.Button(bottom_frame, text="Delete order", bg="#dd3c3c", activebackground="#ff0000", command=self.delete)
        deleteButton.grid(row=0, column=2, padx=30, pady=15)

        logoutButton = tk.Button(bottom_frame, text="Log out", bg="#9999ff", activebackground="#d24dff", command=self.log_out)
        logoutButton.grid(row=0, column=3, padx=30, pady=15)

        self.root.mainloop()

# if __name__ == '__main__':
#     app = ShowOrders(6)

