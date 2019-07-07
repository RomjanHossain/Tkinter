'''Importing some necessery things'''
from tkinter import *
import tkinter.messagebox

'''setting-up  the window'''
window = Tk()
#window.config
window.title("Convert D/H/B")
window.geometry('600x400')
window.resizable(False,False)

'''defining some converting functions '''


''' Converting decimal to binary function'''

def conv_bin(event):
	value = entry_display.get()
	if value == '':
		tkinter.messagebox.showerror('Value Error', 'Enter some value \nPlease! ')
	else:
		value = int(value)
		bina = bin(value).replace('0b','')
		display_value = Label(window,fg='red',font =("Times", 14, "bold italic"))
		display_value['text']=bina
		display_value.grid(row=4,column=2)


'''Converting decimal value to hexa-value'''
def conv_hex(event):
	value = entry_display.get()
	if value =='':
		tkinter.messagebox.showerror('Value Error', 'Enter some value \nPlease! ')

	else:
		value = int(value)
		hexa = hex(value).replace('0x','')
		display_value = Label(window,fg='red',font =("Times", 14, "bold italic"))
		display_value['text']= hexa
		display_value.grid(row=5,column=2)


'''converting binary to decimal value'''


def bin_deci(event):
	value = entry_display.get()
	if value =='':
		tkinter.messagebox.showerror('Value Error', 'Enter some value \nPlease! ')
	else:
		def binary(x):
			value = str(x)
			value = list(value)
			deci = 0
			for i in range(len(value)):
				power = value.pop()
				if power =='1':
					deci +=pow(2,i)
			return deci

		bi=binary(value)
		display_value = Label(window,fg='red',font =("Times", 14, "bold italic"))
		display_value['text']=bi
		display_value.grid(row=6,column=2)


'''converting hexa-decimal to Decimal'''


def hex_deci(something):
	value = entry_display.get()
	if value !='':
		def hex_deci(x):
			value = str(x)
			return int(value,16)
		hi=hex_deci(value)
		display_value=Label(window,fg='red',font =("Times", 14, "bold italic"))
		display_value['text']=hi
		display_value.grid(row=7,column=2)
	else:
		tkinter.messagebox.showerror('Value Error',"Enter a valid number")


'''Here goes the Title'''
title = Label(window, text='Input Interger',fg='green',font =("Times", 14, "bold italic"))
title.grid(row=1,column=1,padx=6,pady=6,columnspan=4)

'''Here's the input values '''

entry_display = Entry(window,bd = 5,width=40)
entry_display.place(x=10, y=10, width=100) #width in pixels
entry_display.grid(row = 2,column = 1 )


'''Converting tilte'''
convert_to = Label(window, text="Convert To",fg='black',font =("Times", 14, "bold italic"))
convert_to.grid(row=3,column=0)

'''Result title'''

result = Label(window, text = "Result32",fg='black',font =("Times", 14, "bold italic"))
result.grid(row = 3, column=2)
'''Here's goes the fucking buttons part '''

'''Binary button'''


bina_btn = Button(window, text = 'Binary',fg='green',font =("Times", 14, "bold italic"))
bina_btn.bind("<Button-1>", conv_bin)
bina_btn.grid(row=4,column=0)

signal = Label(window, text = "====>",fg='black',font =("Times", 14, "bold italic"))
signal.grid(row=4,column=1)


'''Hexa-decimal button'''


hexa_btn = Button(window, text = 'Hexa-Decimal', fg='green',font=("TImes", 14,"bold italic"))
hexa_btn.bind("<Button-1>", conv_hex )
hexa_btn.grid(row=5,column=0)

signal1 = Label(window, text = "====>",fg='black',font =("Times", 14, "bold italic"))
signal1.grid(row=5,column=1)

'''binary to decimal button'''


deci_btn = Button(window, text = 'Binary to Decimal',fg='green',font =("Times", 14, "bold italic"))
deci_btn.bind("<Button-1>", bin_deci )
deci_btn.grid(row=6,column=0)

signal2 = Label(window, text = "====>",fg='black',font =("Times", 14, "bold italic"))
signal2.grid(row=6,column=1)

'''hexa to decimal'''


deci_btn2 = Button(window, text='Hexa-Decimal to Decimal',fg='green',font=("Times",14,"bold italic"))
deci_btn2.bind("<Button-1>",hex_deci)
deci_btn2.grid(row=7,column=0)

signal3 = Label(window, text = "====>",fg='black',font =("Times", 14, "bold italic"))
signal3.grid(row=7,column=1)

'''The finishing part'''

window.mainloop()
