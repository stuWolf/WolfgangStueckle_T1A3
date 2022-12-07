# from tkinter import *
import tkinter as tk
from  tkinter import ttk
# import math
from formula import calculate_capital
def table(num_years, m):
    A=0
    ws  = tk.Tk()
    ws.title('Total Savings in AUD')
    ws.geometry('500x500')
    ws['bg'] = '#AC99F2'

    game_frame = tk.Frame(ws)
    game_frame.pack()

    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('Years', 'Accrued', 'Total Contributions')

    my_game.column("#0", width=0,  stretch=tk.NO)
    my_game.column("Years",anchor=tk.CENTER, width=80)
    my_game.column("Accrued",anchor=tk.CENTER,width=160)
    my_game.column("Total Contributions",anchor=tk.CENTER,width=160)


    my_game.heading("#0",text="",anchor=tk.CENTER)
    my_game.heading("Years",text="Years",anchor=tk.CENTER)
    my_game.heading("Accrued",text="Accrued end of Year",anchor=tk.CENTER)
    my_game.heading("Total Contributions",text="Total Contributions",anchor=tk.CENTER)

    for i in range(1,num_years+1, 1):
        A += calculate_capital('monthly',18, m, 0,i)
        my_game.insert(parent='',index='end',iid=i,text='',
        values=[(f'Year {i}'),str(round(A,2)), m*12*i])
# my_game.insert(parent='',index='end',iid=1,text='',
# values=['Year 1','13670','13000'])


    my_game.pack()

    ws.mainloop()

table(10, 100)