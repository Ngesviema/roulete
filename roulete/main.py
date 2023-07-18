from tkinter import *
import random
import time
users = []
var_us = None
id_users = {}
id_int = 1
while True:
    var_us = input('Введите id игрока: ')
    if var_us != 'go':
        try:
          users.append(int(var_us))
        except ValueError:
            print('Критическая ошибка :( Шучу, вводите id!!!')
        else:
            id_users[int(var_us)]=id_int
            id_int +=1
    else:
        break


window = Tk()
window.geometry('1600x900')
window.resizable(width=False, height=False)
window.title('Рулетка')
canvas = Canvas(width=1600, height=900)
canvas.pack()
class Restangeles:
    def __init__(self, num, text):
        self.num = num
        self.outline = 'black'
        self.text = text
        self.x = 10*(self.num%10) + 149*((self.num-1)%10) if self.num % 10 != 0 else 10*10 + 149*9
        self.x_2 = self.x + 149
        self.y = 10*(self.num//10+1)+79*(self.num//10) if self.num % 10 != 0 else 10*(self.num//10) + 79*(self.num//10-1)
        self.y_2 = self.y + 79
        self.kub = None
        self.wrt_txt = None
        self.bg = 'white'

    def draw(self):
        self.kub = canvas.create_rectangle(self.x,self.y,self.x_2,self.y_2,outline=self.outline, width=2, fill = self.bg)
        self.wrt_txt = canvas.create_text(self.x+74, self.y+39,text=self.text)

    def draw_kub(self):
        self.kub = canvas.create_rectangle(self.x,self.y,self.x_2,self.y_2,outline=self.outline, width=2)
    def go(self):
        colors = ['red', 'orange', 'green','yellow', 'blue','purple']
        self.outline = random.choice(colors)
        canvas.delete(self.kub)
        self.draw_kub()
        window.update()
        time.sleep(1)
        self.outline = 'black'
        canvas.delete(self.kub)
        self.draw_kub()
        window.update()

    def won(self):
        self.bg = 'yellow'
        canvas.delete(self.kub)
        canvas.delete(self.wrt_txt)
        self.draw()
        window.update()
        time.sleep(3)
        canvas.delete('all')
        canvas.create_text(800,450,text=f'Победил игрок с id {self.text}', font=('Arial', 25))

kubs = []
f_num = 0
for id in id_users:
    kubs.append(Restangeles(id_users[id],users[f_num]))
    f_num +=1
id_kub = {}
kub_num = 1
for kub in kubs:
    id_kub[kub_num] = kub
    kub_num +=1

file = open('win.txt', 'r')
win_text = int(file.readline())
for kub in kubs:
    kub.draw()
kol_krut = random.randint(1,5)
xod = 1
while xod <= kol_krut:
    for kub in kubs:
        kub.go()
        if xod==kol_krut and int(kub.text) == win_text:
            kub.won()
            break
    xod +=1
window.mainloop()

