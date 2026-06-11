from tkinter import*
from tkinter import messagebox
root=Tk()
count=0
co=1
def a_click(a):
    global co,count
    if a["text"]==" " and co==1:
        a["text"]="X"
        count+=1
        co=0
        winner()
        tie()
    elif a["text"]==" " and co==0:
        a["text"]="O"
        count+=1
        co=1
        winner()
        tie()
    else:
        messagebox.showerror("Invalid","Enter in the vacant box")   

def disable():
    a1.config(state=DISABLED)
    a2.config(state=DISABLED)
    a3.config(state=DISABLED)
    a4.config(state=DISABLED)
    a5.config(state=DISABLED)
    a6.config(state=DISABLED)
    a7.config(state=DISABLED)
    a8.config(state=DISABLED)
    a9.config(state=DISABLED)
    


def reset():
     global a1,a2,a3,a4,a5,a6,a7,a8,a9
     a1["text"]=a2["text"]=a3["text"]=a4["text"]=a5["text"]=a6["text"]=a7["text"]=a8["text"]=a9["text"]=" "
     count,co
     a1.config(bg="white",state=NORMAL)
     a2.config(bg="white",state=NORMAL)
     a3.config(bg="white",state=NORMAL)
     a4.config(bg="white",state=NORMAL)
     a5.config(bg="white",state=NORMAL)
     a6.config(bg="white",state=NORMAL)
     a7.config(bg="white",state=NORMAL)
     a8.config(bg="white",state=NORMAL)
     a9.config(bg="white",state=NORMAL)
    


win=0
def winner():
    if a1["text"]=="X" and a2["text"]=="X" and a3["text"]=="X":
          win=1
          a1.config(bg="yellow")
          a2.config(bg="yellow")
          a3.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a4["text"]=="X" and a5["text"]=="X" and a6["text"]=="X":
          win=1
          a4.config(bg="yellow")
          a5.config(bg="yellow")
          a6.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a7["text"]=="X" and a8["text"]=="X" and a9["text"]=="X":
          win=1
          a7.config(bg="yellow")
          a8.config(bg="yellow")
          a9.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a1["text"]=="X" and a4["text"]=="X" and a7["text"]=="X":
          win=1
          a1.config(bg="yellow")
          a4.config(bg="yellow")
          a7.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a2["text"]=="X" and a5["text"]=="X" and a8["text"]=="X":
          win=1
          a2.config(bg="yellow")
          a5.config(bg="yellow")
          a8.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a3["text"]=="X" and a6["text"]=="X" and a9["text"]=="X":
          win=1
          a3.config(bg="yellow")
          a6.config(bg="yellow")
          a9.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a1["text"]=="X" and a5["text"]=="X" and a9["text"]=="X":
          win=1
          a1.config(bg="yellow")
          a5.config(bg="yellow")
          a9.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a3["text"]=="X" and a5["text"]=="X" and a7["text"]=="X":
          win=1
          a3.config(bg="yellow")
          a5.config(bg="yellow")
          a7.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a1["text"]=="O" and a2["text"]=="O" and a3["text"]=="O":
          win=1
          a1.config(bg="yellow")
          a2.config(bg="yellow")
          a3.config(bg="yellow")
          messagebox.showinfo("Result","X wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a4["text"]=="O" and a5["text"]=="O" and a6["text"]=="O":
          win=1
          a4.config(bg="yellow")
          a5.config(bg="yellow")
          a6.config(bg="yellow")
          messagebox.showinfo("Result","O wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a7["text"]=="O" and a8["text"]=="O" and a9["text"]=="O":
          win=1
          a7.config(bg="yellow")
          a8.config(bg="yellow")
          a9.config(bg="yellow")
          messagebox.showinfo("Result","O wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a1["text"]=="O" and a4["text"]=="O" and a7["text"]=="O":
          win=1
          a1.config(bg="yellow")
          a4.config(bg="yellow")
          a7.config(bg="yellow")
          messagebox.showinfo("Result","O wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a2["text"]=="O" and a5["text"]=="O" and a8["text"]=="O":
          win=1
          a2.config(bg="yellow")
          a5.config(bg="yellow")
          a8.config(bg="yellow")
          messagebox.showinfo("Result","O wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a3["text"]=="O" and a6["text"]=="O" and a9["text"]=="O":
          win=1
          a3.config(bg="yellow")
          a6.config(bg="yellow")
          a9.config(bg="yellow")
          messagebox.showinfo("Result","O wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a1["text"]=="O" and a5["text"]=="O" and a9["text"]=="O":
          win=1
          a1.config(bg="yellow")
          a5.config(bg="yellow")
          a9.config(bg="yellow")
          messagebox.showinfo("Result","O wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()
    elif a3["text"]=="O" and a5["text"]=="O" and a7["text"]=="O":
          win=1
          a3.config(bg="yellow")
          a5.config(bg="yellow")
          a7.config(bg="yellow")
          messagebox.showinfo("Result","O wins !!!")
          disable()
          z=messagebox.askyesno("New Game","Want to play another game?")
          if z==1:
             reset()

def tie():
    if win!=1 and a1["text"]!=" " and a2["text"]!=" " and a3["text"]!=" " and a4["text"]!=" " and a5["text"]!=" " and a6["text"]!=" " and a7["text"]!=" " and a8["text"]!=" " and a9["text"]!=" ":
        messagebox.showinfo("RESULT","ITS A TIE!!!")
        z=messagebox.askyesno("tie","Want to play another game?")
        if z==1:
           reset()
        else:
            messagebox.showinfo("HOPE YOU ENJOYED","HAVE A GREAT DAY AHEAD!!")
            disable()

a1=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a1))

a2=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a2))

a3=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a3))

a4=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a4))

a5=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a5))

a6=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a6))

a7=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a7))

a8=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a8))

a9=Button(root, text=" ",width=7,height=5,command=lambda: a_click(a9))

a1.grid(row=0,column=0)
a2.grid(row=0,column=1)
a3.grid(row=0,column=2)
a4.grid(row=1,column=0)
a5.grid(row=1,column=1)
a6.grid(row=1,column=2)
a7.grid(row=2,column=0)
a8.grid(row=2,column=1)
a9.grid(row=2,column=2)




root.mainloop()



