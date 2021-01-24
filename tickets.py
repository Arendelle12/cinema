import tkinter as tk
import my_orders
from queries import select_all, delete_data
import my_orders

BG = "#66ccff"
FG = "#00334d"

class ShowTickets:
    def __init__(self, customer_id, order_id):
        self.customer_id = customer_id
        self.order_id = order_id
        self.tickets_id = []
        
        self.show()
        

    def orders(self):
        self.root.destroy()
        my_orders.ShowOrders(self.customer_id)
        

    def delete(self):
        sql = """DELETE FROM tickets WHERE ticket_id = %s;"""
        delete_id = []
        for v in self.checkbuttons_variables:
            delete_id.append(v.get())
        print(delete_id)

        for ticket_id in delete_id:
            if ticket_id != 0:
                value = (ticket_id, )
                delete_data(sql, value)

        self.root.destroy()
        self.show()


    def show(self):
        self.root = tk.Tk()
        self.root.title('My tickets')

        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        checkLabel = tk.Label(top_frame, text="Check", width=11, bg=BG, fg=FG)
        checkLabel.grid(row=0, column=0)
        tittleLabel = tk.Label(top_frame, text="Tittle", width=20, bg=BG, fg=FG)
        tittleLabel.grid(row=0, column=1)
        typeLabel = tk.Label(top_frame, text="Type of ticket", width=20, bg=BG, fg=FG)
        typeLabel.grid(row=0, column=2)
        priceLabel = tk.Label(top_frame, text="Price", width=20, bg=BG, fg=FG)
        priceLabel.grid(row=0, column=3)
        numberLabel = tk.Label(top_frame, text="Number of seat", width=20, bg=BG, fg=FG)
        numberLabel.grid(row=0, column=4)
        discountLabel = tk.Label(top_frame, text="Percent discount", width=20, bg=BG, fg=FG)
        discountLabel.grid(row=0, column=5)



        values = (self.order_id, )
        sql = """SELECT s.title, type_of_ticket, price, number_of_seat, percent_discount
                FROM tickets AS t INNER JOIN screenings AS s ON t.screening_id = s.screening_id
                WHERE t.order_id = (%s) 
                ORDER BY number_of_seat;"""

        id_sql = """SELECT ticket_id
                FROM tickets 
                WHERE order_id = (%s) 
                ORDER BY number_of_seat;"""

        tick_id = select_all(id_sql, values)
        for indx, tid in enumerate(tick_id):
            self.tickets_id.append(tid[0])
        #print(self.tickets_id)

        self.checkbuttons_variables = []

        records = select_all(sql, values)
        for index, record in enumerate(records):
            var = tk.IntVar()
            tk.Checkbutton(top_frame, variable=var, onvalue=self.tickets_id[index]).grid(row=index+1, column=0, pady=3)
            self.checkbuttons_variables.append(var)
            col = 1
            for r in record:
                tk.Label(top_frame, text=r).grid(row=index+1, column=col, pady=3)
                col += 1

        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=1, column=0)

        ordersButton = tk.Button(bottom_frame, text="Show my orders", bg="#ffff4d", activebackground="#ffa31a", command=self.orders)
        ordersButton.grid(row=0, column=0, padx=50, pady=10)

        deleteButton = tk.Button(bottom_frame, text="Delete ticket", bg="#dd3c3c", activebackground="#ff0000", command=self.delete)
        deleteButton.grid(row=0, column=1, padx=50, pady=10)

        self.root.mainloop()

if __name__ == '__main__':
    app = ShowTickets(4, 4)