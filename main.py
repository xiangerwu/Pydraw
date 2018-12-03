#!/usr/bin/python
from tkinter import *
import tkinter.messagebox
import random
import time

def alert(titoru,content):  # MessageBox(懶人用)
     tkinter.messagebox.showinfo(titoru,content)

def begin():
    # Draw.configure(background="#ffde8b") # 背景顏色
    Draw.title("抽籤程式") # Title
    Draw.geometry('400x250')    # Screen Size
    Draw.bind('<Escape>',(lambda event: exit(0))) # 按<ESC>退出

def part():
    global chance
    global times
    global draws1
    global draws2
    times=0
    chance=5
    draws1=0
    draws2=0
    def Lottery():  # 抽獎過程
        global chance
        global times
        global draws1
        global draws2

        if(times==0):   # 未設定或已抽完
            alert("警告!"," 0 次你還抽啊")
            # Input.grid()    # 復原設定按鈕
            # Confirm.grid()
            # start.grid_remove() # 移除抽籤按紐
        elif(times>0):  # 未抽完
            times-=1   
            result=random.randint(1,10) # 產生亂數
            if(result<=chance): # 確認亂數機率，增加抽中的次數
                draws1+=1
                alert("抽籤結果",Lot1.get())
                times1.config(text=Lot1.get()+" ： "+str(draws1)+"次")
            else:
                draws2+=1
                alert("抽籤結果",Lot2.get())
                times2.config(text=Lot2.get()+" ： "+str(draws2)+"次")
        
    def Take(): # 決定次數
        global chance
        global times
        global draws1
        global draws2
        draws1=0
        draws2=0
        Draw.geometry('220x155')    
        if(len(Input.get())!=0 and len(Lot1.get())!=0 and len(Lot2.get())!=0):
            times=int(Input.get())
            Input.grid_remove()
            Lot1.grid_remove()
            Lot2.grid_remove()
            Confirm.grid_remove()
            sc0.grid_remove()
            sc1.grid_remove()
            sc2.grid_remove()
            Probability1.grid_remove()
            Probability2.grid_remove()
            ChanceUp.grid_remove()
            ChanceDown.grid_remove()
            show.config(text="總共抽 "+str(times)+" 次",)
            show.grid(row=0,column=0,padx=10,pady=10,stick=W)
            start.grid(row=1,column=0,padx=10,pady=1,stick=N+E+S+N)
            times1.config(text=Lot1.get()+" ： "+str(draws1)+"次")
            times2.config(text=Lot2.get()+" ： "+str(draws2)+"次")
            times1.grid(row=4,column=0,padx=10,pady=5,stick=W)
            times2.grid(row=5,column=0,padx=10,pady=5,stick=W)
        else:
            alert("警告!!","好歹輸入點什麼啊") 
   
    def change(x):  # 變更機率
        global chance
        if(x==0):
            if(chance>1):
                chance-=1
            else:
                alert("警告!","不能再大了")
        elif(x==1):
            if(chance<9):
                chance+=1
            else:
                alert("警告!","不能再小了")
        Probability1.config(text=str(chance)+"成機率")
        Probability2.config(text=str(10-chance)+"成機率")

    sc0=Label(Draw,text="抽籤的次數：",font=80)
    sc0.grid(row=0,column=0,padx=3) # 抽籤次數
    Input=Entry(Draw,font=80) 
    Input.grid(row=0,column=1,padx=0,pady=15,stick=W)

    sc1=Label(Draw,text="設定第一個選項：",font=80)
    sc1.grid(row=1,column=0,padx=3) # 輸入第一個選項
    Lot1=Entry(Draw,font=80)   
    Lot1.grid(row=1,column=1,pady=15)
    Probability1=Label(Draw,text=str(chance)+"成機率",font=80)  # 第一個籤的機率
    Probability1.grid(row= 1,column= 3)

    sc2=Label(Draw,text="設定第二個選項：",font=80)
    sc2.grid(row=2,column=0,padx=3) # 輸入第二個選項
    Lot2=Entry(Draw,font=80)    
    Lot2.grid(row=2,column=1,pady=15)
    Probability2=Label(Draw,text=str(10-chance)+"成機率",font=80)  # 第二個籤的機率
    Probability2.grid(row= 2,column= 3)
    
    ChanceUp=Button(Draw,text="▲",font=48,command=lambda:change(0)) # 調整機率按鈕<上升>
    ChanceDown=Button(Draw,text="▼",font=48,command=lambda:change(1))   # 調整機率按鈕<下降>

    ChanceUp.grid(row= 4,padx=10,pady=0,stick=W) 
    ChanceDown.grid(row= 4,padx=20,pady=0) 
    show=Label(Draw,font=80,width=20)
   
    times1=Label(Draw,font=200)  # 第一個已抽中次數
    times2=Label(Draw,font=200)  # 第二個已抽中次數
    Confirm=Button(Draw,text="產生籤筒",font=100,heigh=2,width=17,command=Take)   # 決定次數按鈕(重置)
    Confirm.grid(row=4,column=1,padx=5,pady=10,stick=E)
    start=Button(Draw,text="手中無籤，在此抽籤",font=48,width=20,command=Lottery)  # 抽籤按鈕
   

Draw=Tk()   # 產生視窗
begin() # 預設視窗大小
part()


Draw.mainloop()