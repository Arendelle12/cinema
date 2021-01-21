import tkinter as tk
from tkinter import ttk
import psycopg2
from config import config

# class AddOrder:
#    def __init__(self):
#       self.root = tk.Tk()
#       self.root.title('Add order')

#       self.add()
#       self.root.mainloop()

#    def read_from_table(self, sql, values = None):
#       conn = None
#       try:
#          # read database configuration
#          params = config()
#          # connect to the PostgreSQL database
#          conn = psycopg2.connect(**params)
#          # create a new cursor
#          cur = conn.cursor()
#          # execute the INSERT statement
#          cur.execute(sql, values)
#          #return value
#          data = cur.fetchall()
#          # commit the changes to the database
#          conn.commit()
#          # close communication with the database
#          cur.close()
#       except (Exception, psycopg2.DatabaseError) as error:
#          print(error)
#       finally:
#          if conn is not None:
#                conn.close()

#       return data

#    def callbackFunc(self, event):
#       movie = self.comboExample.get()

#       title = (movie, )


#    def add(self):
#       master_frame = tk.Frame(self.root, relief=tk.RIDGE)
#       master_frame.grid(row=0, column=0)

#       top_frame = tk.Frame(master_frame, relief=tk.RIDGE)
#       top_frame.grid(row=0, column=0)

#       self.middle_frame = tk.Frame(master_frame, relief=tk.RIDGE)
#       self.middle_frame.grid(row=1, column=0)

#       bottom_frame = tk.Frame(master_frame, relief=tk.RIDGE)
#       bottom_frame.grid(row=2, column=0)

#       titleLabel = tk.Label(top_frame, text="Select movie", bg="#66ccff")
#       titleLabel.grid(row=0, column=0)

#       data = self.read_from_table("""SELECT title FROM screenings GROUP BY title ORDER BY title;""")
#       titles=[]
#       for i in data:
#          titles.append(i[0])
      
#       self.comboExample = ttk.Combobox(top_frame, values=titles)
#       self.comboExample.grid(row=1, column=0, padx=20)
#       self.comboExample.current()

#       self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

      



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