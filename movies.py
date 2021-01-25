import tkinter as tk
from queries import select_all
import screenings 
import my_orders

BG = "#66b3ff"  
FG = "white"
ROWS, COLS = 10, 3  
ROWS_DISP = 8  
COLS_DISP = 3  

class ShowMovies:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.root = tk.Tk()
        self.root.title("Movies")
        self.root.configure(background="Gray") 
        self.get_data()
        self.show_records()
        self.root.mainloop()

    def get_data(self):
        self.rows = select_all("""SELECT COUNT(*) FROM movies;""")[0][0]
        self.cols = select_all("""SELECT COUNT(*) FROM information_schema.columns WHERE table_name='movies';""")[0][0]
        self.movies = select_all("""SELECT * FROM movies ORDER BY title, year_of_production;""")

    def show_screenings(self):
        self.root.destroy()
        screenings.ShowScreenings(self.customer_id)

    def show_orders(self):
        self.root.destroy()
        my_orders.ShowOrders(self.customer_id)

    def show_records(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, bg=BG, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        label1a = tk.Label(top_frame, text="Title", bg=BG, fg=FG, width=20)
        label1a.grid(row=0, column=0, padx=3, pady=5)

        label1b = tk.Label(top_frame, text="Year of production", bg=BG, fg=FG, width=20)
        label1b.grid(row=0, column=1, padx=3, pady=5)

        label1c = tk.Label(top_frame, text="Length", bg=BG, fg=FG, width=20)
        label1c.grid(row=0, column=2, padx=3, pady=5)

        middle_frame = tk.Frame(master_frame)
        middle_frame.grid(row=1, column=0)

        canvas = tk.Canvas(middle_frame)
        canvas.grid(row=0, column=0)

        vsbar = tk.Scrollbar(middle_frame, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

        labels_frame = tk.Frame(canvas, bd=2)
        labels_frame.grid(row=0, column=0)

        for i in range(self.rows):
            for j in range(self.cols):
                label = tk.Label(master=labels_frame, text=self.movies[i][j], width=20)
                label.grid(row=i, column=j, padx=5, pady=5)
                
        canvas.create_window((0,0), window=labels_frame, anchor=tk.NW)

        labels_frame.update_idletasks()  
        bbox = canvas.bbox(tk.ALL)  

        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/self.cols) * COLS_DISP), int((h/self.rows) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)

        bottom_frame = tk.Frame(master_frame)
        bottom_frame.grid(row=2, column=0)

        screenings_button = tk.Button(bottom_frame, text="Show screenings", bg="#4dff4d", activebackground="#00ff00", command=self.show_screenings)
        screenings_button.grid(row=0, column=0, padx=20)

        orders_button = tk.Button(bottom_frame, text="Show my orders", bg="#ffff4d", activebackground="Yellow", command=self.show_orders)
        orders_button.grid(row=0, column=1, padx=20)


# if __name__ == "__main__":
#     app = ShowMovies()    