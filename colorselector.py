from tkinter import *
from tkinter import colorchooser

class color:
    def __init__(self,root):
        self.root=root
        self.root.title("Color Chooser")
        self.root.geometry("300x300")
        self.root.resizable(0,0)
        #self.root.iconbitmap("color.ico")

        def color():
            bgcolor=colorchooser.askcolor(title="Select Color")
            TXT.insert(END,"" + bgcolor[1]+"\n")
            #TXT.config(bg=bgcolor[1])


        def on_enter1(e):
            But_color['background']="black"
            But_color['foreground']="cyan"
  
        def on_leave1(e):
            But_color['background']="SystemButtonFace"
            But_color['foreground']="SystemButtonText"

        #Frame===============
        Main_Frame=Frame(self.root,bg="gray76",relief=RIDGE,bd=3,width=300,height=300)
        Main_Frame.place(x=0,y=0)

        Frame_top=Frame(Main_Frame,width=295,height=100,bd=3,bg="gray50",relief=RIDGE)
        Frame_top.place(x=0,y=0)

        Frame_bottom=Frame(Main_Frame,width=295,height=195,bd=3,bg="white",relief=RIDGE)
        Frame_bottom.place(x=0,y=100)


        #===================Button================================
        Lab_color=LabelFrame(Frame_top,text="Select Color",width=290,height=95,bg="#0b0550",fg="pink")
        Lab_color.place(x=0,y=0)

        But_color=Button(Lab_color,text="Select Color",font=('times new roman',10,"bold"),width=13,height=1,cursor="hand2",command=color)
        But_color.place(x=85,y=20)
        But_color.bind("<Enter>",on_enter1)
        But_color.bind("<Leave>",on_leave1)

        #================Frame_bottom
        TXT=Text(Frame_bottom, width=40,height=11,font=('arial',10,'bold'),bd=5,bg="#c4c5df",relief=RIDGE,state="normal",fg="black")
        TXT.place(x=0,y=0)


if __name__ == "__main__":
    root=Tk()
    app=color(root)
    root.mainloop()
