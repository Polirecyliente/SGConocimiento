
#   TkInter

#T# TkInter is an API for GUI programming

#T# import the TkInter module
import tkinter

#T# create a window with Tk()
topW1 = tkinter.Tk()

#T# give the window's dimensions with geometry()
topW1.geometry("1000x400")

#T# callback function for button press
def bPress1():
    print("Button was pressed\nB1var:",B1var.get(),"\nB2var:",B2var.get(),
        "\nE1var:",E1var.get(),"\nlistbox1:",listbox1.curselection(),
        "\n",radioVar.get(),"was selected","\nSlide value:",slidVar.get(),
        "\nSpinner value:",spinVar.get())
    print("Text mark idx:",text1.index("markCreated1"),"\nText tag idx:",
        text1.tag_ranges("tagCreated1"))

#T# create a button with Button()
button1 = tkinter.Button(topW1,text="press",relief='ridge',command=bPress1)

coords1 = (10,15,50,85)
#T# create a canvas with Canvas()
canvas1 = tkinter.Canvas(topW1,cursor="circle",bg="pink")
arc1 = canvas1.create_arc(coords1,fill='light blue')
line1 = canvas1.create_line(coords1)
oval1 = canvas1.create_oval(coords1)

#T# create tkinter python variables with IntVar(), StringVar(), DoubleVar(), and BooleanVar()
B1var = tkinter.IntVar()
B2var = tkinter.IntVar()

#T# create checkbuttons with Checkbutton()
checkB1 = tkinter.Checkbutton(topW1,text="Opt1",variable=B1var,
        state=tkinter.DISABLED)
checkB2 = tkinter.Checkbutton(topW1,text="Opt2",variable=B2var)

E1var = tkinter.StringVar()
#T# create one line text entry with Entry()
entry1 = tkinter.Entry(topW1,show="*",textvariable=E1var)

#T# create a frame for widgets with Frame()
frame1 = tkinter.Frame(topW1,bd=7,width=500,height=600)

#T# create a label with Label()
label1 = tkinter.Label(frame1,textvariable=E1var)

#T# create a listbox with Listbox()
listbox1 = tkinter.Listbox(frame1,selectmode=tkinter.EXTENDED,height=3)

#T# create a scrollbar with Scrollbar()
scroll1 = tkinter.Scrollbar(topW1,repeatdelay=1000,repeatinterval=600,
        troughcolor="orange",command=listbox1.yview)

#T# add yscrollcommand to listbox after creating the scrollbar
listbox1.config(yscrollcommand=scroll1.set)

#T# insert options into listbox with insert()
listbox1.insert(4,"Option1")
listbox1.insert(3,"Option2")
listbox1.insert(1,"Option3")
listbox1.insert(2,"Option4")
listbox1.insert(5,"Option5")
listbox1.insert(6,"Option6")

def m1Press1():

#T# create new window with Toplevel()
    newWin = tkinter.Toplevel(topW1)

#T# put window off and on with withdraw() and deiconify()
    newWin.withdraw()
    newWin.deiconify()

#T# change a window's title with title()
    newWin.title("Window from menu")

#T# create a menu button with Menubutton()
menuButton1 = tkinter.Menubutton(topW1,anchor=tkinter.E,text="menu button",
                width=17)

#T# create a menu that will hold menu options with Menu()
menuOptions1 = tkinter.Menu(menuButton1,title="tearoffMenu",
                postcommand=m1Press1)

#T# add a menu's options to a menubutton with menubutton["menu"] = menuOpts
menuButton1["menu"] = menuOptions1

#T# add a checkbutton to a menu's options with add_checkbutton
menuOptions1.add_checkbutton(label="FMenu1")

def m2Press1():
    print("menu2 button1 was pressed")
def m2Press2():
    print("menu2 button2 was pressed")
#T# create a menu button as part of the menubar with Menu()
menuBar1 = tkinter.Menu(topW1)
menuOptions2 = tkinter.Menu(menuBar1)
menuOptions2.add_command(label="command1",command=m2Press1)
menuOptions2.add_separator()
menuOptions2.add_command(label="command2",command=m2Press2)

#T# add a menu's options to the menubar with add_cascade()
menuBar1.add_cascade(label="menu opts name",menu=menuOptions2)

#T# create a message box with Message()
messg1 = tkinter.Message(topW1,text="Hello\nThis message text appears in\
                the window for the current program in execution")

radioVar = tkinter.StringVar()
#T# create radio buttons with Radiobutton()
radioB1 = tkinter.Radiobutton(topW1,text="radioOption1",value="Op1",
            variable=radioVar)
radioB2 = tkinter.Radiobutton(topW1,text="radioOption2",value="Op2",
            variable=radioVar)
radioB3 = tkinter.Radiobutton(topW1,text="radioOption3",value="Op3",
            variable=radioVar)

slidVar = tkinter.StringVar()
#T# create a slider scale with Scale()
slider1 = tkinter.Scale(topW1,variable=slidVar,from_=8,to=23,label="amount",
    orient=tkinter.HORIZONTAL,resolution=0.2,tickinterval=6.5)

#T# create a text widget with Text()
text1 = tkinter.Text(topW1,insertontime=2000,insertofftime=1000,
        insertwidth=35,insertborderwidth=4,spacing2=20,tabs=27,
        wrap=tkinter.WORD)

#T# insert characters into a text widget with insert()
text1.insert(tkinter.END,"inserted text, this is a long string to make up \
to 2 or more lines of text in the screen. Repeated lines are not allowed")

#T# create a mark with mark_set()
text1.mark_set("markCreated1","1.15")
text1.insert("markCreated1","INSM")

#T# create a tag with tag_add()
text1.tag_add("tagCreated1","1.20","1.30")
text1.tag_config("tagCreated1",foreground="#FF00FF")

spinTup = (3,92,"str1",64)
spinVar = tkinter.StringVar()
#T# create a spinner with Spinbox()
spinner1 = tkinter.Spinbox(frame1,values=spinTup,
        textvariable=spinVar)

#T# create a pane for widgets with PanedWindow()
panedW1 = tkinter.PanedWindow(frame1,sashwidth=30,showhandle=tkinter.ON)

panedScale1 = tkinter.Scale(panedW1)
panedButton1 = tkinter.Button(panedW1,text="PanedB1",bitmap="hourglass")
#T# add widgets to a paned window with add()
panedW1.add(panedScale1)
panedW1.add(panedButton1)

import tkinter.messagebox
def retIg():

#T# display a message box with the messagebox module of tkinter
    tkinter.messagebox.askretrycancel("ask Title","press retry or cancel")

#T# create a labeled frame with LabelFrame()
labelFr1 = tkinter.LabelFrame(topW1,text="labeled frame",
    labelanchor=tkinter.S)
button2 = tkinter.Button(labelFr1,text="ButtonInLabelframe",command=retIg,
    font=("Helvetica",20,"overstrike","italic","bold"))

#T# place widgets with place(), pack(), and grid()
button1.place(x = 50,y=50)
canvas1.place(x=130,y=20)
checkB1.pack()
checkB2.pack()
entry1.pack(side=tkinter.RIGHT)
frame1.place(x=10,y=90)
label1.grid()
listbox1.grid()
menuButton1.pack()
messg1.pack()
radioB1.pack()
radioB2.pack()
radioB3.pack()
slider1.pack()
scroll1.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text1.pack()
spinner1.grid()
panedW1.grid()
labelFr1.place(x=600,y=15)
button2.grid()

#T# place menubar in window with config(menu = menubar1)
topW1.config(menu = menuBar1)

#T# display the window and wait for events with mainloop()
topW1.mainloop()