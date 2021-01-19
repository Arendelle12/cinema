
import  tkinter as tk
from tkinter import ttk
import psycopg2
from config import config

class ShowScreenings:
    def __init__(self):
        self.app = tk.Tk() 
        self.app.geometry('600x250')
        self.master_frame = tk.Frame(self.app, relief=tk.RIDGE)
        self.master_frame.grid(row=0, column=0)
        self.show()
        self.app.mainloop()

    def read_from_table(self, sql, data = None):
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
            cur.execute(sql, data)
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

    def callbackFunc(self, event):
        movie = self.comboExample.get()

        title = (movie, )
        sql = """SELECT title, screening_date, screening_time FROM screenings WHERE title = (%s) ORDER BY screening_date, screening_time;"""
        records = self.read_from_table(sql, title)

        read_titles = []
        read_dates = []
        read_times = []
        
        for r in records:
            read_titles.append(r[0])
            read_dates.append(r[1])
            read_times.append("{:d}:{:02d}".format(r[2].hour, r[2].minute))
         
        rows = self.read_from_table("""SELECT COUNT(*) FROM screenings WHERE title = (%s);""", title)[0][0]
        cols = 3

        for widget in self.bottom_frame.winfo_children():
            widget.destroy()

        for j in range(cols):
            for i in range(rows):
                if(j == 0):
                    label = tk.Label(master=self.bottom_frame, text=read_titles[i], width=20)
                if(j == 1):
                    label = tk.Label(master=self.bottom_frame, text=read_dates[i], width=20)
                if(j == 2):
                    label = tk.Label(master=self.bottom_frame, text=read_times[i], width=20)

                label.grid(row=i, column=j, padx=5, pady=5, sticky="N")

    def show(self):
        top_frame = tk.Frame(self.master_frame, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)

        self.bottom_frame = tk.Frame(self.master_frame, relief=tk.RIDGE)
        self.bottom_frame.grid(row=1, column=0, sticky="N")
        
        data = self.read_from_table("""SELECT title FROM screenings GROUP BY title ORDER BY title;""")
        titles=[]
        for i in data:
            titles.append(i[0])
        labelTop = tk.Label(top_frame, text = "Choose movie")
        labelTop.grid(row=0, column=0)

        self.comboExample = ttk.Combobox(top_frame, values=titles)
        self.comboExample.grid(row=1, column=0, padx=200)
        self.comboExample.current()

        self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

if __name__ == '__main__':
    app = ShowScreenings()


# import tkinter as tk 
# from tkinter import ttk 
  
# # Creating tkinter window 
# window = tk.Tk() 
# window.geometry('500x350') 
# # Label 
# tk.Label(window, text = "Select the Month :").grid(column = 0, row = 15, padx = 10, pady = 25) 
  
# n = tk.StringVar() 
# monthchoosen = ttk.Combobox(window, width = 27,  
#                             textvariable = n) 
  
# # Adding combobox drop down list 
# monthchoosen['values'] = (' January',  
#                           ' February', 
#                           ' March', 
#                           ' April', 
#                           ' May', 
#                           ' June',  
#                           ' July',  
#                           ' August',  
#                           ' September',  
#                           ' October',  
#                           ' November',  
#                           ' December') 
  
# monthchoosen.grid(column = 1, row = 15) 
 
# monthchoosen.current() 
# month = monthchoosen.get() 
# print(month)
# window.mainloop() 

###################################################

# import tkinter as tk
# from tkinter import ttk
 
# app = tk.Tk() 
# app.geometry('200x100')

# labelTop = tk.Label(app,
#                     text = "Choose your favourite month")
# labelTop.grid(column=0, row=0)

# comboExample = ttk.Combobox(app, 
#                             values=[
#                                     "January", 
#                                     "February",
#                                     "March",
#                                     "April"])
# print(dict(comboExample)) 
# comboExample.grid(column=0, row=1)
# comboExample.current(1)

# print(comboExample.current(), comboExample.get())

# app.mainloop()

###################################################################

# import tkinter as tk
# from tkinter import ttk


# class Combo:
#     def __init__(self):
#         self.app = tk.Tk() 
#         self.app.geometry('200x100')
#         self.show()
#         self.app.mainloop()

#     # def callbackFunc(self, event):
#     #         print("New Element Selected: ", self.comboExample.get())

#     # def get_name(self):
#     #     self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

#     def cmd(self):
#         a = self.comboExample.get()
#         print(a)

#     def show(self):
#         labelTop = tk.Label(self.app,
#                             text = "Choose your favourite month")
#         labelTop.grid(column=0, row=0)

#         self.comboExample = ttk.Combobox(self.app, 
#                                     values=[
#                                             "January AAAA", 
#                                             "February BBB",
#                                             "March CCC",
#                                             "April DDD"])


#         self.comboExample.grid(column=0, row=1)
#         self.comboExample.current(1)
#         button1 = tk.Button(self.app, text="Get value", command=self.cmd, activebackground='Lime')
#         button1.grid(row=2, column=0)
#         #self.get_name()
#         #print(self.comboExample.get())

# if __name__ == "__main__":
#     app = Combo()

#############################################

# from tkinter import *

# class Checkbar(Frame):
#    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
#       Frame.__init__(self, parent)
#       self.vars = []
#       for pick in picks:
#          var = IntVar()
#          chk = Checkbutton(self, text=pick, variable=var)
#          chk.pack(side=side, anchor=anchor, expand=YES)
#          self.vars.append(var)

#    def state(self):
#       return map((lambda var: var.get()), self.vars)


# if __name__ == '__main__':
#    root = Tk()
#    lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
#    tgl = Checkbar(root, ['English','German'])
#    lng.pack(side=TOP,  fill=X)
#    tgl.pack(side=LEFT)
#    lng.config(relief=GROOVE, bd=2)

#    def allstates(): 
#         print(type(lng))
#         print(list(lng.state()), list(tgl.state()))
#         a = list(lng.state())
#         for i in a:
#             print(type(i))
#             if i == 1:
                

#    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
#    Button(root, text='Peek', command=allstates).pack(side=RIGHT)

   

#    root.mainloop()
