'''Import tkinter module and create a window and size it accordingly.
  A  variable is assigned to get entry(Just like normal input).
  typ variable is assigned to find type of operation performed.'''
##########################################################################################################################
##########################################################################################################################    

from tkinter import *
from tkinter.font import *
window=Tk()
root=Frame(window,background="CadetBlue",width=30)
root.grid()
window.title("Simple Calculator")
typ=""
fonts=Font(size=12)
fonts1=Font(size=18)
##########################################################################################################################
##########################################################################################################################    

#Various functions are created to perform the taks
'''Button click is used count or store a number when a number button is pressed'''
def sndstart():
    import constitutiondayquiz.py
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number) )

#Functions for particular operations are created(+,-,x,/)
#Addition   
def button_add():
    global typ
    typ="add"
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    return

#Multiplication
def button_multiply():
    global typ
    typ="multiply"
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    return

#Division
def button_divide():
    global typ
    typ="divide"
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    return

#Subtraction
def button_subtract():
    global typ
    typ="subtract"
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)
    return

#Function to specify how program should proceed when '=' is pressed
#Equal_to(=)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if typ=="add":
        e.insert(0,f_num+int(second_number))
    if typ=="multiply":
        e.insert(0,f_num*int(second_number))
    if typ=="divide":
        x=f_num/int(second_number)
        y=len(str(x))-2
        if str(x)[-2:]==".0":
            e.insert(0,str(x)[:y])
        else:
             e.insert(0,f_num/int(second_number))
    if typ=="subtract":
        e.insert(0,f_num-int(second_number))

#Clear button to ensure that  calculations do not get mixed up.
#Clear            
def button_clear():
    e.delete(0,END)
    
#The calculator is defined inside a function to call to when the start button is clicked
def calculator():
    
    #The widgets added in the introduction page are forgotten
    button_start.grid_forget()
    xyz.grid_forget()
    yz.grid_forget()
    button_start1.grid_forget()
    x.grid_forget()

    #Global scope is defined to the buttons
    global button_add
    global button_subtract
    global button_multiply
    global button_divide
    global button_equal
    global button_clear
    global button_exit
    global e
    
    #An entry box is created
    e=Entry(root,width=35,borderwidth=5)
    e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    
    #Various buttons are defined to be displayed and the created functions are linked to them
    #Buttons for numbers(These are linked to button_click)
    button_1=Button(root,text="1",padx=45,pady=20.2,command=lambda:button_click(1),width=2,font=fonts).grid(row=3,column=0)
    button_2=Button(root,text="2",padx=42,pady=20,command=lambda:button_click(2),width=2,font=fonts).grid(row=3,column=1)
    button_3=Button(root,text="3",padx=40,pady=20.3,command=lambda:button_click(3),width=2,font=fonts).grid(row=3,column=2)
    button_4=Button(root,text="4",padx=45,pady=20,command=lambda:button_click(4),width=2,font=fonts).grid(row=2,column=0)
    button_5=Button(root,text="5",padx=42,pady=20,command=lambda:button_click(5),width=2,font=fonts).grid(row=2,column=1)
    button_6=Button(root,text="6",padx=40,pady=20.3,command=lambda:button_click(6),width=2,font=fonts).grid(row=2,column=2)
    button_7=Button(root,text="7",padx=45,pady=20,command=lambda:button_click(7),width=2,font=fonts).grid(row=1,column=0)
    button_8=Button(root,text="8",padx=42,pady=20,command=lambda:button_click(8),width=2,font=fonts).grid(row=1,column=1)
    button_9=Button(root,text="9",padx=40,pady=20.3,command=lambda:button_click(9),width=2,font=fonts).grid(row=1,column=2)
    button_0=Button(root,text="0",padx=45,pady=20.5,command=lambda:button_click(0),width=2,font=fonts).grid(row=4,column=0)

    #Buttons for the 4 operators(These are linked to button_add,button_subtract,button_multiply,button_divide)
    button_add=Button(root,text="+",padx=37,pady=14,command=button_add,bg="#ffd300",width=2,height=1,font=fonts1).grid(row=4,column=1)
    button_multiply=Button(root,text="×",padx=37,pady=14.8,command=button_multiply,bg="#ffd300",width=2,height=1,font=fonts1).grid(row=5,column=1)
    button_subtract=Button(root,text="−",padx=35.2,pady=14,command=button_subtract,bg="#ffd300",width=2,height=1,font=fonts1).grid(row=4,column=2)
    button_divide=Button(root,text="÷",padx=35.2,pady=14.5,command=button_divide,bg="#ffd300",width=2,height=1,font=fonts1).grid(row=5,column=2)

    #button for equal to operator(This is linked to button_equal)
    button_equal=Button(root,text="=",padx=41,pady=83,command=button_equal,bg="#ff6600",width=2,font=fonts1,height=1).grid(row=5,column=0,rowspan=3)

    #Buttons for clear and exit(Clear is linked to button_clear and Exit can be defined directly using .destroy)
    button_clear=Button(root,text="Clear",command=button_clear,padx=86,pady=20,bg="#616161",fg="#ffffff",width=4,font=fonts).grid(row=6,column=1,columnspan=2)
    button_exit=Button(root,text="Exit",command=window.destroy,padx=86,pady=18,bg="#ff0021",fg="#ffffff",width=4,font=fonts).grid(row=7,column=1,columnspan=2)

    #A label is created to notify the user to click 'Clear' button after every calculation
    label=Label(root,text="  NOTE: Click  'Clear'  After  Each  Calculation To  Avoid  Errors.  ",width=46,padx=3.4).grid(row=8,column=0,columnspan=3,rowspan=1)
##########################################################################################################################
##########################################################################################################################    

#Formatting for the start page is done here
Label(root,bg='CadetBlue').grid(row=2)
Label(root,bg='CadetBlue').grid(row=3)
Label(root,bg='CadetBlue').grid(row=4)
Label(root,bg='CadetBlue').grid(row=8)
'''Label(root).grid(row=9)
Label(root).grid(row=10)
Label(root,height=5).grid(row=11)'''
xyz=Label(root,text="Computer Science Project",font=("Alfarn",30))
xyz.grid(row=1,column=5)
yz=Label(root,text="Simple Calculator",fg="white",bg='CadetBlue',font=("Copperplate Gothic Light",30),width=30)
yz.grid(row=2,column=5)
button_start=Button(root,text="Startq",command=sndstart,bg="DarkOrange",fg="black",font=("Britannic Bold",35),width=10,height=2)
button_start1=Button(root,text="Startc",command=calculator,bg="DarkOrange",fg="black",font=("Britannic Bold",35),width=10,height=2)
button_start.grid(row=10,column=5)
button_start1.grid(row=11,column=5)
x=Label(root,height=5)
x.grid(row=15)

##########################################################################################################################
##########################################################################################################################    

window.mainloop()

##########################################################################################################################
##########################################################################################################################    

#Information On Other things in this source code
''''xyz=Button()' is used to create a button.
  'xyz=Label()' is used to create a label.
  'xyz=Entry()' is used to get an input box.
  Any widget that is created has to be put into the main window by 'Widget_name(windowname)'.
  width,height,padx,pady,fg,bg are used for formatting(To make the output look good).
  for the execution of the program '.mainloop' has to be added.
 ' global variable_name' is used to access a variable defined inside a function at any other part of the program'''
#End

##########################################################################################################################
##########################################################################################################################    

                                                                                                                    #THANKYOU
