from tkinter import *
import time
import random


window = Tk()
window.geometry('1600x900')
window.resizable(width=False, height=False)
window.title('Рулетка')

class Restangeles:
    def __init__(self, num, text):
        self.num = num
        self.outline = 'white'
        self.text = text
        self.x = 10*(self.num%10) + 149*((self.num-1)%10) if self.num % 10 != 0 else 10*10 + 149*9
        self.x_2 = self.x + 149
        self.y = 10*(self.num//10+1)+79*(self.num//10) if self.num % 10 != 0 else 10*(self.num//10) + 79*(self.num//10-1)
        self.y_2 = self.y + 79
        self.kub = None
        self.wrt_txt = None
        self.bg = 'white'

    def draw(self):
        self.kub = canvas.create_rectangle(self.x,self.y,self.x_2,self.y_2,outline=self.outline, width=2, fill=self.bg)
        self.wrt_txt = canvas.create_text(self.x+74, self.y+39,text=self.text)

    #def draw_kub(self):
    #    self.kub = canvas.create_rectangle(self.x,self.y,self.x_2,self.y_2,outline=self.outline, width=2)
    def go(self):
        colors = ['red', 'orange', 'green','yellow', 'blue','purple']
        self.outline = random.choice(colors)
        canvas.delete(self.kub)
        canvas.delete(self.wrt_txt)
        self.draw()
        window.update()
        time.sleep(10/len(kubs))
        self.outline = 'white'
        canvas.delete(self.kub)
        canvas.delete(self.wrt_txt)
        self.draw()
        window.update()

    def won(self):
        self.bg = 'green'
        canvas.delete(self.kub)
        canvas.delete(self.wrt_txt)
        self.draw()
        window.update()
        time.sleep(3)
        canvas.delete('all')
        canvas.create_text(800,450,text=f'Победил игрок с id {self.text}', font=('Arial', 25))

users = []
var_us = None
id_users = {}
id_int = 1
error_inpt = None

kubs = []
f_num = 0
file = open('win.txt', 'r')
win_text = int(file.readline())
file.close()
def reg():
    global  kubs, f_num
    for id in id_users:
        kubs.append(Restangeles(id_users[id], users[f_num]))
        f_num += 1
    id_kub = {}
    kub_num = 1
    for kub in kubs:
        id_kub[kub_num] = kub
        kub_num += 1
    for kub in kubs:
        kub.draw()

kol_krut = random.randint(2, 6)
xod = 1

def dogo():
    global bat_go,kol_krut,xod
    bat_go.destroy()
    while xod <= kol_krut:
        for kub in kubs:
            kub.go()
            if xod == kol_krut and int(kub.text) == win_text:
                kub.won()
                break
        xod += 1
inpt = Entry(background='white', textvariable='id')
inpt.pack(anchor=NW)
bat_go = None
def func_go():
    global  bat_go
    bat_go = Button(text="Запуск",command = dogo )
    bat_go.place(x=1540,y=890)

def inpt_req(event):
    global users,id_users,id_int,error_inpt
    if error_inpt != None:
        error_inpt.destroy()
    if inpt.get() != 'go':
        try:
            users.append(int(inpt.get()))
        except ValueError:
            inpt.delete(0,END)
            error_inpt = Label(text='Критическая ошибка :( Шучу, вводите id!!!')
            error_inpt.place(x=100, y=200)
        else:

            id_users[int(inpt.get())]=id_int

            id_int +=1
            print(users)
            print(id_users)
            inpt.delete(0, END)
    else:
        inpt.destroy()
        reg()
        func_go()
window.bind('<Return>',inpt_req)

canvas = Canvas(width=1600, height=900,bg = 'grey')
canvas.pack()

window.mainloop()