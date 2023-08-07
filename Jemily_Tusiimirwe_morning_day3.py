import tkinter as tk
def button_click(number):
    current = entry.get()
    entry.delete(0,tk,END)
    entry.insert(tk.END,current + str(number))

def button_clear():
    entry.delete(0,tk.END)
def button_equal():
    expression=entry.get()
    result=eval(expression)
    entry.delete(0,tk.END)
    entry.insert(tk.END,result)
#creating the main window
window=tk.Tk()
window.title("Jemily_Tusiimirwe_simple_calculator")

entry = tk.Entry(window,width=30,justify="right")
entry.grid(row=0, column=0,columnspan=4)
#creating number buttons
button1 = tk.Button(window,text="1",padx=10,pady=5,command=lambda:button_click(1))  
button2 = tk.Button(window,text="2",padx=10,pady=5,command=lambda:button_click(2))
button3 = tk.Button(window,text="3",padx=10,pady=5,command=lambda:button_click(3))  
button4 = tk.Button(window,text="4",padx=10,pady=5,command=lambda:button_click(4)) 
button5= tk.Button(window,text="5",padx=10,pady=5,command=lambda:button_click(5)) 
button6 = tk.Button(window,text="6",padx=10,pady=5,command=lambda:button_click(6)) 
button7 = tk.Button(window,text="7",padx=10,pady=5,command=lambda:button_click(7)) 
button8 = tk.Button(window,text="8",padx=10,pady=5,command=lambda:button_click(8)) 
button9 = tk.Button(window,text="9",padx=10,pady=5,command=lambda:button_click(9)) 
button0 = tk.Button(window,text="0",padx=10,pady=5,command=lambda:button_click(0)) 
#creating operatorbuttons
button_add = tk.Button(window,text="+",padx=10,pady=5,command=lambda:button_click('+'))
button_divide = tk.Button(window,text="/",padx=10,pady=5,command=lambda:button_click('/'))
button_subtract = tk.Button(window,text="-",padx=10,pady=5,command=lambda:button_click('-'))
button_multiply = tk.Button(window,text="*",padx=10,pady=5,command=lambda:button_click('*'))

button_equal=tk.Button(window,text="=",padx=10,pady=5,command=button_equal)
button_clear=tk.Button(window,text="C",padx=10,pady=5,command=button_clear)

#Arranging buttons on the grid
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_divide.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button_subtract.grid(row=3,column=3)

button0.grid(row=4,column=1)
button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_multiply.grid(row=1,column=3)

window.mainloop()










