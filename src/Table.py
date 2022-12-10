# from tkinter import *
import tkinter as tk
from  tkinter import ttk
# import math
from formula import calculate_capital

def print_csv():
    pass

def show_table(P, m,  r, Compound_frequ, num_years):
   
    ws  = tk.Tk()
    ws.title(f'Total Savings in AUD after {num_years} years')


    table_frame = tk.Frame(ws, width = 500, height = 800, bg = '#AC99F2' )

    table_frame.pack()

# ttk.Treeview.column(column_id, anchor=Tkinter.E)
    my_table = ttk.Treeview(table_frame) 

    my_table['columns'] = ('Years', 'Accrued', 'Total Contributions')

    my_table.column("#0", width=0,  stretch=tk.YES)
    my_table.column("Years",anchor=tk.CENTER, width=80)
    my_table.column("Accrued",anchor=tk.E,width=180)
    my_table.column("Total Contributions",anchor=tk.E,width=180)


    my_table.heading("#0",text="",anchor=tk.CENTER)
    my_table.heading("Years",text="Years",anchor=tk.CENTER)
    my_table.heading("Accrued",text="Accrued end of Year",anchor=tk.CENTER)
    my_table.heading("Total Contributions",text="Total Contributions",anchor=tk.CENTER)

    for i in range(1,num_years+1, 1):
        capital = int(calculate_capital(P, m,  r, Compound_frequ, i))

        my_table.insert(parent='',index='end',iid=i,text='',
        values=[(f'Year {i}'),(f'{"{:,}".format(capital)} '), f'{m*12*i}'])

    calculate_button = tk.Button(ws,
						text = " Print .CSV ",
						command = print_csv, font= 'bold',fg="white", bg='blue')
    calculate_button.pack(side = tk.BOTTOM)
   


    # show table
    my_table.pack()


    ws.mainloop()

show_table(0,100,18,'monthly' ,50)