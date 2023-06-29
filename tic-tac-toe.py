from tkinter import *

class Duz():
    def __init__(self, w: Tk) -> None:
        self.conter = 0
        self.w = w
        self.w.title('duz')

        self.state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        self.b1 = Button(self.w, text= self.state[0][0], bg= 'lightgray', width= 6, height= 3, command= self.but1)
        self.b1.place(x = 10, y = 10)
        self.b2 = Button(self.w, text= self.state[0][1], bg= 'lightgray', width= 6, height= 3, command=self.but2)
        self.b2.place(x = 70, y = 10)
        self.b3 = Button(self.w, text= self.state[0][2], bg= 'lightgray', width= 6, height= 3, command= self.but3)
        self.b3.place(x = 130, y = 10)

        self.b4 = Button(self.w, text= self.state[1][0], bg= 'lightgray', width= 6, height= 3, command= self.but4)
        self.b4.place(x = 10, y = 70)
        self.b5 = Button(self.w, text= self.state[1][1], bg= 'lightgray', width= 6, height= 3, command= self.but5)
        self.b5.place(x = 70, y = 70)
        self.b6 = Button(self.w, text= self.state[1][2], bg= 'lightgray', width= 6, height= 3, command= self.but6)
        self.b6.place(x = 130, y = 70)

        self.b7 = Button(self.w, text= self.state[2][0], bg= 'lightgray', width= 6, height= 3, command= self.but7)
        self.b7.place(x = 10, y = 130)
        self.b8 = Button(self.w, text= self.state[2][1], bg= 'lightgray', width= 6, height= 3, command= self.but8)
        self.b8.place(x = 70, y = 130)
        self.b9 = Button(self.w, text= self.state[2][2], bg= 'lightgray', width= 6, height= 3, command= self.but9)
        self.b9.place(x = 130, y = 130)
        
        self.recognizer = 0
    
    def iswin(self):
        sym = ''
        ll = list(zip(*self.state))
        x = [self.state[0][0] , self.state[1][1], self.state[2][2]]
        xx = [self.state[0][2] , self.state[1][1], self.state[2][0]]
        
        if len(set(self.state[0])) == 1 and ' ' not in self.state[0]:
            sym = self.state[0][0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            self.show_result(sym)
        
        elif len(set(self.state[1])) == 1 and ' ' not in self.state[1]:
            sym = self.state[1][0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            self.show_result(sym)
        
        elif len(set(self.state[2])) == 1 and ' ' not in self.state[2]:
            sym = self.state[2][0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            self.show_result(sym)
        
        elif len(set(ll[0])) == 1 and ' ' not in ll[0]:
            sym = ll[0][0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            self.show_result(sym)
        elif len(set(ll[1])) == 1 and ' ' not in ll[1]:
            sym = ll[1][0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            return sym
        
        elif len(set(ll[2])) == 1 and ' ' not in ll[2]:
            sym = ll[2][0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            self.show_result(sym) 

        elif len(set(x)) == 1 and ' ' not in x:
            sym = x[0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            self.show_result(sym)

        elif len(set(xx)) == 1 and ' ' not in xx:
            sym = xx[0]
            self.b1.config(state= 'disabled')
            self.b2.config(state= 'disabled')
            self.b3.config(state= 'disabled')
            self.b4.config(state= 'disabled')
            self.b5.config(state= 'disabled')
            self.b6.config(state= 'disabled')
            self.b7.config(state= 'disabled')
            self.b8.config(state= 'disabled')
            self.b9.config(state= 'disabled')
            self.show_result(sym)

        elif ' ' not in [j for i in self.state for j in i]:
            self.show_result(' ')

    def but1(self):
        self.state[0][0] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[0][0] == '◯':
            self.b1.config( text= self.state[0][0], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b1.config(text= self.state[0][0], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b1.place(x = 10, y = 10)
        self.conter += 1
        self.iswin()

    def but2(self):
        self.state[0][1] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[0][1] == '◯':
            self.b2.config(text= self.state[0][1], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b2.config(text= self.state[0][1], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b2.place(x = 70, y = 10)
        self.conter += 1
        self.iswin()

    def but3(self):
        self.state[0][2] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[0][2] == '◯':
            self.b3.config(text= self.state[0][2], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b3.config(text= self.state[0][2], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b3.place(x = 130, y = 10)
        self.conter += 1
        self.iswin()

    def but4(self):
        self.state[1][0] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[1][0] == '◯':
            self.b4.config(text= self.state[1][0], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b4.config(text= self.state[1][0], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b4.place(x = 10, y = 70)
        self.conter += 1
        self.iswin()

    def but5(self):
        self.state[1][1] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[1][1] == '◯':
            print('---')
            self.b5.config(text= self.state[1][1], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b5.config(text= self.state[1][1], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b5.place(x = 70, y = 70)
        self.conter += 1
        self.iswin()

    def but6(self):
        self.state[1][2] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[1][2] == '◯':
            self.b6.config(text= self.state[1][2], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b6.config(text= self.state[1][2], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b6.place(x = 130, y = 70)
        self.conter += 1
        self.iswin()

    def but7(self):
        self.state[2][0] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[2][0] == '◯':
            self.b7.config(text= self.state[2][0], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b7.config(text= self.state[2][0], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b7.place(x = 10, y = 130)
        self.conter += 1
        self.iswin()

    def but8(self):
        self.state[2][1] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[2][1] == '◯':
            self.b8.config(text= self.state[2][1], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b8.config(text= self.state[2][1], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b8.place(x = 70, y = 130)
        self.conter += 1
        self.iswin()

    def but9(self):
        self.state[2][2] = '◯' if self.conter % 2 == 0 else 'X'
        if self.state[2][2] == '◯':
            self.b9.config(text= self.state[2][2], bg= 'lightgreen', width= 6, height= 3, state= 'disabled')
        else:
            self.b9.config(text= self.state[2][2], bg= 'pink', width= 6, height= 3, state= 'disabled')
        self.b9.place(x = 130, y = 130)
        self.conter += 1
        self.iswin()

    def show_result(self, sym):
        self.ww = Tk()
        self.ww.title('result')
        if sym == ' ':
            Label(self.ww, text= '  no one can not win!!  ').pack()
        elif sym == 'X':
            Label(self.ww, text= '  the player 2 win that the symbol was using is X!!  ').pack()
        else:
            Label(self.ww, text= '  the player 1 win that the symbol was using is ◯!!  ').pack()
        Button(self.ww, text= 'ok', bg= 'green', fg= 'white', command= self.exit).pack()
    
    def exit(self):
        self.ww.destroy()
        self.w.destroy()

w = Tk()
Duz(w)
w.mainloop()