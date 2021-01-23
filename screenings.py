import  tkinter as tk
from tkinter import ttk
import psycopg2
from config import config
from queries import select_all
import add_order

class ShowScreenings:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.root = tk.Tk() 
        self.root.geometry('600x300')
        self.root.title("Screenings") 
        self.screening_id = 0
        self.show()
        self.root.mainloop()

    def callbackFunc(self, event):
        self.read_id = []
        self.read_titles = []
        self.read_dates = []
        self.read_times = []
        self.radiobutton_vars = []

        movie = self.comboExample.get()

        title = (movie, )
        sql = """SELECT screening_id, title, screening_date, screening_time FROM screenings WHERE title = (%s) ORDER BY screening_date, screening_time;"""
        records = select_all(sql, title)

        for r in records:
            self.read_id.append(r[0])
            self.read_titles.append(r[1])
            self.read_dates.append(r[2])
            self.read_times.append(r[3])

            
         
        rows = select_all("""SELECT COUNT(*) FROM screenings WHERE title = (%s);""", title)[0][0]
        cols = 3

        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        
        self.var = tk.IntVar()
        self.var.set(0)

        for i in range(rows):
            radiobutton = tk.Radiobutton(master=self.middle_frame, variable=self.var, value=i)
            radiobutton.grid(row=i, column=0)

        for j in range(cols):
            for i in range(rows):
                if(j == 0):
                    label = tk.Label(master=self.middle_frame, text=self.read_titles[i], width=20)
                if(j == 1):
                    label = tk.Label(master=self.middle_frame, text=self.read_dates[i], width=20)
                if(j == 2):
                    scr_time = "{:d}:{:02d}".format(self.read_times[i].hour, self.read_times[i].minute)
                    label = tk.Label(master=self.middle_frame, text=scr_time, width=20)

                label.grid(row=i, column=j+1, padx=5, pady=5, sticky="N")

    def getValue(self):
        idx = self.var.get()
        # print(idx, ": ", self.read_id[idx])
        self.root.destroy()
        add_order.AddOrder(self.customer_id, self.read_id[idx])


    def show(self):
        self.master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        self.master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(self.master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        self.middle_frame = tk.Frame(self.master_frame, relief=tk.RIDGE)
        self.middle_frame.grid(row=1, column=0, sticky="N")

        bottom_frame = tk.Frame(self.master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=2, column=0)
        
        data = select_all("""SELECT title FROM screenings GROUP BY title ORDER BY title;""")
        titles=[]
        for i in data:
            titles.append(i[0])
        labelTop = tk.Label(top_frame, text = "Choose movie", fg="green")
        labelTop.grid(row=0, column=0)

        self.comboExample = ttk.Combobox(top_frame, values=titles)
        self.comboExample.grid(row=1, column=0, padx=200)
        self.comboExample.current()

        self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

        okButton = tk.Button(bottom_frame, text="OK", command=self.getValue, bg="#4dff4d", activebackground="#00ff00")
        okButton.grid(row=0, column=0)

# if __name__ == '__main__':
#     root = ShowScreenings(6)