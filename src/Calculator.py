import tkinter as tk
# from tkinter import *
from  tkinter import ttk
import math

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as mlines
# from ttk import *


val = 10

 

# Top level window and display it
root = tk.Tk()
root.title("Investment calculator")
# frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget
main_frame = tk.Canvas(root, width = 600, height = 1000, bg = '#AC99F2' ) # Sice of base window
main_frame.pack()


def plot():
	val = 10
	t = np.arange(0., val, 0.2)  # t goes from 0 to val, 0.2 increment
	plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g', t, 100*np.sin(t))
	plt.xlabel('entry a')
	plt.ylabel('entry b')
	# plt.title('Histogram of IQ')
	plt.suptitle('Categorical Plotting')
	blue_line = mlines.Line2D([], [], color='blue', marker='*',markersize=15, label='Blue stars')
	green_line = mlines.Line2D([], [], color='green', marker='',markersize=15, label='Green line')
	plt.legend(handles=[green_line, blue_line])
	plt.show()

def reset():
	pass
	# inp = int(input_txt.get(1.0, "end-1c"))
	# res = inp*inp
	# lbl.config(text = "Provided Input: "+ string(inp))
	# top_label.config(text= 'The result is in: ')
	# output_label.config(text =(f'{inp} squared is {res}'))

def calculate():
	# inp = int(input_txt.get(1.0, "end-1c"))
	# res = math.sqrt(inp)
	# lbl.config(text = "Provided Input: "+ string(inp))
	# output_label.config(text =(f'The square root of {inp} is: {res}'))
	res = compound.get()
	top_label.config(text= 'The result is in: ')
	output_label.config(text =(f'The output is is: {res}'))

# plot(10)	
    
# TextBox Creation for input Initial Investment
Step1_txt = tk.LabelFrame(main_frame,
				text= 'Step1: Initial Investment', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)
input_initial = tk.Text(main_frame,
				height = 1,font= 'bold',
				width = 10)

# TextBox Creation for input Monthly Contribution
Step2_txt = tk.LabelFrame(main_frame,
				text= 'Step2: Monthly Contribution', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)
input_monthly = tk.Text(main_frame,
				height = 1,font= 'bold',
				width = 10)

# TextBox Creation for input Monthly Contribution
Step3_txt = tk.LabelFrame(main_frame,
				text= 'Step3: Annual interest rate in %', 
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)
input_interest = tk.Text(main_frame,font= 'bold',
				height = 1,
				width = 10)


# get compound rate from choice box

Step4_txt = tk.LabelFrame(main_frame,
				text= 'Step4: Choose compound frequency',
				fg='white', bg = 'blue', font= 'bold',
				height = 40,
				width = 300)

choices = ['Annually', 'Monthly', 'Quarterly']
variable = tk.StringVar(main_frame)
variable.set('Annually')
compound = ttk.Combobox(main_frame, values = choices, height = 6,
				width = 10)



# # Button Creation
# square_button = tk.Button(main_frame,
# 						text = "X^2",
# 						command = square, fg="white", bg='blue')

# Button Creation
calculate_button = tk.Button(main_frame,
						text = "Calculate",
						command = calculate, font= 'bold',fg="white", bg='blue')

plot_button = tk.Button(main_frame,
						text = 'Plot Function',
						command = plot,font= 'bold', fg="white", bg='blue')


reset_button = tk.Button(main_frame,
						text = "Reset",
						command = exit,font= 'bold', fg="white", bg='blue')


# Label Creation for output
top_label = tk.Label(main_frame, text = '' )
output_label  = tk.Label(main_frame, text = '')

main_frame.create_window(150, 30, window=Step1_txt)  # click me
main_frame.create_window(500, 30, window=input_initial)  # click me
main_frame.create_window(150, 90, window=Step2_txt)  # click me
main_frame.create_window(500, 90, window=input_monthly)  # click me
main_frame.create_window(150, 150, window=Step3_txt)  # click me
main_frame.create_window(500, 150, window=input_interest)  # click me
main_frame.create_window(150, 210, window=Step4_txt)  # click me
main_frame.create_window(500, 210, window=compound)  # click me
# main_frame.create_window(500, 50, window=variable)  # click me
main_frame.create_window(150, 350, window=calculate_button)  # click me
main_frame.create_window(300, 350, window=reset_button)  # click me
# main_frame.create_window(200, 150, window=square_root_button)  # quit x,y
main_frame.create_window(200, 600, window=plot_button)  # quit x,y

main_frame.create_window(200, 400, window=top_label)  # quit x,y
main_frame.create_window(200, 440, window=output_label)  # quit x,y

# plot(10)
main_frame.mainloop()
# print(inputtxt.get(1.0, "end-1c"))
