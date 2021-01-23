import tkinter as tk
import psycopg2
from config import config

BG = "#66ccff"

class ShowRecords:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("490x300+200+200")
        self.root.title('Records')
        self.titleLabel = tk.Label(self.root, text="Title", width=20, bg=BG)
        self.titleLabel.grid(row=0, column=0)
        self.yearLabel = tk.Label(self.root, text="Year", width=20, bg=BG)
        self.yearLabel.grid(row=0, column=1)
        self.lengthLabel = tk.Label(self.root, text="Length", width=20, bg=BG)
        self.lengthLabel.grid(row=0, column=2)
        self.show_records()
        self.root.mainloop()

    def show_records(self):
        data = self.read_from_movies()
        for index, record in enumerate(data):
            tk.Label(self.root, text=record[0]).grid(row=index+1, column=0, pady=3)
            tk.Label(self.root, text=record[1]).grid(row=index+1, column=1, pady=3)
            tk.Label(self.root, text=record[2]).grid(row=index+1, column=2, pady=3)

    def read_from_movies(self):
        sql = """SELECT * FROM movies ORDER BY title, year_of_production;"""
        conn = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql)
            #return value
            self.data = cur.fetchall()
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return self.data

if __name__ == "__main__":
    show = ShowRecords()