# from tkinter import *
import tkinter as tk
from  tkinter import ttk
import math

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

for i in range(10):

    my_game.insert(parent='',index='end',iid=i,text='',
    values=[(f'Year {i}'),'1000',str(1000+i*12*1000)])
# my_game.insert(parent='',index='end',iid=1,text='',
# values=['Year 1','13670','13000'])


my_game.pack()

ws.mainloop()