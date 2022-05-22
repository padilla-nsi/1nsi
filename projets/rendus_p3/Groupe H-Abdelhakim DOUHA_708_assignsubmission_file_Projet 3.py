from shutil import move
from tkinter import*

from random import*
 

fenetreplateau=Tk()

fenetreplateau.geometry("755x750")

fenetreplateau.title(" Jeu des Petits Chevaux ")

Fondde=Canvas(fenetreplateau,width=200,height=200)

E=Canvas(fenetreplateau,width=750,height=750)



Fondde.place(x=750,y=0)

 

E.place(x=0,y=0)

a=400

b=0

c=0

d=400

e=50

f=450

g=50

h=450

a1=0

b1=0


#Création des ecuries
def ecurie_1():

    ecurie_1 = [1]

def ecurie_2():

    ecurie_2 = [2]

def ecurie_3():

    ecurie_3 = [3]

def ecurie_4():

    ecurie_4 = [4]

 

E.create_rectangle(0,0,300,300,fill='yellow',width=2)

E.create_rectangle(0,450,300,750,fill='blue',width=2)

E.create_rectangle(450,0,750,300,fill='red',width=2)

E.create_rectangle(450,450,750,750,fill='green',width=2)

 
#Creation des placements de depart
E.create_rectangle(0,300,50,350,fill="gold")

E.create_rectangle(400,0,450,50,fill="darkred")

E.create_rectangle(700,400,750,450,fill='darkgreen')

E.create_rectangle(300,700,350,750,fill='darkblue')

E.create_rectangle(700,350,750,400,fill="red")

E.create_rectangle(350,0,400,50,fill="yellow")

E.create_rectangle(0,350,50,400,fill="blue")

E.create_rectangle(350,700,400,750,fill="green")

 
#Creation du milieu
E.create_polygon(350,350,375,375,350,400,outline="black", fill="yellow")

E.create_polygon(400,350,375,375,400,400,outline="black",fill="green")

E.create_polygon(350,350,400,350,375,375,outline="black",fill="red")

E.create_polygon(350,400,400,400,375,375,outline="black",fill="blue")

 
#Creation des chiffres
P1j=Label(fenetreplateau,text="1",font=10,fg="gold")

P2j=Label(fenetreplateau,text="2",font=10,fg="gold")

P3j=Label(fenetreplateau,text="3",font=10,fg="gold")

P4j=Label(fenetreplateau,text="4",font=10,fg="gold")

P5j=Label(fenetreplateau,text="5",font=10,fg="gold")

P6j=Label(fenetreplateau,text="6",font=10,fg="gold")

 

P1b=Label(fenetreplateau,text="6",font=10,fg="blue")

P2b=Label(fenetreplateau,text="5",font=10,fg="blue")

P3b=Label(fenetreplateau,text="4",font=10,fg="blue")

P4b=Label(fenetreplateau,text="3",font=10,fg="blue")

P5b=Label(fenetreplateau,text="2",font=10,fg="blue")

P6b=Label(fenetreplateau,text="1",font=10,fg="blue")

 

P1v=Label(fenetreplateau,text="1",font=10,fg="red")

P2v=Label(fenetreplateau,text="2",font=10,fg="red")

P3v=Label(fenetreplateau,text="3",font=10,fg="red")

P4v=Label(fenetreplateau,text="4",font=10,fg="red")

P5v=Label(fenetreplateau,text="5",font=10,fg="red")

P6v=Label(fenetreplateau,text="6",font=10,fg="red")

 

P1r=Label(fenetreplateau,text="1",font=10,fg="green")

P2r=Label(fenetreplateau,text="2",font=10,fg="green")

P3r=Label(fenetreplateau,text="3",font=10,fg="green")

P4r=Label(fenetreplateau,text="4",font=10,fg="green")

P5r=Label(fenetreplateau,text="5",font=10,fg="green")

P6r=Label(fenetreplateau,text="6",font=10,fg="green")

 

P1j.place(x=70,y=360)

P2j.place(x=120,y=360)

P3j.place(x=170,y=360)

P4j.place(x=220,y=360)

P5j.place(x=270,y=360)

P6j.place(x=320,y=360)

 

P1v.place(x=365,y=60)

P2v.place(x=365,y=110)

P3v.place(x=365,y=160)

P4v.place(x=365,y=210)

P5v.place(x=365,y=260)

P6v.place(x=365,y=310)

 

P6r.place(x=420,y=360)

P5r.place(x=470,y=360)

P4r.place(x=520,y=360)

P3r.place(x=570,y=360)

P2r.place(x=620,y=360)

P1r.place(x=670,y=360)

 

P1b.place(x=365,y=410)

P2b.place(x=365,y=460)

P3b.place(x=365,y=510)

P4b.place(x=365,y=560)

P5b.place(x=365,y=610)

P6b.place(x=365,y=660)



#Def des joueurs
def joueur_1():

    joueur_1 = [5]

def joueur_2():

    joueur_2 = [6]

def joueur_3():

    joueur_3 = [7]

def joueur_4():

    joueur_4 = [8]


#Créations du dé
def update():
    x = 1, 2, 3, 4, 5 ,6
    print(random.randint(1,6))
    tab = [1, 2, 3, 4, 5, 6, 7, 8]

    if x == 6:
        ecurie_1 = 0
        joueur_1 = a + 1

 
#Creation du plateau
for i in range (0,18):

    E.create_rectangle(a1,350,a1+50,400)

    a1=a1+50

    E.create_rectangle(350,b1,400,b1+50)

    b1=b1+50

for i in range (0,7):

    E.create_rectangle(a,300,a+50,350,fill="red")

    a=a+50

    E.create_rectangle(b,400,b+50,450,fill="blue")

    b=b+50

    E.create_rectangle(300,c,350,c+50,fill="yellow")

    c=c+50

    E.create_rectangle(400,d,450,d+50,fill="green")

    d=d+50

for i in range (0,5):

    E.create_rectangle(400,e,450,e+50,fill="red")

    e=e+50

    E.create_rectangle(300,f,350,f+50,fill="blue")

    f=f+50

    E.create_rectangle(g,300,g+50,350,fill="yellow")

    g=g+50

    E.create_rectangle(h,400,h+50,450,fill="green")

    h=h+50

def personnages():
    if x == 6:
        move = 6
fenetreplateau.mainloop()