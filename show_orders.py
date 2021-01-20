import tkinter as tk
import psycopg2
from config import config

class ShowOrders:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('My orders')

        self.show()
        self.root.mainloop()
        

    def read_from_table(self, sql, values):
        conn = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, values)
            #return value
            data = cur.fetchall()
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return data

    def show(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        checkLabel = tk.Label(top_frame, text="Check", width=11, bg="#66ccff")
        checkLabel.grid(row=0, column=0)
        titleLabel = tk.Label(top_frame, text="Title", width=20, bg="#66ccff")
        titleLabel.grid(row=0, column=1)
        typeLabel = tk.Label(top_frame, text="Type of ticket", width=20, bg="#66ccff")
        typeLabel.grid(row=0, column=2)
        numberLabel = tk.Label(top_frame, text="Number of tickets", width=20, bg="#66ccff")
        numberLabel.grid(row=0, column=3)
        priceLabel = tk.Label(top_frame, text="Price", width=20, bg="#66ccff")
        priceLabel.grid(row=0, column=4)
        dateLabel = tk.Label(top_frame, text="Date", width=20, bg="#66ccff")
        dateLabel.grid(row=0, column=5)
        timeLabel = tk.Label(top_frame, text="Time", width=20, bg="#66ccff")
        timeLabel.grid(row=0, column=6)

        customer_id = 2

        values = (customer_id, )
        sql = """SELECT s.title, type_of_ticket, COUNT(type_of_ticket), SUM(price), s.screening_date, s.screening_time 
                FROM tickets AS t INNER JOIN orders AS o ON t.order_id = o.order_id INNER JOIN screenings AS s ON t.screening_id = s.screening_id 
                WHERE customer_id = (%s) 
                GROUP BY t.order_id, s.screening_date, s.screening_time, s.title, type_of_ticket
                ORDER BY s.title, s.screening_date, s.screening_time;"""

        records = self.read_from_table(sql, values)

        for index, record in enumerate(records):
            tk.Checkbutton(top_frame).grid(row=index+1, column=0, pady=3)
            col = 1
            for r in record:
                tk.Label(top_frame, text=r).grid(row=index+1, column=col, pady=3)
                col += 1

        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=1, column=0)

if __name__ == '__main__':
    app = ShowOrders()