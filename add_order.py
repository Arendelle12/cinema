import tkinter as tk
from tkinter import ttk
import psycopg2
from config import config
from show_records import ShowRecords

class AddOrder:
    def __init__(self, screening_id):
        self.root = tk.Tk()
        self.root.title('Add order')

        self.screening_id = screening_id

        self.add()
        self.root.mainloop()

    def read_from_table(self, sql, values = None):
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
            data = cur.fetchone()
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

    def getValue(self):
        rN = self.regularNumber.get()
        sN = self.studentNumber.get()
        fN = self.familyNumber.get()
        print(rN, sN, fN)

        self.root.destroy()
        sr_temp = ShowRecords()
        

    def add(self):
        master_frame = tk.Frame(self.root, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)

        top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)
        middle_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        middle_frame.grid(row=1, column=0)
        bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
        bottom_frame.grid(row=2, column=0)

        sql = """SELECT title, screening_date, screening_time FROM screenings WHERE screening_id = (%s);"""
        id_value = (self.screening_id, )
        screening_info = self.read_from_table(sql, id_value)
        print(screening_info[0], screening_info[1], screening_info[2])


        titleLabel = tk.Label(top_frame, text=screening_info[0], fg="#66ccff", width=20)
        titleLabel.grid(row=0, column=0)
        dateLabel = tk.Label(top_frame, text=screening_info[1], fg="#66ccff", width=20)
        dateLabel.grid(row=0, column=1)
        scr_time = "{:d}:{:02d}".format(screening_info[2].hour, screening_info[2].minute)
        timeLabel = tk.Label(top_frame, text=scr_time, fg="#66ccff", width=20)
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
        self.familyNumber = tk.Spinbox(middle_frame, from_=4, to=10, width=3)
        self.familyNumber.grid(row=3, column=2)

        addButton = tk.Button(bottom_frame, text="Add", bg="#33ff33", activebackground="#00e600", command=self.getValue)
        addButton.grid(row=0, column=0, padx=20)

if __name__ == "__main__":
    app = AddOrder(2)  

      



# master = tk.Tk()
# master.geometry('400x100')

# w = tk.Spinbox(master, from_=0, to=10, width=3)
# w.grid(row=0, column=0)

# master.mainloop()



# def sel():
#    selection = str(var.get())
#    print(selection)
#    st = selection.split()
#    print(st)
#    label1.config(text = st[0])
#    label2.config(text = st[1])

# root = tk.Tk()
# root.geometry('200x150')

# var = tk.StringVar(root, 'Option 1')
# R1 = tk.Radiobutton(root, text="Option 1", variable=var, value='Option 1',
#                   command=sel)
# R1.pack( anchor = tk.W )

# R2 = tk.Radiobutton(root, text="Option 2", variable=var, value='Optio 2',
#                   command=sel)
# R2.pack( anchor = tk.W )

# R3 = tk.Radiobutton(root, text="Option 3", variable=var, value='Opti 3',
#                   command=sel)
# R3.pack( anchor = tk.W)

# label1 = tk.Label(root)
# label1.pack()
# label2 = tk.Label(root)
# label2.pack()
# root.mainloop()