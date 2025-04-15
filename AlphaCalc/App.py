import tkinter as tk

root = tk.Tk()

# === dimensions ===
root.title("Simple Calc for math n chem in HS") #title
root.configure(background="#df7fd5") #background colour
root.minsize(500,500) #how small it should be
root.maxsize(500,500)  #how big i can make it
#root.geometry("300x300+50+50") #the size and shape of window when we first run it 300x300 - size  +50+50 - where it should appear on screen
# === labels ===
#tk.Label(root,text="Calc - short for calculus ").pack()

# === Frames ===
#Calculations visualizer
frame = tk.Frame(root, width=450, height=150, bg="#f4b6ed").pack(padx=10,pady=10) #padxy - "distance beetwen other widgets"

#0-9 buttons
buttons_frame = tk.Frame(root,width=325,height=300,bg="#f4b6ed").place(x=25,y=185)
def buttons():
    x = [40,120,200]
    y = [210,300,390]
    nr = 1
    for i in range(3):
        for j in range(3):
            ButtonFrame = tk.Frame(buttons_frame,width=60,height=60,bg="#df7fd5")
            ButtonFrame.place(x=x[j],y=y[i])                                        #if u do it in 1 line it wont actually assign a place to a frame
            tk.Button(ButtonFrame,text=f"{nr}",bg="#df7fd5",fg="#f4b6ed",).place(x=0,y=0,width=60,height=60)
            nr +=1
    ButtonFrame_0 = tk.Frame(buttons_frame,width=60,height=240,bg="#df7fd5")
    ButtonFrame_0.place(x=280,y=210)
    tk.Button(ButtonFrame_0,text="0",bg="#df7fd5",fg="#f4b6ed",).place(x=0,y=0,width=60,height=240)
buttons()

#calculations buttons
calculations_frame = tk.Frame(root,width=100,height=300,bg="#f4b6ed").pack(padx=25,pady=10,side=tk.RIGHT)

ButtonFramePlus = tk.Frame(calculations_frame,width=75,height=60,bg="#df7fd5").place(x=388,y=210)
ButtonFrameMinus = tk.Frame(calculations_frame,width=75,height=60,bg="#df7fd5").place(x=388,y=300)
ButtonFrameEqual = tk.Frame(calculations_frame,width=75,height=60,bg="#df7fd5").place(x=388,y=390)

root.mainloop()

