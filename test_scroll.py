import tkinter as tk

LABEL_BG = "#ccc"  # Light gray.
ROWS, COLS = 15, 3  # Size of grid.
ROWS_DISP = 8  # Number of rows to display.
COLS_DISP = 3  # Number of columns to display.

class MyApp(tk.Tk):
    def __init__(self, title="Sample App", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title(title)
        self.configure(background="Gray")
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        #self.geometry('800x800')

        master_frame = tk.Frame(self, bd=3, relief=tk.RIDGE)
        master_frame.grid(row=0, column=0)
        #sticky=tk.NSEW)
        # master_frame.columnconfigure(0, weight=1)
        # master_frame.rowconfigure(1, weight=1)


        top_frame = tk.Frame(master_frame, bg="Light Blue", bd=3, relief=tk.RIDGE)
        top_frame.grid(row=0, column=0)
        # top_frame.grid(sticky=tk.NSEW)
        # top_frame.columnconfigure((0,1,2), weight=1)

        

        frame1a = tk.Frame(top_frame, bg="Light blue", bd=2, relief=tk.GROOVE)
        frame1a.grid(row=0, column=0)
        #, sticky=tk.NSEW)
        #frame1a.columnconfigure(0, weight=1)

        frame1b = tk.Frame(top_frame, bg="Light blue", bd=2, relief=tk.GROOVE)
        frame1b.grid(row=0, column=1)#, sticky=tk.NSEW)
        #frame1b.columnconfigure(0, weight=1)

        frame1c = tk.Frame(top_frame, bg="Light blue", bd=2, relief=tk.GROOVE)
        frame1c.grid(row=0, column=2)#, sticky=tk.NSEW)
        #frame1c.columnconfigure(0, weight=1)

        label1a = tk.Label(frame1a, text="Frame1 Contents", bg="Light blue", width=20)
        label1a.grid(row=0, column=0, padx=3, pady=5)#, sticky=tk.N)

        label1b = tk.Label(frame1b, text="Frame1b Contents", bg="Light blue", width=20)
        label1b.grid(row=0, column=0, padx=3, pady=5)#, sticky=tk.N)

        label1c = tk.Label(frame1c, text="Frame1c Contents", bg="Light blue", width=20)
        label1c.grid(row=0, column=0, padx=3, pady=5)#, sticky=tk.N)

        cb_var1a = tk.IntVar()
        checkbutton1a = tk.Checkbutton(frame1a, text="StartCheckBox", variable=cb_var1a, bg="Light blue")
        checkbutton1a.grid(row=1, column=0, padx=2)#, sticky=tk.N)

        cb_var1b = tk.IntVar()
        checkbutton1b = tk.Checkbutton(frame1b, text="Startbb", variable=cb_var1b, bg="Light blue")
        checkbutton1b.grid(row=1, column=0, padx=2)#, sticky=tk.N)

        cb_var1c = tk.IntVar()
        checkbutton1c = tk.Checkbutton(frame1c, text="Startccc", variable=cb_var1c, bg="Light blue")
        checkbutton1c.grid(row=1, column=0, padx=2)#, sticky=tk.N)

        #####

        

        # Create a frame for the canvas and scrollbar(s).
        frame2 = tk.Frame(master_frame)
        frame2.grid(row=1, column=0, columnspan=3)#, sticky=tk.NSEW)
        # frame2.columnconfigure(0, weight=1)
        # frame2.rowconfigure(0, weight=1)

        # Add a canvas in that frame.
        canvas = tk.Canvas(frame2)
        canvas.grid(row=0, column=0)#, sticky=tk.NSEW)
        # canvas.columnconfigure(0, weight=1)
        # canvas.rowconfigure(0, weight=1)

        # Create a vertical scrollbar linked to the canvas.
        # to tez dziala
        vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=1, sticky=tk.NS)
        canvas.configure(yscrollcommand=vsbar.set)

                # Create a frame on the canvas to contain the buttons.
        ##################################
        # ten frame nie dziala, czerwone pole sie nie powieksza, moze to przez to, ze jest na canvas???
        labels_frame = tk.Frame(canvas, bd=2)
        labels_frame.grid(row=0, column=0, columnspan=3)#, sticky=tk.NSEW)
        # buttons_frame.columnconfigure(0, weight=1)
        #  
        # labels_frame.columnconfigure((0,1,2), weight=1)
        ################

        for i in range(15):
            for j in range(3):
                if j==0:
                    label = tk.Label(master=labels_frame, text=f"Row {i} Column {j}", width=20)
                    label.grid(row=i, column=j, padx=5, pady=5)#, sticky=tk.NSEW)
                elif j==1:
                    label = tk.Label(master=labels_frame, text=f"Row {i}", width=20)
                    label.grid(row=i, column=j, padx=5, pady=5)#, sticky=tk.NSEW)
                elif j==2:
                    label = tk.Label(master=labels_frame, text=f"Row", width=20)
                    label.grid(row=i, column=j, padx=5, pady=5)#, sticky=tk.NSEW)
               # label.columnconfigure(0, weight=1)

        # for i in range(15):
        #     label = tk.Label(master=buttons_frame, text=f"Row {i} Column 0")
        #     label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.NSEW)
            #label.columnconfigure(0, weight=1)

        # # Add the buttons to the frame.
        # for i in range(1, ROWS+1):
        #     for j in range(1, COLS+1):
        #         button = tk.Button(buttons_frame, padx=7, pady=7, relief=tk.RIDGE,
        #                            text="[%d, %d]" % (i, j))
        #         button.grid(row=i, column=j, sticky='news')

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=labels_frame, anchor=tk.NW)

        labels_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        #print('canvas.bbox(tk.ALL): {}'.format(bbox))

        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)

        # label3 = tk.Label(top_frame, text="Frame3 Contents", bg=LABEL_BG)
        # label3.grid(row=4, column=0, pady=5, sticky=tk.NW)

        # frame3 = tk.Frame(top_frame, bg="Blue", bd=2, relief=tk.GROOVE)
        # frame3.grid(row=5, column=0, sticky=tk.NW)

        # cb_var2 = tk.IntVar()
        # checkbutton2 = tk.Checkbutton(frame3, text="EndCheckBox", variable=cb_var2)
        # checkbutton2.grid(row=0, column=0, padx=2)


if __name__ == "__main__":
    app = MyApp("Scrollable Canvas")
    app.mainloop()