from tkinter import *
import time
import random
from _operator import pos

class Ball:
    def __init__(self,canvas, color, thanh):
        self.canvas= canvas
        self.thanhtruot=thanh
        self.id= canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,100,200)
        start=[-3,-2,-1,1,2,3]
        random.shuffle(start)
        self.x=start[0];
        self.y=1;
        self.canvas_height= 500;
        self.canvas_width= 400;
        self.over= False
        
    def vacham(self, pos):
        pos_thanhTruot= self.canvas.coords(self.thanhtruot.id)
        if pos[0]>=pos_thanhTruot[0] and pos[0]<= pos_thanhTruot[2]:
            if pos[1]>=pos_thanhTruot[1] and pos[3]<=pos_thanhTruot[3]:
                return True
        return False 
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos= self.canvas.coords(self.id)
        if pos[1] <=0:
            self.y=3
        if pos[3]>= self.canvas_height:
            self.over=True
        if self.vacham(pos)== True:
            self.y=-3;
        if pos[0]<= 0:
            self.x=3
        if pos[2]>= self.canvas_width:
            self.x=-3

class thanhTruot:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id= canvas.create_rectangle(0,0,100,20, fil= color)
        self.canvas.move(self.id,300,400)
        self.canvas.bind_all('<KeyPress-Left>',self.trai)
        self.canvas.bind_all('<KeyPress-Right>',self.phai)
        self.x=0;
        self.y=0;
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        
    def trai(self,event):
        self.x=-2.5
    def phai(self,event):
        self.x=2.5

        
tk= Tk()
tk.title("Game Do Bong_Le Truong Ngoc Huy")
tk.resizable(0,0)
can= Canvas(tk,width=400,height=500)
can.pack()

thanh= thanhTruot(can, "black")
bong= Ball(can, "red",thanh)

while 1:
    if bong.over != True:
        bong.draw()
        thanh.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        break;

tk.mainloop()