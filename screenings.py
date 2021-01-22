import  tkinter as tk
from tkinter import ttk
import psycopg2
from config import config
from queries import select_all

class ShowScreenings:
    def __init__(self):
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
        # self.radiobutton_vars.append(var)

        for i in range(rows):
            #var = tk.IntVar()
            radiobutton = tk.Radiobutton(master=self.middle_frame, variable=self.var, value=i)
            radiobutton.grid(row=i, column=0)
            #self.radiobutton_vars.append(var)

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
        print(idx, ": ", self.read_id[idx])


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

if __name__ == '__main__':
    root = ShowScreenings()


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
 
# root = tk.Tk() 
# root.geometry('200x100')

# labelTop = tk.Label(root,
#                     text = "Choose your favourite month")
# labelTop.grid(column=0, row=0)

# comboExample = ttk.Combobox(root, 
#                             values=[
#                                     "January", 
#                                     "February",
#                                     "March",
#                                     "April"])
# print(dict(comboExample)) 
# comboExample.grid(column=0, row=1)
# comboExample.current(1)

# print(comboExample.current(), comboExample.get())

# root.mainloop()

###################################################################

# import tkinter as tk
# from tkinter import ttk


# class Combo:
#     def __init__(self):
#         self.root = tk.Tk() 
#         self.root.geometry('200x100')
#         self.show()
#         self.root.mainloop()

#     # def callbackFunc(self, event):
#     #         print("New Element Selected: ", self.comboExample.get())

#     # def get_name(self):
#     #     self.comboExample.bind("<<ComboboxSelected>>", self.callbackFunc)

#     def cmd(self):
#         a = self.comboExample.get()
#         print(a)

#     def show(self):
#         labelTop = tk.Label(self.root,
#                             text = "Choose your favourite month")
#         labelTop.grid(column=0, row=0)

#         self.comboExample = ttk.Combobox(self.root, 
#                                     values=[
#                                             "January AAAA", 
#                                             "February BBB",
#                                             "March CCC",
#                                             "April DDD"])


#         self.comboExample.grid(column=0, row=1)
#         self.comboExample.current(1)
#         button1 = tk.Button(self.root, text="Get value", command=self.cmd, activebackground='Lime')
#         button1.grid(row=2, column=0)
#         #self.get_name()
#         #print(self.comboExample.get())

# if __name__ == "__main__":
#     root = Combo()

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
