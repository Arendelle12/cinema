import tkinter as tk
import psycopg2
from config import config

BG = "#66b3ff"  # Light blue.
ROWS, COLS = 10, 3  # Size of grid.
ROWS_DISP = 8  # Number of rows to display.
COLS_DISP = 3  # Number of columns to display.

class ShowMovies:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Movies")
        self.root.configure(background="Gray") 
        self.number()
        self.show_records()
        self.root.mainloop()
        

    def number(self):
        self.rows = self.read_from_table("""SELECT COUNT(*) FROM movies;""")[0][0]
        self.cols = self.read_from_table("""SELECT COUNT(*) FROM information_schema.columns WHERE table_name='movies';""")[0][0]
        self.data = self.read_from_table("""SELECT * FROM movies ORDER BY title, year_of_production;""")
        #print(self.data)

    def read_from_table(self, sql):
        #sql = """SELECT * FROM movies ORDER BY title, year_of_production;"""
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

    def show_screenings(self):
        print("screen")

    def show_orders(self):
        print("order")

    def show_records(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, bg=BG, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        label1a = tk.Label(top_frame, text="Title", bg=BG, fg="white", width=20)
        label1a.grid(row=0, column=0, padx=3, pady=5)

        label1b = tk.Label(top_frame, text="Year of production", bg=BG, fg="white", width=20)
        label1b.grid(row=0, column=1, padx=3, pady=5)

        label1c = tk.Label(top_frame, text="Length", bg=BG, fg="white", width=20)
        label1c.grid(row=0, column=2, padx=3, pady=5)

        # Create a frame for the canvas and scrollbar(s).
        middle_frame = tk.Frame(master_frame)
        middle_frame.grid(row=1, column=0)

        # Add a canvas in that frame.
        canvas = tk.Canvas(middle_frame)
        canvas.grid(row=0, column=0)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(middle_frame, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

        labels_frame = tk.Frame(canvas, bd=2)
        labels_frame.grid(row=0, column=0)

        for i in range(self.rows):
            for j in range(self.cols):
                label = tk.Label(master=labels_frame, text=self.data[i][j], width=20)
                label.grid(row=i, column=j, padx=5, pady=5)
                

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=labels_frame, anchor=tk.NW)

        labels_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/self.cols) * COLS_DISP), int((h/self.rows) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)

        bottom_frame = tk.Frame(master_frame)
        bottom_frame.grid(row=2, column=0)

        screenings_button = tk.Button(bottom_frame, text="Show screenings", bg="#4dff4d", activebackground="#00ff00", command=self.show_screenings)
        screenings_button.grid(row=0, column=0, padx=20)

        orders_button = tk.Button(bottom_frame, text="Show my orders", bg="#ffff4d", activebackground="Yellow", command=self.show_orders)
        orders_button.grid(row=0, column=1, padx=20)



if __name__ == "__main__":
    app = ShowMovies()
    