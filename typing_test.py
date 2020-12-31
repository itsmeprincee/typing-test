from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
# list of characters to diaplay the text
easy_words = ["king","queen","rathod","vijay","pubg","freefire","sarda","suryanarayan","sandhya","laxminarayana","vamsi","pavan","mahesh","mounika","is","a","chair","table","gate","a","b","c","d","e","f","g","h","i",'j',"k","l","m","n","o","p","q",'r',"s",'t','u','v','w','x','y','z',"Door","T.V","Refrigrator","Box","Bedsheet","Switches","Wires","Plugs","Torch" ,"Light","Card","ID","Pan","Aadhaar","Ruby","Web","Ewc","Johnson","Years","Warranty","Adani","Fortified","Scheme","Stock","Oil","Jio","Refined","Vitamins","Turkey","Charger","Godrej","God","Evil","Devil","Ghost","Rocks","Stones","For"]
medium_words = ["1","2","3","4","5","6","7","8","9","0","fLOOr","CeiL","MotherBoard","Cpu","keyBoaRd","MouSe","PrInce","ChipSet","USb","porT","netWork","siM","GPu","BUS","Data","Bus","Address","BUs","Microprocessor","Ground","vcc","GitHub","stack","Exchange","resumE","Intelligence","Circuit","HDMI Port","Sensor","Charging","Dvd","penDrive","Camera","Hacking","Hackerrank"]
special_characters = ['!','@',"#","$","%","^","&","*","(",")","+","_","-","=","{","}","[","]",";",":","<",">","?","/",".",",","|"]
random_word=None
# it is used to diaplay the text that the user wants to enter into a entry box
def textvar():
    global easy_words,medium_words,special_characters,t1,n,text_box,random_word,entry_box
    input_type = n.get()
    if input_type != "Easy" and input_type!="Medium" and input_type!="High":
        messagebox.showerror("combobox error","Please select the level of the text")
    else:
        entry_box.delete(0,END)
        if input_type == "Easy":
            random_word = str(" ".join(random.sample(easy_words,30)))
        elif input_type == "Medium":
            random_word = str(" ".join(random.sample((easy_words+medium_words),40)))
        elif input_type =="High":
            random_word = str(" ".join(random.sample((easy_words+medium_words+special_characters),50)))
        text_box.config(text=random_word)
        t1 = time.time()
# it is used to verify the input text is accuracy rate,speed of typing..
def verification():
    global t1,random_word,entry_box,strr,n
    entered_word=""
    errors=0
    t2 = time.time()
    input_type = n.get()
    input_data = strr.get()
    if input_type != "Easy" and input_type!="Medium" and input_type!="High":
        messagebox.showerror("combobox error","Please select the level of the text")
    else:
        if random_word==None:
            messagebox.showerror("input error","please click \"start\" button")
        elif len(input_data)==0:
            messagebox.showerror("input error","please enter valid data in entry box")
        else:
            if len(input_data) > len(random_word):
                messagebox.showinfo("result","\"your input data is greater than actual data\"")
            else:
                mins,secs=divmod(t2-t1,60)
                hours,mins= divmod(mins,60)
                try:
                    for x in range(len(random_word)):
                        if input_data[x]!=random_word[x]:
                            errors +=1
                            entered_word += "~"
                        else:
                            entered_word += random_word[x]
                except:
                    errors += len(random_word)-len(input_data)
                    entered_word += "~~"
                accuracy = (((len(random_word)-int(errors))/len(random_word))*100)
                #messagebox.showinfo("result",str(int(hours))+"h"+" "+str(int(mins))+"m"+" "+str(int(secs))+"s"+str(errors))
                text_box.config(text=entered_word)
                messagebox.showinfo("result","Errors :"+" "+str(errors)+"/"+str(len(random_word))+"\n"+"Time :"+" "+str(int(hours))+"h"+" "+str(int(mins))+"m"+" "+str(int(secs))+"s"+"\n"+"Acuuracy :"+" "+str(accuracy))
#it is used to reset all input_data
def reset_data():
    global entry_box,random_word,text_box
    entry_box.delete(0,END)
    random_word=""
    text_box.config(text="")

#defining gadgets to display the user interface
def gadgets():
    global strr,text_box,entry_box,n
    #heading to display the title of the window...
    heading_label = Label(parent,text="Typing Test",font=("Helvetica",18,"bold"),bg="white",fg="black")
    heading_label.pack()
    description = Label(parent,text="NOTE : \"You have to enter the text carefully without any error\".\n the Time will count down when you tap the start button and ended up when you tap submit button\nYour errors will be replaced with \"~\" symbol..\"~\" indicates single error and \"~~\" indicates more than single error",font=("times new roman",12,"italic"),bg="white",fg="black",pady=5)
    description.pack()
    #combo box to select the difficulty of the text
    n=StringVar()
    combo = ttk.Combobox(parent,width=20,textvariable=n)
    combo.pack()
    combo['values']=["Easy","Medium","High"]
    combo.current()
    n.set("select level")
    #a Frame that contains the text and entry box to display the text and an entry box to enter the displayed data
    input_frame = Frame(parent,bg="white",pady=10)
    input_frame.pack()
    #text to show the user to enter
    text_box = Message(input_frame,width=800,anchor=W,justify="left",font=("times new roman",14,"bold"),padx=0,pady=0,bg="ghostwhite")
    text_box.grid(row=0,column=0,columnspan =3)
    #a box to show the user to enter text..
    Entry_label = Label(input_frame,text="Enter text here:",bg="white",font=("Helvetica",12,"bold"),fg="#d19a66")
    Entry_label.grid(row=1,column=0,padx=5)
    strr = StringVar()
    entry_box = Entry(input_frame,font=("Helvetica",10,"bold"),width=70,textvariable=strr,justify="left",bd=0,insertbackground="blue",bg="silver",highlightthickness=5)
    entry_box.grid(row=1,column=1,pady=20,ipady=10,padx=5)
    #buttons used to diaplay the action performed by the user
    bottom_buttons = Frame(parent,bg="white")
    bottom_buttons.pack(side=BOTTOM)
    #start button to start the typing test
    start_button = Button(bottom_buttons,text="start",height=2,width=20,bd=0,bg='#61afef',command=textvar)
    start_button.grid(row=0,column=0,padx=5,pady=5)
    #submit button to validate the user data...
    submit_button = Button(bottom_buttons,text="Submit",height=2,width=20,bd=0,bg="#8ab171",command=verification)
    submit_button.grid(row=0,column=1,padx=5)
    #reset button to clear the text fileds..
    reset_button = Button(bottom_buttons,text="reset",height=2,width=20,bd=0,bg="#9a63ae",command=reset_data)
    reset_button.grid(row=0,column=2,padx=5)

parent = Tk()
parent.title("Typing Test")
parent.resizable(False,False)
parent.geometry("800x400")
parent.config(bg="white")
gadgets()
parent.mainloop()
