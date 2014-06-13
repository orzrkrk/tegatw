# -*- coding:utf-8 -*- 
import sys
import Tkinter

def on_clicked():
    print "ボタンが押された！"
def on_clickExit(event):
    sys.exit()  #exit
#button
window = Tkinter.Tk() 
Tkinter.Button(window, text = "押してください。", command = on_clicked).pack()

#check box
Tkinter.Checkbutton(window, text = "check button").pack()

#entry
entry = Tkinter.Entry(window)
entry.insert(Tkinter.END, "END")
entry.pack()

#scale
Tkinter.Scale(window, orient = Tkinter.HORIZONTAL).pack()

Tkinter.Button(window, text = "exit", command = on_clickExit).pack()
window.mainloop()
