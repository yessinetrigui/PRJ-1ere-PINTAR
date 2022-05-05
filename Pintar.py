import turtle
import random
import tkinter
from tkinter import StringVar
from tkinter import Tk
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
from playsound import playsound
#import winsound
from turtle import Screen
import webbrowser
import tkinter as tk


def bu():
    webbrowser.open_new_tab('https://unosoft1.wordpress.com')

#winsound.MessageBeep()

X = 'By: UnoSoft'
window1 = Tk()
window1.resizable(0, 0)
window1.title('You Are Welcome')
fnt1 = 'Cookie-Regular 50'
fnt2 = 'Jokerman 40'
fnt3 = 'Ravie 15'

lab1=ttk.Label(window1, text='Pintar V1', font=fnt1, foreground='red')
lab2=ttk.Label(window1, text=X, font=fnt2, foreground='#800080')
lab4=ttk.Label(window1, text='Enjoy !', font=fnt3, foreground='green')
bu1=ttk.Button(window1, text='Call Us', command=bu)
svname01=StringVar()
cnbx= ttk.Combobox(values=('english','عربية'), state='readonly', textvariable=svname01, width=20, height=20)
svname01.set('choose an language')

def do():

    if cnbx.get() == 'english':
        window1.destroy()
        pen = turtle.Turtle()
        screen = Screen()
        style = ttk.Style()
        style.theme_use('clam')
        screen.title('Pintar V1')
        lebl = ttk.Label(text='Color Y. Choosed', width=20, padding=8, font=("arial", 7))
        y = '6'
        z = '1'
        svname = StringVar()
        svname5 = StringVar()
        pn = ttk.PanedWindow(width=0, height=105)
        pn.pack()
        bu1 = ttk.Button(text='Color Chooser  [Click To Choose Your Color]', padding=20)
        bu2 = ttk.Button(text='Exit', padding=3)
        bu3 = ttk.Button(text='Center', padding=3)
        bu4 = ttk.Button(text='Clear', padding=3)
        bu5 = ttk.Combobox(values=('classic', 'arrow', 'turtle', 'circle'), width=15, textvariable=svname5,
                           state='readonly')
        svname5.set('Choose Shape')
        bu6 = ttk.Button(text='▲', padding=y)
        bu7 = ttk.Button(text='▼', padding=y)
        bu8 = ttk.Button(text='▶', padding=y)
        bu9 = ttk.Button(text='◀', padding=y)
        bu10 = ttk.Button(text='Choose Your Pen Size')
        bu11 = ttk.Button(text='Pen Up', padding=z)
        bu12 = ttk.Button(text='Pen Down', padding=z)
        svname1 = StringVar()
        cnbx1 = ttk.Combobox(values=('fastest', 'fast', 'normal', 'slow', 'slowest'), state='readonly',
                             textvariable=svname1)
        svname1.set('Enter Your Pen Speed')
        bu13 = ttk.Button(text='OK')
        bu15 = ttk.Button(text='Bg Color', padding=z)
        bu16 = ttk.Button(text='Music', padding=z)
        svname4 = StringVar()
        bu17 = ttk.Button(text='Enter Your Text', padding=6)
        bu18 = ttk.Button(text='OK', padding=6)
        svname2 = StringVar()
        cnbx2 = ttk.Combobox(values=('Triangle', 'Circle', 'Object 1', 'Object 2', 'Object 3', 'Object 4', 'Dot'),
                             textvariable=svname2, state="readonly")
        svname2.set('Choose An Object')
        bu19 = ttk.Button(text='Ok')
        buu = ttk.Button(text='press to\nbegin fill', padding=0, width=8)
        buu1 = ttk.Button(text='prees to\nend fill', padding=0, width=8)
        bu20 = ttk.Button(text='Option')

        class full():
            def beginfull():
                pen.begin_fill()
                buu.config(text=' Button\npressed')
                buu1.config(text='prees to\nend fill')
                style.configure('bu11.TButton', background='Green')
                buu.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                buu1.configure(style='bu12.TButton')

            def endfull():
                pen.end_fill()
                buu1.config(text='Button\npressed')
                buu.config(text='press to\nbegin fill')
                style.configure('bu11.TButton', background='Green')
                buu1.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                buu.configure(style='bu12.TButton')

        buu.config(command=full.beginfull)
        buu1.config(command=full.endfull)

        class Music():

            def Musics():
                music1 = (
                'DataMusic/Music01.wav', 'DataMusic/Music02.wav', 'DataMusic/Music04.wav', 'DataMusic/Music05.wav')
                randmusic = (random.choice(music1))
                playsound(randmusic)
                return
        screen.setup(width=1030, height=700)

        class WidthS():

            def width():
                wdth = screen.textinput('Pintar', 'Choose Your Pen Width')
                pen.width(wdth)

        def bg():
            color = colorchooser.askcolor()
            screen.bgcolor(color[1])

        class Moves():

            def up():
                pen.setheading(90)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def down():
                pen.setheading(270)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def left():
                pen.setheading(180)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def right():
                pen.setheading(0)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()
        class Colors():
            def color():
                color = colorchooser.askcolor()
                pen.color(color[1])
                lebl.config(background=color[1])
                lebl.config(text=color[1], font=("arial", 10), width=9, foreground='white')
                lebl.place(x=82, y=632)

        class More():
            def centre():
                pen.penup()
                pen.goto(0, 0)
                pen.pendown()

            def delete():
                pen.clear()

        svname3 = StringVar()

        class Objects():

            def do():
                if cnbx2.get() == 'Circle':
                    x = screen.textinput('Pintar V0.2', 'choose rayon of circle')
                    pen.circle(int(x))



                elif cnbx2.get() == 'Triangle':
                    pen.setheading(40)
                    pen.forward(50)
                    pen.left(-90)
                    pen.forward(50)
                    pen.left(-130)
                    pen.forward(80)


                elif cnbx2.get() == 'Object 1':
                    for i in range(12):
                        pen.forward(200)
                        pen.left(150)

                elif cnbx2.get() == 'Object 2':
                    for i in range(10):
                        pen.forward(200)
                        pen.left(135)

                elif cnbx2.get() == 'Object 3':
                    for i in range(4):
                        pen.forward(200)
                        pen.right(270)

                elif cnbx2.get() =='Object 4':
                    for i in range(50):
                        pen.forward(200)
                        pen.left(70)

                elif cnbx2.get() == 'Dot':
                    dt = screen.textinput('Pintar', 'Enter Your Dot width')
                    pen.dot(int(dt))
                else:
                    messagebox.showerror('Pintar', 'Please Choose an Object')
        class Text():

            def text():
                x001 = screen.textinput('Pintar','Enter your text')
                pen.write(x001)

        class Speeds():

            def speed():
                if cnbx1.get() == 'fastest':
                    pen.speed('fastest')
                elif cnbx1.get() == 'fast':
                    pen.speed('fast')
                elif cnbx1.get() == 'normal':
                    pen.speed('normal')
                elif cnbx1.get() == 'slow':
                    pen.speed('slow')
                elif cnbx1.get() == 'slowest':
                    pen.shape('slowest')
                else:
                    messagebox.showerror('Pintar','choose pen speed')
        class Randcolor():

            def randcolor():
                colors = (
                'red', 'blue', 'purple', 'yellow', 'green', '#FF4000', '#D7DF01', '#A5DF00', '#3ADF00', '#00FFFF',
                '#8000FF',
                '#FF00FF', '#FF0080')
                randcolors = (random.randrange(0, len(colors)))
                pen.color(colors[randcolors])

        class Pen():

            def up():
                style.configure('bu11.TButton', background='Green')
                bu11.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                bu12.configure(style='bu12.TButton')
                pen.penup()

            def down():
                style.configure('bu12.TButton', background='Green')
                bu12.configure(style='bu12.TButton')
                style.configure('bu11.TButton', background='Red')
                bu11.configure(style='bu11.TButton')
                pen.pendown()

        def soundStop():
            playsound("DataMusic/stop.wav")

        def quitter():
            if messagebox.askyesno('Pintar', 'Are You Sure To Exit') == True:
                screen.bye()

        def shapes():
            if bu5.get() == 'classic':
                pen.shape('classic')
            elif bu5.get() == 'turtle':
                pen.shape('turtle')
            elif bu5.get() == 'arrow':
                pen.shape('arrow')
            elif bu5.get() == 'circle':
                pen.shape('circle')
            else:
                messagebox.showerror('Pintar', 'choose a shape')
        class OPTION():
            def option():
                windowOP = Tk()

                fnt10 = 'Cookie-Regular 12'
                fnt2 = 'GIGI 10'
                windowOP.title('Option')
                windowOP.geometry('400x250')
                windowOP.resizable(0, 0)
                lbx=tk.Listbox(windowOP)
                lbx.insert(0, 'Options')
                lbx.insert(1, 'About')
                lab01 = ttk.Label(windowOP, text='Created By High Level Soft', foreground='red',font=fnt10)
                lab02 = ttk.Label(windowOP, text='Codding By: Yessine Trigui', foreground='red',font=fnt10)

                lab1 = ttk.Label(windowOP, text='Distance')
                ent1 = ttk.Entry(windowOP)
                def do():
                    f1 = open('DataBase/dataop.txt', 'w')
                    f1.write(ent1.get())
                    f1.close()
                    ent1.delete(0, END)
                    windowOP.destroy()
                    messagebox.showinfo('Pintar','Distance Changed')

                bu001 = ttk.Button(windowOP, text='Done',command=do)

                lab1.place(x=170, y=50)
                ent1.place(x=135, y=75)
                bu001.place(x=160, y=100)
                lab01.place(x=110, y=190)

        bu1.configure(command=Colors.color)
        bu2.configure(command=quitter)
        bu3.configure(command=More.centre)
        bu4.configure(command=More.delete)
        bu18.configure(command=shapes)
        bu6.configure(command=Moves.up)
        bu7.configure(command=Moves.down)
        bu8.configure(command=Moves.right)
        bu9.configure(command=Moves.left)
        bu10.configure(command=WidthS.width)
        bu11.configure(command=Pen.up)
        bu12.configure(command=Pen.down)
        bu13.configure(command=Speeds.speed)
        bu15.configure(command=bg)
        bu16.configure(command=Music.Musics)
        bu17.configure(command=Text.text)
        bu19.config(command=Objects.do)
        bu20.config(command=OPTION.option)
        bu1.place(x=745, y=630)
        bu2.place(x=945, y=600)
        bu3.place(x=866, y=600)
        bu4.place(x=787, y=600)
        bu5.place(x=265, y=635)
        bu6.place(x=82, y=600)
        lebl.place(x=77, y=632)
        bu7.place(x=82, y=662)
        bu8.place(x=164, y=631)
        bu9.place(x=0, y=631)
        bu10.place(x=255, y=600)
        bu11.place(x=5, y=605)
        bu12.place(x=169, y=605)
        cnbx1.place(x=420, y=635)
        bu13.place(x=450, y=662)
        bu15.place(x=5, y=667)
        bu16.place(x=170, y=667)
        bu17.place(x=605, y=600)
        bu18.place(x=278, y=662)
        butest = ttk.Button(text='Stop Music', command=soundStop, padding=3).place(x=708, y=600)
        bu16.configure(padding=1)
        buu.place(x=385, y=660)
        buu1.place(x=545, y=660)
        cnbx2.place(x=600, y=635)
        bu19.place(x=630, y=660)

        bu20.place(x=450, y=600)

        def dragging(x, y):
            pen.ondrag(None)
            pen.setheading(pen.towards(x, y))
            pen.goto(x, y)
            pen.ondrag(dragging)

        def main():
            screen.listen()
            pen.ondrag(dragging)

        main()

        turtle.done()
    elif cnbx.get() == 'French':
        window1.destroy()
        pen = turtle.Turtle()
        screen = Screen()
        style = ttk.Style()
        style.theme_use('clam')
        screen.title('Pintar V0.3')
        lebl = ttk.Label(text='Color Y. Choosed', width=20, padding=8, font=("arial", 7))
        y = '6'
        z = '1'
        svname = StringVar()
        svname5 = StringVar()
        pn = ttk.PanedWindow(width=0, height=105)
        pn.pack()
        bu1 = ttk.Button(text='Color Chooser  [Click To Choose Your Color]', padding=20)
        bu2 = ttk.Button(text='Exit', padding=3)
        bu3 = ttk.Button(text='Center', padding=3)
        bu4 = ttk.Button(text='Clear', padding=3)
        bu5 = ttk.Combobox(values=('classic', 'arrow', 'turtle', 'circle'), width=15, textvariable=svname5,
                           state='readonly')
        svname5.set('Choose Shape')
        bu6 = ttk.Button(text='▲', padding=y)
        bu7 = ttk.Button(text='▼', padding=y)
        bu8 = ttk.Button(text='▶', padding=y)
        bu9 = ttk.Button(text='◀', padding=y)
        bu10 = ttk.Button(text='Choose Your Pen Size')
        bu11 = ttk.Button(text='Pen Up', padding=z)
        bu12 = ttk.Button(text='Pen Down', padding=z)
        svname1 = StringVar()
        cnbx1 = ttk.Combobox(values=('fastest', 'fast', 'normal', 'slow', 'slowest'), state='readonly',
                             textvariable=svname1)
        svname1.set('Enter Your Pen Speed')
        bu13 = ttk.Button(text='OK')
        bu15 = ttk.Button(text='Bg Color', padding=z)
        bu16 = ttk.Button(text='Music', padding=z)
        svname4 = StringVar()
        bu17 = ttk.Button(text='Enter Your Text', padding=6)
        bu18 = ttk.Button(text='OK', padding=6)
        svname2 = StringVar()
        cnbx2 = ttk.Combobox(values=('Triangle', 'Circle', 'Object 1', 'Object 2', 'Object 3', 'Object 4', 'Dot'),
                             textvariable=svname2, state="readonly")
        svname2.set('Choose An Object')
        bu19 = ttk.Button(text='Ok')
        buu = ttk.Button(text='press to\nbegin fill', padding=0, width=8)
        buu1 = ttk.Button(text='prees to\nend fill', padding=0, width=8)
        bu20 = ttk.Button(text='Option')

        class full():
            def beginfull():
                pen.begin_fill()
                buu.config(text=' Button\npressed')
                buu1.config(text='prees to\nend fill')
                style.configure('bu11.TButton', background='Green')
                buu.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                buu1.configure(style='bu12.TButton')

            def endfull():
                pen.end_fill()
                buu1.config(text='Button\npressed')
                buu.config(text='press to\nbegin fill')
                style.configure('bu11.TButton', background='Green')
                buu1.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                buu.configure(style='bu12.TButton')

        buu.config(command=full.beginfull)
        buu1.config(command=full.endfull)

        class Music():

            def Musics():
                music1 = (
                'DataMusic/Music01.wav', 'DataMusic/Music02.wav', 'DataMusic/Music04.wav', 'DataMusic/Music05.wav')
                randmusic = (random.choice(music1))
                winsound.PlaySound(randmusic, winsound.SND_ASYNC)

        screen.setup(width=1030, height=700)

        class WidthS():

            def width():
                wdth = screen.textinput('Pintar', 'Choose Your Pen Width')
                pen.width(wdth)

        def bg():
            color = colorchooser.askcolor()
            screen.bgcolor(color[1])

        class Moves():

            def up():
                pen.setheading(90)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def down():
                pen.setheading(270)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def left():
                pen.setheading(180)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def right():
                pen.setheading(0)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()
        class Colors():
            def color():
                color = colorchooser.askcolor()
                pen.color(color[1])
                lebl.config(background=color[1])
                lebl.config(text=color[1], font=("arial", 10), width=9, foreground='white')
                lebl.place(x=82, y=632)

        class More():
            def centre():
                pen.penup()
                pen.goto(0, 0)
                pen.pendown()

            def delete():
                pen.clear()

        svname3 = StringVar()

        class Objects():

            def do():
                if cnbx2.get() == 'Circle':
                    x = screen.textinput('Pintar V0.2', 'choose rayon of circle')
                    pen.circle(int(x))



                elif cnbx2.get() == 'Triangle':
                    pen.setheading(40)
                    pen.forward(50)
                    pen.left(-90)
                    pen.forward(50)
                    pen.left(-130)
                    pen.forward(80)


                elif cnbx2.get() == 'Object 1':
                    for i in range(12):
                        pen.forward(200)
                        pen.left(150)

                elif cnbx2.get() == 'Object 2':
                    for i in range(10):
                        pen.forward(200)
                        pen.left(135)

                elif cnbx2.get() == 'Object 3':
                    for i in range(4):
                        pen.forward(200)
                        pen.right(270)

                elif cnbx2.get() =='Object 4':
                    for i in range(50):
                        pen.forward(200)
                        pen.left(70)

                elif cnbx2.get() == 'Dot':
                    dt = screen.textinput('Pintar', 'Enter Your Dot width')
                    pen.dot(int(dt))
                else:
                    messagebox.showerror('Pintar', 'Please Choose an Object')
        class Text():

            def text():
                x001 = screen.textinput('Pintar','Enter your text')
                pen.write(x001)

        class Speeds():

            def speed():
                if cnbx1.get() == 'fastest':
                    pen.speed('fastest')
                elif cnbx1.get() == 'fast':
                    pen.speed('fast')
                elif cnbx1.get() == 'normal':
                    pen.speed('normal')
                elif cnbx1.get() == 'slow':
                    pen.speed('slow')
                elif cnbx1.get() == 'slowest':
                    pen.shape('slowest')
                else:
                    messagebox.showerror('Pintar','choose pen speed')
        class Randcolor():

            def randcolor():
                colors = (
                'red', 'blue', 'purple', 'yellow', 'green', '#FF4000', '#D7DF01', '#A5DF00', '#3ADF00', '#00FFFF',
                '#8000FF',
                '#FF00FF', '#FF0080')
                randcolors = (random.randrange(0, len(colors)))
                pen.color(colors[randcolors])

        class Pen():

            def up():
                style.configure('bu11.TButton', background='Green')
                bu11.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                bu12.configure(style='bu12.TButton')
                pen.penup()

            def down():
                style.configure('bu12.TButton', background='Green')
                bu12.configure(style='bu12.TButton')
                style.configure('bu11.TButton', background='Red')
                bu11.configure(style='bu11.TButton')
                pen.pendown()

        def soundStop():
            winsound.PlaySound("DataMusic/stop.wav", winsound.SND_ASYNC)

        def quitter():
            if messagebox.askyesno('Pintar', 'Are You Sure To Exit') == True:
                screen.bye()

        def shapes():
            if bu5.get() == 'classic':
                pen.shape('classic')
            elif bu5.get() == 'turtle':
                pen.shape('turtle')
            elif bu5.get() == 'arrow':
                pen.shape('arrow')
            elif bu5.get() == 'circle':
                pen.shape('circle')
            else:
                messagebox.showerror('Pintar', 'choose a shape')
        class OPTION():
            def option():
                windowOP = Tk()
                fnt10 = 'Cookie-Regular 20'
                fnt2 = 'GIGI 10'
                windowOP.title('Option')
                windowOP.geometry('400x250')
                windowOP.resizable(0, 0)
                lbx=Listbox(windowOP)
                lbx.insert(0, 'Options')
                lbx.insert(1, 'About')
                lab01 = ttk.Label(windowOP, text='Made In Tunisia', foreground='red',font=fnt10)
                lab02 = ttk.Label(windowOP, text='Codding By: Yessine Trigui', foreground='red',font=fnt10)

                lab1 = ttk.Label(windowOP, text='Distance')
                ent1 = ttk.Entry(windowOP)
                def do():
                    f1 = open('DataBase/dataop.txt', 'w')
                    f1.write(ent1.get())
                    f1.close()
                    ent1.delete(0, END)
                    windowOP.destroy()
                    messagebox.showinfo('Pintar','Distance Changed')

                bu001 = ttk.Button(windowOP, text='Done',command=do)

                lab1.place(x=170, y=50)
                ent1.place(x=135, y=75)
                bu001.place(x=160, y=100)
                lab02.place(x=70, y=215)
                lab01.place(x=110, y=190)

        bu1.configure(command=Colors.color)
        bu2.configure(command=quitter)
        bu3.configure(command=More.centre)
        bu4.configure(command=More.delete)
        bu18.configure(command=shapes)
        bu6.configure(command=Moves.up)
        bu7.configure(command=Moves.down)
        bu8.configure(command=Moves.right)
        bu9.configure(command=Moves.left)
        bu10.configure(command=WidthS.width)
        bu11.configure(command=Pen.up)
        bu12.configure(command=Pen.down)
        bu13.configure(command=Speeds.speed)
        bu15.configure(command=bg)
        bu16.configure(command=Music.Musics)
        bu17.configure(command=Text.text)
        bu19.config(command=Objects.do)
        bu20.config(command=OPTION.option)
        bu1.place(x=745, y=630)
        bu2.place(x=945, y=600)
        bu3.place(x=866, y=600)
        bu4.place(x=787, y=600)
        bu5.place(x=265, y=635)
        bu6.place(x=82, y=600)
        lebl.place(x=77, y=632)
        bu7.place(x=82, y=662)
        bu8.place(x=164, y=631)
        bu9.place(x=0, y=631)
        bu10.place(x=255, y=600)
        bu11.place(x=5, y=605)
        bu12.place(x=169, y=605)
        cnbx1.place(x=420, y=635)
        bu13.place(x=450, y=662)
        bu15.place(x=5, y=667)
        bu16.place(x=170, y=667)
        bu17.place(x=605, y=600)
        bu18.place(x=278, y=662)
        butest = ttk.Button(text='Stop Music', command=soundStop, padding=3).place(x=708, y=600)
        bu16.configure(padding=1)
        buu.place(x=385, y=660)
        buu1.place(x=545, y=660)
        cnbx2.place(x=600, y=635)
        bu19.place(x=630, y=660)

        bu20.place(x=450, y=600)

        def dragging(x, y):
            pen.ondrag(None)
            pen.setheading(pen.towards(x, y))
            pen.goto(x, y)
            pen.ondrag(dragging)

        def main():
            screen.listen()
            pen.ondrag(dragging)

        main()

        turtle.done()

    elif cnbx.get() =='عربية':
        window1.destroy()
        pen = turtle.Turtle()
        screen = Screen()
        style = ttk.Style()
        style.theme_use('clam')
        screen.title('بينتار V1')
        lebl = ttk.Label(text='االون الذي اخترته', width=20, padding=8, font=("arial", 7))
        y = '6'
        z = '1'
        svname = StringVar()
        svname5 = StringVar()
        pn = ttk.PanedWindow(width=0, height=105)
        pn.pack()
        bu1 = ttk.Button(text='اضغط لاختيار لون الخط                                           ', padding=20)
        bu2 = ttk.Button(text='خروج', padding=3)
        bu3 = ttk.Button(text='وسط', padding=3)
        bu4 = ttk.Button(text='احذف', padding=3)
        bu5 = ttk.Combobox(values=('كلاسيكي', 'سهم', 'سلحفات', 'دائرة'), width=15, textvariable=svname5,
                           state='readonly')
        svname5.set('اختر شكل')
        bu6 = ttk.Button(text='▲', padding=y)
        bu7 = ttk.Button(text='▼', padding=y)
        bu8 = ttk.Button(text='▶', padding=y)
        bu9 = ttk.Button(text='◀', padding=y)
        bu10 = ttk.Button(text='اضغط لادخال حجم الخط')
        bu11 = ttk.Button(text='ارفع القلم', padding=z)
        bu12 = ttk.Button(text='انزل القلم', padding=z)
        svname1 = StringVar()
        cnbx1 = ttk.Combobox(values=('أكثر سرعة', 'سريع', 'عادي', 'بطيء', 'اكثر بطء'), state='readonly',
                             textvariable=svname1)
        svname1.set('اضغط لاختيار سرعة الرسم')
        bu13 = ttk.Button(text='موافق')
        bu15 = ttk.Button(text='لون الخلفية', padding=z)
        bu16 = ttk.Button(text='موسيقى', padding=z)
        svname4 = StringVar()
        bu17 = ttk.Button(text='اضغط لادخال نص', padding=6)
        bu18 = ttk.Button(text='موافق', padding=6)
        svname2 = StringVar()
        cnbx2 = ttk.Combobox(values=('مثلث', 'دائرة', 'شكل 1', 'شكل 2', 'شكل 3', 'شكل 4', 'نقطة'),
                             textvariable=svname2, state="readonly")
        svname2.set('اختر شكل ارسمه')
        bu19 = ttk.Button(text='موافق')
        buu = ttk.Button(text='لبدء التلوين\nاضغط', padding=0, width=8)
        buu1 = ttk.Button(text='انهاء التلوين\nاضغط', padding=0, width=8)
        bu20 = ttk.Button(text='اعدادات')

        class full():
            def beginfull():
                pen.begin_fill()
                buu.config(text='الزر\nمضغوط')
                buu1.config(text='اضغط لانهاءالتلوين')
                style.configure('bu11.TButton', background='Green')
                buu.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                buu1.configure(style='bu12.TButton')

            def endfull():
                pen.end_fill()
                buu1.config(text='الزر\nمضغوط')
                buu.config(text='اضغط لبدءالتلوين')
                style.configure('bu11.TButton', background='Green')
                buu1.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                buu.configure(style='bu12.TButton')

        buu.config(command=full.beginfull)
        buu1.config(command=full.endfull)

        class Music():

            def Musics():
                music1 = (
                'DataMusic/Music01.wav', 'DataMusic/Music02.wav', 'DataMusic/Music04.wav', 'DataMusic/Music05.wav')
                randmusic = (random.choice(music1))
                winsound.PlaySound(randmusic, winsound.SND_ASYNC)

        screen.setup(width=1030, height=700)

        class WidthS():

            def width():
                wdth = screen.textinput('بينتار', 'اختر حجم الخط')
                pen.width(wdth)

        def bg():
            color = colorchooser.askcolor()
            screen.bgcolor(color[1])

        class Moves():

            def up():
                pen.setheading(90)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def down():
                pen.setheading(270)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def left():
                pen.setheading(180)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()

            def right():
                pen.setheading(0)
                f2 = open('DataBase/dataop.txt', 'r')
                dis1 =f2.read()
                pen.forward(int(dis1))
                f2.close()
        class Colors():
            def color():
                color = colorchooser.askcolor()
                pen.color(color[1])
                lebl.config(background=color[1])
                lebl.config(text=color[1], font=("arial", 10), width=9, foreground='white')
                lebl.place(x=82, y=632)

        class More():
            def centre():
                pen.penup()
                pen.goto(0, 0)
                pen.pendown()

            def delete():
                pen.clear()

        svname3 = StringVar()

        class Objects():

            def do():
                if cnbx2.get() == 'دائرة':
                    x = screen.textinput('بينتار', 'ادخل شعاع الدائرة')
                    pen.circle(int(x))



                elif cnbx2.get() == 'مثلث':
                    pen.setheading(40)
                    pen.forward(50)
                    pen.left(-90)
                    pen.forward(50)
                    pen.left(-130)
                    pen.forward(80)


                elif cnbx2.get() == 'شكل 1':
                    for i in range(12):
                        pen.forward(200)
                        pen.left(150)

                elif cnbx2.get() == 'شكل 2':
                    for i in range(10):
                        pen.forward(200)
                        pen.left(135)

                elif cnbx2.get() == 'شكل 3':
                    for i in range(4):
                        pen.forward(200)
                        pen.right(270)

                elif cnbx2.get() =='شكل 4':
                    for i in range(50):
                        pen.forward(200)
                        pen.left(70)

                elif cnbx2.get() == 'نقطة':
                    dt = screen.textinput('بينتار', 'اختر حجم القلم')
                    pen.dot(int(dt))
                else:
                    messagebox.showerror('بينتار', 'ارجوك اختر شكل')
        class Text():

            def text():
                x001 = screen.textinput('بينتار', 'ادخل النص')
                pen.write(x001)

        class Speeds():

            def speed():
                if cnbx1.get() == 'أكثر سرعة':
                    pen.speed('fastest')
                elif cnbx1.get() == 'سريع':
                    pen.speed('fast')
                elif cnbx1.get() == 'عادي':
                    pen.speed('normal')
                elif cnbx1.get() == 'بطيء':
                    pen.speed('slow')
                elif cnbx1.get() == 'اكثر بطء':
                    pen.shape('slowest')
                else:
                    messagebox.showerror('بينتار','اختر سرعة الرسم')

        class Randcolor():

            def randcolor():
                colors = (
                'red', 'blue', 'purple', 'yellow', 'green', '#FF4000', '#D7DF01', '#A5DF00', '#3ADF00', '#00FFFF',
                '#8000FF',
                '#FF00FF', '#FF0080')
                randcolors = (random.randrange(0, len(colors)))
                pen.color(colors[randcolors])

        class Pen():

            def up():
                style.configure('bu11.TButton', background='Green')
                bu11.configure(style='bu11.TButton')
                style.configure('bu12.TButton', background='Red')
                bu12.configure(style='bu12.TButton')
                pen.penup()

            def down():
                style.configure('bu12.TButton', background='Green')
                bu12.configure(style='bu12.TButton')
                style.configure('bu11.TButton', background='Red')
                bu11.configure(style='bu11.TButton')
                pen.pendown()

        def soundStop():
            winsound.PlaySound("DataMusic/stop.wav", winsound.SND_ASYNC)

        def quitter():
            if messagebox.askyesno('بينتار', 'هل انت متأكد من الخروج') == True:
                screen.bye()

        def shapes():
            if bu5.get() == 'كلاسيكي':
                pen.shape('classic')
            elif bu5.get() == 'سلحفات':
                pen.shape('turtle')
            elif bu5.get() == 'سهم':
                pen.shape('arrow')
            elif bu5.get() == 'دائرة':
                pen.shape('circle')
            else:
                messagebox.showerror('بينتار', 'اختر شكل')

        class OPTION():
            def option():
                windowOP = Tk()
                fnt10 = 'Cookie-Regular 20'
                fnt2 = 'GIGI 10'
                windowOP.title('اعدادات')
                windowOP.geometry('400x250')
                windowOP.resizable(0, 0)
                lbx=Listbox(windowOP)
                lbx.insert(0, 'Options')
                lbx.insert(1, 'About')
                lab01 = ttk.Label(windowOP, text='Created By High Level Soft', foreground='red',font=fnt10)
                lab02 = ttk.Label(windowOP, text='Yessine Trigui  :بواسطة البرمجة ', foreground='red',font=fnt10)

                lab1 = ttk.Label(windowOP, text='مسافة رسم خط')
                ent1 = ttk.Entry(windowOP)
                def do():
                    f1 = open('DataBase/dataop.txt', 'w')
                    f1.write(ent1.get())
                    f1.close()
                    ent1.delete(0, END)
                    windowOP.destroy()
                    messagebox.showinfo('بينتار', 'تم تغير المسافة')

                bu001 = ttk.Button(windowOP, text='حسنا',command=do)

                lab1.place(x=170, y=50)
                ent1.place(x=135, y=75)
                bu001.place(x=160, y=100)
                lab01.place(x=110, y=190)

        bu1.configure(command=Colors.color)
        bu2.configure(command=quitter)
        bu3.configure(command=More.centre)
        bu4.configure(command=More.delete)
        bu18.configure(command=shapes)
        bu6.configure(command=Moves.up)
        bu7.configure(command=Moves.down)
        bu8.configure(command=Moves.right)
        bu9.configure(command=Moves.left)
        bu10.configure(command=WidthS.width)
        bu11.configure(command=Pen.up)
        bu12.configure(command=Pen.down)
        bu13.configure(command=Speeds.speed)
        bu15.configure(command=bg)
        bu16.configure(command=Music.Musics)
        bu17.configure(command=Text.text)
        bu19.config(command=Objects.do)
        bu20.config(command=OPTION.option)
        bu1.place(x=745, y=630)
        bu2.place(x=945, y=600)
        bu3.place(x=866, y=600)
        bu4.place(x=787, y=600)
        bu5.place(x=265, y=635)
        bu6.place(x=82, y=600)
        lebl.place(x=77, y=632)
        bu7.place(x=82, y=662)
        bu8.place(x=164, y=631)
        bu9.place(x=0, y=631)
        bu10.place(x=255, y=600)
        bu11.place(x=5, y=605)
        bu12.place(x=169, y=605)
        cnbx1.place(x=420, y=635)
        bu13.place(x=450, y=662)
        bu15.place(x=5, y=667)
        bu16.place(x=170, y=667)
        bu17.place(x=605, y=600)
        bu18.place(x=278, y=662)
        butest = ttk.Button(text='ايقاف الموسيقى', command=soundStop, padding=3).place(x=708, y=600)
        bu16.configure(padding=1)
        buu.place(x=385, y=660)
        buu1.place(x=545, y=660)
        cnbx2.place(x=600, y=635)
        bu19.place(x=630, y=660)

        bu20.place(x=450, y=600)

        def dragging(x, y):
            pen.ondrag(None)
            pen.setheading(pen.towards(x, y))
            pen.goto(x, y)
            pen.ondrag(dragging)

        def main():
            screen.listen()
            pen.ondrag(dragging)

        main()

        turtle.done()


    else:
        messagebox.showerror('Pintar', 'Choose a language ✘')



lab1.pack()
lab2.pack()

cnbx.pack()
bu2=ttk.Button(window1, text='Ok', command=do, padding=20).pack()
bu1.pack()
lab4.pack()
window1.mainloop()
