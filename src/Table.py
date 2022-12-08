# from tkinter import *
import tkinter as tk
from  tkinter import ttk
# import math
from formula import calculate_capital

def print_csv():
    pass

def show_table(P, m,  r, Compound_frequ, num_years):
    A=0
    ws  = tk.Tk()
    ws.title('Total Savings in AUD')
    # ws.geometry('500x600')
    # ws['bg'] = '#AC99F2'

    game_frame = tk.Frame(ws, width = 500, height = 800, bg = '#AC99F2' )
    # game_frame = tk.Frame(ws)
    game_frame.pack()

    # my_game = ttk.Treeview(main_frame) 
    my_game = ttk.Treeview(game_frame) 
    # my_game.geometry('500x600')

    my_game['columns'] = ('Years', 'Accrued', 'Total Contributions')

    my_game.column("#0", width=0,  stretch=tk.YES)
    my_game.column("Years",anchor=tk.CENTER, width=80)
    my_game.column("Accrued",anchor=tk.CENTER,width=180)
    my_game.column("Total Contributions",anchor=tk.CENTER,width=180)


    my_game.heading("#0",text="",anchor=tk.CENTER)
    my_game.heading("Years",text="Years",anchor=tk.CENTER)
    my_game.heading("Accrued",text="Accrued end of Year",anchor=tk.CENTER)
    my_game.heading("Total Contributions",text="Total Contributions",anchor=tk.CENTER)

    for i in range(1,num_years+1, 1):
        A = calculate_capital(P, m,  r, Compound_frequ, i)

        my_game.insert(parent='',index='end',iid=i,text='',
        values=[(f'Year {i}'),str(round(A,2)), m*12*i])

    calculate_button = tk.Button(ws,
						text = " Print .CSV ",
						command = print_csv, font= 'bold',fg="white", bg='blue')
    calculate_button.pack(side = tk.BOTTOM)
   
    # game_frame.create_window(150, 350, window=calculate_button)  # calculate capital, show graph
# my_game.insert(parent='',index='end',iid=1,text='',
# values=['Year 1','13670','13000'])

    # show table
    my_game.pack()


    ws.mainloop()

#show_table(0,100,18,'monthly' ,50)