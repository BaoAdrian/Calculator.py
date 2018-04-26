################################################################################################
#
# Simple calculator with minimal testing. Just a raw sample of a Calculator program made
# using python implementing use of lambda functions and tkinter GUI package.
#
# 
# To Do: Catch division by zero error
# 		 Format padding and clickable field
#
#
################################################################################################


from tkinter import*


def btn_Click(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btn_Clear():
	global operator
	operator = ""
	text_Input.set("")


def btn_Equals():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator = ""


cal = Tk()
cal.title("My Calculator")
operator = ""
text_Input = StringVar()


text_display = Entry(cal, font = ('arial', 20, 'bold'), textvariable = text_Input, bd = 30, insertwidth = 4, 
	bg = "light steel blue", justify = 'right')

text_display.grid(columnspan = 4)

# First row (from the top)

btn7 = Button(
	cal, 
	activebackground = "firebrick1", 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20,'bold'), 
	text = "7", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(7)
	)

btn7.grid(row = 1, column = 0)


btn8 = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "8", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(8))

btn8.grid(row = 1, column = 1)


btn9 = Button(cal, 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "9", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(9))

btn9.grid(row = 1, column = 2)


addition_btn = Button(cal, 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "+", 
	bg = "deep sky blue", 
	command = lambda :btn_Click("+"))

addition_btn.grid(row = 1, column = 3)



# Second row (from the top)

btn4 = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "4", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(4))

btn4.grid(row = 2, column = 0)


btn5 = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "5", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(5))

btn5.grid(row = 2, column = 1)


btn6 = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "6", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(6))

btn6.grid(row = 2, column = 2)


subtraction_btn = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 2, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "-", 
	bg = "deep sky blue", 
	command = lambda :btn_Click("-"))

subtraction_btn.grid(row = 2, column = 3)



# Third row (from the top)

btn1 = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 8, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "1", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(1))

btn1.grid(row = 3, column = 0)


btn2 = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 8, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "2", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(2))

btn2.grid(row = 3, column = 1)


btn3 = Button(
	cal, padx = 16, 
	pady = 16, 
	bd = 8, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "3", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(3))

btn3.grid(row = 3, column = 2)

multiplication_btn = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 8, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "*", 
	bg = "deep sky blue",
	command = lambda :btn_Click("*"))

multiplication_btn.grid(row = 3, column = 3)



# Fourth row (from the top) 

btn_Clear = Button(
	cal, 
	padx = 16, 
	pady = 16,
	bd = 8,
	fg = "black",
	font = ('arial', 20, 'bold'), 
	text = "C", 
	bg = "deep sky blue", 
	command = btn_Clear)

btn_Clear.grid(row = 4, column = 0)


btn0 = Button(
	cal, 
	padx = 16,
	pady = 16, 
	bd = 8, 
	fg = "black",
	font = ('arial', 20, 'bold'), 
	text = "0", 
	bg = "deep sky blue", 
	command = lambda :btn_Click(0))

btn0.grid(row = 4, column = 1)


btn_Equals = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 8, 
	fg = "black", 
	font = ('arial', 20,'bold'), 
	text = "=", 
	bg = "deep sky blue", 
	command = btn_Equals)

btn_Equals.grid(row = 4, column = 2)


division_btn = Button(
	cal, 
	padx = 16, 
	pady = 16, 
	bd = 8, 
	fg = "black", 
	font = ('arial', 20, 'bold'), 
	text = "/", 
	bg = "deep sky blue", 
	command = lambda :btn_Click("/"))

division_btn.grid(row = 4, column = 3)



# Loop until user exits
cal.mainloop()



# END