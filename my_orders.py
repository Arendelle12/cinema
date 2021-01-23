import tkinter as tk
from queries import select_all
import movies
import login 

BG = "#66ccff"
FG = "#00334d"

class ShowOrders:
    def __init__(self, customer_id):
        self.root = tk.Tk()
        self.root.title('My orders')
        self.customer_id = customer_id
        self.show()
        self.root.mainloop()
        
    def movies(self):
        self.root.destroy()
        movies.ShowMovies(self.customer_id)

    def tickets(self):
        #pobranie id zamowienia
        pass

    def delete(self):
        pass

    def log_out(self):
        self.root.destroy()
        login.InputWindow()

    def show(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        checkLabel = tk.Label(top_frame, text="Check", width=11, bg=BG, fg=FG)
        checkLabel.grid(row=0, column=0)
        titleLabel = tk.Label(top_frame, text="Title", width=20, bg=BG, fg=FG)
        titleLabel.grid(row=0, column=1)
        typeLabel = tk.Label(top_frame, text="Type of ticket", width=20, bg=BG, fg=FG)
        typeLabel.grid(row=0, column=2)
        numberLabel = tk.Label(top_frame, text="Number of tickets", width=20, bg=BG, fg=FG)
        numberLabel.grid(row=0, column=3)
        priceLabel = tk.Label(top_frame, text="Price", width=20, bg=BG, fg=FG)
        priceLabel.grid(row=0, column=4)
        dateLabel = tk.Label(top_frame, text="Date", width=20, bg=BG, fg=FG)
        dateLabel.grid(row=0, column=5)
        timeLabel = tk.Label(top_frame, text="Time", width=20, bg=BG, fg=FG)
        timeLabel.grid(row=0, column=6)

        customer_id = 4

        values = (customer_id, )
        sql = """SELECT s.title, type_of_ticket, COUNT(type_of_ticket), SUM(price), s.screening_date, s.screening_time 
                FROM tickets AS t INNER JOIN orders AS o ON t.order_id = o.order_id INNER JOIN screenings AS s ON t.screening_id = s.screening_id 
                WHERE customer_id = (%s) 
                GROUP BY t.order_id, s.screening_date, s.screening_time, s.title, type_of_ticket
                ORDER BY s.title, s.screening_date, s.screening_time;"""

        records = select_all(sql, values)

        for index, record in enumerate(records):
            tk.Checkbutton(top_frame).grid(row=index+1, column=0, pady=3)
            col = 1
            for r in record:
                tk.Label(top_frame, text=r).grid(row=index+1, column=col, pady=3)
                col += 1

        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=1, column=0)

        moviesButton = tk.Button(bottom_frame, text="Show movies", bg="#ffff4d", activebackground="#ffa31a", command=self.movies)
        moviesButton.grid(row=0, column=0, padx=50)

        ticketsButton = tk.Button(bottom_frame, text="Show tickets", bg="#ffff4d", activebackground="#ffa31a", command=self.tickets)
        ticketsButton.grid(row=0, column=1, padx=50)

        deleteButton = tk.Button(bottom_frame, text="Delete order", bg="#dd3c3c", activebackground="#ff0000", command=self.delete)
        deleteButton.grid(row=0, column=2, padx=50)

        logoutButton = tk.Button(bottom_frame, text="Log out", bg="#9999ff", activebackground="#d24dff", command=self.log_out)
        logoutButton.grid(row=0, column=3, padx=50)

if __name__ == '__main__':
    app = ShowOrders(4)

