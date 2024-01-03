import tkinter as tk

def setText(button):
    players = [" ","X","O"]    
    indx = (players.index(button.cget("text")) + 1) % len(players)
    txt = players[indx]
    button.config(text=txt)

root=tk.Tk()
root.title('X/O')
size = 20
wW = 6
hH = 3

button1=tk.Button(root,text=" ", command=lambda: setText(button1) ,width=wW, height=hH, font=('halvetica', size))
button1.grid(row=0,column=0)
button2=tk.Button(root, text=" ", command=lambda: setText(button2) ,width=wW, height=hH, font=('halvetica', size))
button2.grid(row=0,column=1)
button3=tk.Button(root, text=" ", command=lambda: setText(button3) ,width=wW, height=hH, font=('halvetica', size))
button3.grid(row=0,column=2)
button4=tk.Button(root, text=" ", command=lambda: setText(button4) ,width=wW, height=hH, font=('halvetica', size) )
button4.grid(row=1,column=0)
button5=tk.Button(root, text=" ", command=lambda: setText(button5) ,width=wW, height=hH ,font=('halvetica', size))
button5.grid(row=1,column=1)
button6=tk.Button(root, text=" ", command=lambda: setText(button6) ,width=wW, height=hH ,font=('halvetica', size))
button6.grid(row=1,column=2)
button7=tk.Button(root, text=" ", command=lambda: setText(button7) ,width=wW, height=hH ,font=('halvetica', size))
button7.grid(row=2,column=0)
button8=tk.Button(root, text=" ", command=lambda: setText(button8) ,width=wW, height=hH ,font=('halvetica', size))
button8.grid(row=2,column=1)
button9=tk.Button(root, text=" ", command=lambda: setText(button9) ,width=wW, height=hH ,font=('halvetica', size))
button9.grid(row=2,column=2)

root.mainloop()
