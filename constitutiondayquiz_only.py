from tkinter import *
from tkinter.font import *
root=Tk()
quiz=Frame(root,background="gold")
quiz.pack()
root.geometry("850x720")
root.title("Constitution Quiz")
root.config(bg="gold")
fonts=Font(size=20)

score=0
ans=""
mylabel1=Label(quiz,text="")
realans=Label(quiz,text="")
i=0

def answer(value):
    global score
    global ans
    global fonts
    global mylabel1
    global realans
    global i
    global nextbutton
    global radio1, radio2, radio3
    radio1.config(state=DISABLED)
    radio2.config(state=DISABLED)
    radio3.config(state=DISABLED)
    
        
    if value==ans:
       score=score+10
       mylabel1=Label(quiz,text="Correct Answer",font=fonts,bg="fuchsia",padx=20,pady=20,width=15)
       mylabel1.grid(row=6)
       myscore=Label(quiz,text="Your Score:  "+str(score),font=fonts,bg="fuchsia",padx=20,pady=20,width=15)
       myscore.grid(row=7)
       

    else:
        mylabel1=Label(quiz,text="Wrong Answer",font=fonts,bg="fuchsia",padx=20,pady=20,width=15)
        mylabel1.grid(row=6)
        myscore=Label(quiz,text="Your Score:  "+str(score),font=fonts,bg="fuchsia",padx=20,pady=20,width=15)
        myscore.grid(row=7)
        realans=Label(quiz,text="The Correct Answer Is: "+ans,font=fonts,bg="sienna",fg="ivory",padx=20,pady=20,width=77)
        realans.grid(row=8)
        
radio=StringVar()
radio.set(radio)

question=""
def nextquestion():
    global i
    global ans
    global question
    global mylabel1
    global realans
    global radio1, radio2, radio3
    global nextbutton
    mylabel1.destroy()
    realans.destroy()
    
    if i<15:            
        q=["(1) Which Day Is Celebrated To Honour The Date On \n Which The Constitution Of India Came Into Effect?",
           "(2) Who Wrote The Constitution Of India?",
           "(3) Who Was The First Chairman Of The Constituent Assembly?",
           "(4) What Is Celebrated On 26 November Across India Every Year?",
           "(5) From What Is The Basic Structure of the Constitution Adopted?",
           "(6) Which Is Often Referred To As The Mini Constitution Of India?",
           "(7) Which Of The Following Words Was Not Inserted \n Through The Forty Second Amendment Of The Constitution, 1976?",
           "(8) Which Feature Of Our Constitution Was Adopted \n From The Constitution Of Australia?",
           "(9) From Which Country\'s Constitution Is The Preamble Of India Adopted From?",
           "(10) By What Other Name Is The Constitution Of India Referred To?",
           "(11) The Finance Commissions Are Commissions Periodically \n Constituted Under Article 280 Of Our Constitution.\n Who Constitutes The Finance Commission After Every 5 Years?",
           "(12) Which Major Feature Does The Article 12 To 35 \n Contained In Part III of Our Constitution deal with?",
           "(13) Which Following Is Not True Regarding The Constitution Of India?",
           "(14) Which Of The Follwing Is Incorrectly Matched?",
           "(15) Which Of The Following Is Often Referred To AS \"The Bag Of Borrowings\"?"]

       
        o=[["(a) Independence Day","(b) Republic Day","(c) Rashtriya Ekta Diwas"],
           ["(a) B.R.Ambedkar","(b) Kanaiyalal Maneklal Munshi","(c) Prem Behari Narain Raizada"],
           ["(a) Sachchidananda Sinha","(b) B.R.Ambedkar","(c) Harendra Coomar Mookerjee"],
           ["(a) Constitution Day","(b) National Unity Day","(c) Civil Services Day"],
           ["(a) Constitution Of The USSR","(b) The Montagu–Chelmsford Reforms","(c) The Government of India Act, 1935"],
           ["(a) The Preamble","(b) First Amendment Act, 1951","(c) The 42nd Amendment Act, 1976"],
           ["(a) Socialist","(b) Fraternity","(c) Integrity"],
           ["(a) The Preamble","(b) Right To Information","(c) Concurrent Lists"],
           ["(a) France","(b) USA","(c) USSR"],
           ["(a) Ashthadyayi Granthaḥ","(b) Megadhuta Pustaki","(c) Bharatiya Samvidhana"],
           ["(a) The Prime Minister","(b) The President","(c) The Speaker Of Lok Sabha"],
           ["(a) Fundamental Duties","(b) Judicial Review","(c) Fundamental Rights"],
           ["(a) At Its Enactment, The Constitution Had 10 Schedules","(b) At Its Enactment,The Constitution Had 395 Articles","(c) At its enactment,The Constitution had 22 Parts"],
           ["(a) Right To Equality - Articles: 14-18","(b) Right to Freedom - Articles: 19-22","(c) Cultural And Educational Rights - Articles: 39-40"],
           ["(a) The Preamble","(b) The Indian Constitution","(c) Right To Constitutional Remedies"]]
       
       
        a=["(b) Republic Day","(c) Prem Behari Narain Raizada","(a) Sachchidananda Sinha","(a) Constituion Day",
           "(c) The Government of India Act, 1935","(c) The 42nd Amendment Act, 1976","(b) Fraternity",
           "(c) Concurrent Lists","(a) France","(c) Bharatiya Samvidhana","(b) The President","(c) Fundamental Rights",
           "(a) At Its Enactment, The Constitution Had 10 Schedules","(c) Cultural And Educational Rights - Articles: 39-40",
           "(b) The Indian Constitution"]
       
        question=Label(quiz,text=q[i],anchor='c',font=fonts,bg="blanchedalmond",padx=50,pady=100,width=100,height=1).grid(row=2)
        ans=a[i]
        radio1=Radiobutton(quiz,text=o[i][0],command=lambda:answer(radio.get()),variable=radio,value=o[i][0],indicatoron=0,selectcolor="lightgreen",anchor='w',font=fonts,bg="teal",padx=100,pady=25,width=38,height=1)
        radio1.grid(row=3,column=0)
        radio2=Radiobutton(quiz,text=o[i][1],command=lambda:answer(radio.get()),variable=radio,value=o[i][1],indicatoron=0,selectcolor="lightgreen",anchor='w',font=fonts,bg="teal",padx=100,pady=25,width=38,height=1)
        radio2.grid(row=4,column=0)
        radio3=Radiobutton(quiz,text=o[i][2],command=lambda:answer(radio.get()),variable=radio,value=o[i][2],indicatoron=0,selectcolor="lightgreen",anchor='w',font=fonts,bg="teal",padx=100,pady=25,width=38,height=1)
        radio3.grid(row=5,column=0)
        i=i+1
        nextbutton=Button(quiz,text="Next Question",command=nextquestion,font=fonts,bg="darkmagenta",padx=20,pady=20,width=20)
        nextbutton.grid(row=9)
        exitbutton=Button(quiz,text="End Quiz",command=root.destroy,padx=20,pady=20,font=fonts,bg="crimson",width=20).grid(row=10)
        
    if i==15:
        nextbutton.config(state=DISABLED)

def startIspressed():
    global labeltext
    global btnStart
    
    global lblRules
    global empty1
    global empty2
    labeltext.destroy()
    
    lblRules.destroy()
    empty1.destroy()
    empty2.destroy()
    btnStart.grid_forget()    
    nextquestion()
    
    
labeltext = Label(quiz, text = "GA activity \n Constitution Quiz \n By Rithvik, Shrihari, Varun", font = ("Comic sans MS",30,'bold'), background = "gold",pady=50)
labeltext.grid(row=5)

btnStart = Button(quiz, text="Start", command=startIspressed, font=("Showcard Gothic", 30), bg="plum", fg="darkmagenta",pady=20)
btnStart.grid(row=20)

empty1=Label(quiz,text="",bg="gold")
empty1.grid(row=25)
empty2=Label(quiz,text="",bg="gold")
empty2.grid(row=30)

lblRules = Label(quiz,text="This Quiz Contains 15 Questions\nPlease Unmute To answer\nClick Start Once You Are ready",width=100,font=("Consolas", 14),background="honeydew",foreground="black")
lblRules.grid(row=40)


root.mainloop()

