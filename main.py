def insertNumberListBox():
    listbox1.insert(listbox1.size(), textBox1.get())


def deleteNumberListBox():
    selection = listbox1.curselection()
    for i in reversed(selection):
        listbox1.delete(i)


def sendMessageDialog():
    message = simpledialog.askstring("Send Message", "Please enter your message")
    for x in range(listbox1.size()):
        py.sendwhatmsg_instantly(f"+90{listbox1.get(x)}", message, 10, True)


def sendTimedMessageDialog():
    counter = 0
    message = simpledialog.askstring("Send Message", "Please enter your message")
    hour = simpledialog.askinteger("Enter Hour", "Please enter your hour")
    minute = simpledialog.askinteger("Send Minute", "Please enter your minute")
    for x in range(listbox1.size()):
        counter = counter + 1
        if counter == 1:
            py.sendwhatmsg(f"+90{listbox1.get(x)}", message, hour, minute+1, 10, True)
        else:
            py.sendwhatmsg_instantly(f"+90{listbox1.get(x)}", message, 10, True)


def importNumber():
    fs = open("number_dbs.txt", "r")
    for x in fs:
        listbox1.insert(END, x)
    fs.close()


def isChecked():
    if checked.get() == 1:
        button2.configure(command=sendTimedMessageDialog)
    else:
        button2.configure(command=sendMessageDialog)


from tkinter import *
from tkinter import simpledialog
import pywhatkit as py

window = Tk()
window.title('WP Auto Message by Hyperizon')
window.geometry("350x380")

checked = IntVar()

checkbox1 = Checkbutton(window, text='Set time', variable=checked, onvalue=1, offvalue=0, command=isChecked)
label1 = Label(window, text="Please enter a message to be sent")
textBox1 = Entry(window, text="Enter number...", width=34)
button1 = Button(window, text="Add", command=insertNumberListBox)
button4 = Button(window, text="Delete", command=deleteNumberListBox)
button3 = Button(window, text="Import Number", command=importNumber)
listbox1 = Listbox(window, selectmode="multiple")
button2 = Button(window, text="Send", command=sendMessageDialog)

checkbox1.pack()
label1.pack()
textBox1.pack()
button1.pack()
button4.pack()
button3.pack()
listbox1.pack()
button2.pack()

window.mainloop()
