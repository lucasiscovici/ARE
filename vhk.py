         
from tkinter import *
import numpy as np
from random import *
from math import *
import time 
import matplotlib.pyplot as plt
import sys
import os

def damier(): #fonction dessinant le tableau
    global width,height,c
    ligne_vert()
    ligne_hor()
    pers()
    done()
def done():
    global poi,dico_done,dico_cases
    pol=len(dico_cases)
    for i in range(0,pol):
        dico_done[i]=(0)
def ligne_vert():
    c_x = 0
    while c_x != width:
        can1.create_line(c_x,0,c_x,height,width=1,fill='black')
        c_x+=c

def change_pbm(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global pb_mort
    pb_mort = float(eval(entree.get()))
    #print(pb_mort)
def change_pbi(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global pb_infecte
    pb_infecte = float(eval(entree2.get()))
    #print(pb_infecte)

def change_pbii(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global pb_infecte
    pb_infecte = float(eval(entree2.get()))
    #print(pb_infecte)

def ligne_hor():
    c_y = 0
    while c_y != height:
        can1.create_line(0,c_y,width,c_y,width=1,fill='black')

        c_y+=c
def pers():
    global c,width,height,cbc,dico_cases,poi
    for j in range(0,height):
        if j%60==0:
            j-=j%c
            for i in range(0,width):
                if i%60==0:
                    i-=i%c
                    cbc+=1
                    dico_cases[cbc]=(i,j)
                    poi[cbc]=1
                    can1.create_rectangle(i, j, i+c, j+c, fill='green')
   
    pop=len(dico_cases)     
    ys=np.random.randint(0,pop)
    (xx,yy)=dico_cases[ys]
    poi[ys]=2
    dico_done[ys]=1;
    can1.create_rectangle(xx, yy, xx+c, yy+c, fill='red')
    ysd=np.random.randint(0,pop)
    (xxc,yyc)=dico_cases[ysd]
    poi[ysd]=2
    dico_done[ysd]=1;
    can1.create_rectangle(xxc, yyc, xxc+c, yyc+c, fill='red')
def graphou():
    global uoi,nb_v,nb_r,ht,htt,httt,htttt,nb_n,nb_b,httttt
    uoi+=1
    ht.append(int(uoi))
    htt.append(int(nb_v))
    httt.append(int(nb_r))
    htttt.append(int(nb_n))
    httttt.append(int(nb_b))
    
def graph():
    global uoi,nb_v,nb_r,ht,htt,httt,htttt,nb_n,nb_b,httttt
    
    plt.plot(ht, htt)
   # plt.show()
    plt.plot(ht, httt)
 #   plt.show()
    plt.plot(ht, htttt)
 #  plt.show()
    plt.plot(ht, httttt)
    plt.show()


def ver(x,y):
    global dico_cases,can1,dico_etats    
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    
def red(x,y,u):
    global c,dico_cases,dico_etats,poi
    can1.create_rectangle(x, y, x+c, y+c, fill='red')
    poi[u]=2
    #dico_done[u]=1;

def reds(x,y,u):
    global c,dico_cases,dico_etats,poi
    can1.create_rectangle(x, y, x+c, y+c, fill='red')
    
def green(x,y,u):
    global c,dico_cases,dico_etats
    can1.create_rectangle(x, y, x+c, y+c, fill='green')
    poi[u]=1
def purple(x,y,u):
    global c,dico_cases,dico_etats
    can1.create_rectangle(x, y, x+c, y+c, fill='purple')
    poi[u]=3

def out(): #pour ne pas sortir du tableau 
    global dico_historique,c,dico_cases,width,height
    pol=len(dico_cases)
    for i in range(0,pol):
        (xx,yy)=dico_cases[i]
        dico_cases[i]=(xx%width,yy%height)
        
    
def verti(xx,yy,x,y,u):
    global c,dico_cases,dico_etats,pb_infecte,poi
    if poi[u]==1:
        for name, age in dico_cases.items():
            if age == (xx,yy):
                if poi[name]==2 and random()<pb_infecte:
                    red(x,y,u)
                else :
                    green(x,y,u)
    elif poi[u]==2:
        red(x,y,u)
    

def vertiq(x,y,u):
    global c,dico_cases,dico_etats,pb_infecte,poi
    if poi[u]==2:
        reds(x,y,u)
    else:
        green(x,y,u)
def cheko (x,y,o):
    pol=len(dico_cases)
    for i in range(0,pol):
        (xx,yy)=dico_cases[i]
        if (i!=o):
            if (xx==x and yy==y):
                return True
def mouv():
    #print("--------------------")
    global poi,dico_done
    pol=len(poi)
    for i in range(0,pol):
        if poi[i]==2:
            dico_done[i]+=1;
            #print(i,dico_done[i])
    #print("--------------------")
def noir(x,y,z):
    global c,dico_cases,dico_etats
    can1.create_rectangle(x, y, x+c, y+c, fill='black')
    poi[z]=3

def blue(x,y,z):
    global c,dico_cases,dico_etats
    can1.create_rectangle(x, y, x+c, y+c, fill='blue')
    poi[z]=4
    
def chek():
    global c,dico_cases,dico_etats,dico_historiques,to,poi,dico_done,nbmouv
    pol=len(dico_cases)
    for i in range(0,pol):
        (x,y)=dico_cases[i]
        if poi[i]==2 and dico_done[i] >=nbmouv:
            if random()<pb_mort :
                poi[i]=3
                noir(x,y,i)
            else :
                poi[i]=4
                blue(x,y,i)
        elif poi[i]==3:
            noir(x,y,i)
        elif poi[i]==4:
            blue(x,y,i)
        else:
            if len([c for c,v in dico_cases.items() if v==(x,y)])>1 :
                (xxd,yyd)=dico_historiques[i]
                x=xxd
                y=yyd
                dico_cases[i]=(x,y)
            else:
                (x,y)=dico_cases[i]
            if (x-c,y-c) in to:
                verti(x-c,y-c,x,y,i)
            elif (x-c, y) in to:
                verti(x-c,y,x,y,i)
            elif (x-c, y+c) in to:
                verti(x-c,y+c,x,y,i)
            elif (x+c, y-c) in to:
                verti(x+c,y-c,x,y,i)
            elif (x+c, y) in to:
                verti(x+c,y,x,y,i)
            elif (x+c, y+c) in to:
                verti(x+c,y+c,x,y,i)
            elif (x, y-c) in to:
                verti(x,y-c,x,y,i)
            elif (x, y+c) in to:
                verti(x,y+c,x,y,i)
            else:
                vertiq(x,y,i)
def nbb():
    global nb_v,poi,nb_r,nb_n, nb_b
    nb_v= len([c for c,v in poi.items() if v==1])
    nb_r= len([c for c,v in poi.items() if v==2])
    nb_n= len([c for c,v in poi.items() if v==3])
    nb_b= len([c for c,v in poi.items() if v==4])
    
def gos():#main
    global dico_cases,c,dico_historiques,to,flag,poi,pm
    pm+=1
    pop=len(dico_cases)
    to[:] = [] #on vide le tableau des cases occupées
    if flag==0:#si stop 
        for o in range(0,pop) :
            fdfd=random() #chiffre aleatoire
            (xxx,yyy)=dico_cases[o]
            dico_historiques[o] = (xxx,yyy)
            if poi[o]!=3: #si l'etat est different de la mort
                can1.create_rectangle(xxx, yyy, xxx+c, yyy+c, fill='white')#on colorie les anciennes cases en blancs
                if fdfd >0 and fdfd<=1/9: 
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None) #on vide le dictioraire des cases
                    if len([c for c,v in dico_cases.items() if v==(x-c,y-c)]) == 0: #on verifie que la case ne sois pas occupé
                        dico_cases[o]=(x-c,y-c)#on ajoute la nouvelle coordonée
                        to.append((x-c,y-c))
                        #fen1.update()
                    else:#si case ocuppé on ne bouge pas
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=2/9 and fdfd >1/9:
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    if len([c for c,v in dico_cases.items() if v==(x,y-c)]) == 0:
                        dico_cases[o]=(x,y-c)
                        to.append((x,y-c))
                        #fen1.update()
                    else:
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=3/9 and fdfd >2/9:
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    if len([c for c,v in dico_cases.items() if v==(x+c,y-c)]) == 0:
                        dico_cases[o]=(x+c,y-c)
                        to.append((x+c,y-c))
                        #fen1.update()
                    else:
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=4/9 and fdfd >3/9:
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    if len([c for c,v in dico_cases.items() if v==(x-c,y)]) == 0:
                        to.append((x-c,y))
                        dico_cases[o]=(x-c,y)
                        #fen1.update()
                    else:
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=5/9 and fdfd >4/9 :
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    if len([c for c,v in dico_cases.items() if v==(x+c,y)]) == 0:
                        dico_cases[o]=(x+c,y)
                        to.append((x+c,y))
                        #fen1.update()
                    else:
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=6/9 and fdfd >5/9 :
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    if len([c for c,v in dico_cases.items() if v==(x-c,y+c)]) == 0:
                        dico_cases[o]=(x-c,y+c)
                        to.append((x-c,y+c))
                        #fen1.update()
                    else:
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=7/9 and fdfd >6/9 :
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    if len([c for c,v in dico_cases.items() if v==(x,y+c)]) == 0:
                        dico_cases[o]=(x,y+c)
                        to.append((x,y+c))
                        #fen1.update()
                    else:
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=8/9 and fdfd >7/9 :
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    if len([c for c,v in dico_cases.items() if v==(x+c,y+c)]) == 0:
                        dico_cases[o]=(x+c,y+c)
                        to.append((x+c,y+c))
                        #fen1.update()
                    else:
                        dico_cases[o]=(x,y)
                        to.append((x,y))
                if fdfd <=9/9 and fdfd >8/9 :
                    (x,y)=dico_cases[o]
                    dico_cases.pop(o, None)
                    dico_cases[o]=(x,y)
                    to.append((x,y))
                    #fen1.update()
        out()#un ... ne peux pas s'echaper du tableau 
        mouv()
        chek()
        nbb()
        fen1.update()
        #time.sleep(0.1)
        graphou()
        gos()
    
    
def go():
    #print(cbc)
    global width,height
    countt=0
    x=np.random.randint(0,height)
    y=np.random.randint(0,width)
    count=0
    x-=x%c
    y-=y%c
    if (y <= height and y >=0 and x>=0 and x<=width ):
        can1.create_rectangle(x, y, x+c, y+c, fill='purple')
        dico_case[x,y]=1
        dico_etat[x,y]=1
        dico_cont[x,y]=1
        fen1.update()
        contr()
    else :
        go()
      
    #les différentes variables:
def contr():
    global dico_etat,dico_case,pb_mort,dico_cont,gg,width,height,nbn
    if gg!=0:
        dico_cont.clear()
    for o in [c for c,v in dico_etat.items() if v==1] :
        (x,y)=o
        if random()<=pb_mort:
            dico_etat[x,y]=2
            dico_case[x,y]=2
        else :
            dico_etat[x,y]=3
            dico_case[x,y]=3
        #print(x,y)
        if (y <= height and y >=0 and x>=0 and x<=width ):
            #print('oo',x,y)
            contamination(x,y)
    nbn+=1
    nouv()
def stop():
    "arrêt de l'animation"
    
    global flag ,nume

    if nume==0 or nume%2==0:
        flag =1
        graph()
        nume+=1
    else:
        flag=0
        plt.close()
        nume+=1
        gos()

def contamination(x,y):
    place_xx=0.0
    global dico_etat,dico_case,pb_infecte,dico_cont
    countt=1
    
    place_yy=0.0
    for i in range(1,9):
        place_xx=place_x(x,i)
        place_yy=place_y(y,i)
        if random()<=pb_infecte and not((place_xx,place_yy) in dico_case  )and not((place_xx,place_yy) in dico_etat) :
            dico_case[place_xx,place_yy]=1
            dico_etat[place_xx,place_yy]=1
            dico_cont[place_xx,place_yy]=1
        elif not((place_xx,place_yy) in dico_case) and not((place_xx,place_yy) in dico_etat):
            dico_etat[place_xx,place_yy]=3
            dico_cont[place_xx,place_yy]=1
def nouv():
    global dico_case,dico_etat,dico_cont,dico_case_3,dico_case_2,dico_case_1
    #graph()
    for j in [c for c,v in dico_case.items() if v==1] :
        (x, y) = j
        dico_case_1+=1
        if dico_cont[x,y] :
            can1.create_rectangle(x,y,x+c,y+c, fill='purple')
            fen1.update()
    for o in [c for c,v in dico_etat.items() if v==2] :
        (xx, yy) = o
        dico_case_2+=1
        if dico_cont[xx,yy] :
            can1.create_rectangle(xx,yy,xx+c,yy+c, fill='black')
            fen1.update()
    for p in [c for c,v in dico_etat.items() if v==3] :
        (xxx, yyy) = p
        if dico_cont[xxx,yyy] :
            dico_case_3+=1
            can1.create_rectangle(xxx,yyy,xxx+c,yyy+c, fill='green')
            fen1.update()
    
    contr()
def change_nbmouv(event):
    global nbmouv
    nbmouv=float(eval(entree3.get()))
    done()

def restart_program():
    global poi,dico_done,dico_cases
    pop=len(dico_cases)
    ys=np.random.randint(0,pop)
    (xx,yy)=dico_cases[ys]
    while (poi[ys]==2 or  poi[ys]==3):
        ys=np.random.randint(0,pop)
        (xx,yy)=dico_cases[ys]
    poi[ys]=2
    dico_done[ys]=1;
    can1.create_rectangle(xx, yy, xx+c, yy+c, fill='red')
    gos()
def place_x(v,n):
    if n==1 or n==4 or n==6:
        return v-c
    elif n==2 or n==7:
        return v
    elif n==3 or n==5 or n==8:
        return v+c
def place_y(o,p):
    if p==1 or p==2 or p==3:
        return o-c
    elif p==4 or p==5 :
        return o
    elif p==6 or p==7 or p==8 :
        return o+c

ht=[]
httt=[]
htttt=[]
httttt=[]
nume=0
htt=[]
to=[]
pm=-1
nbn=0
height = 800
width = 1200
count=0
nbmouv=30
gg=0
pb_infecte=1
pb_mort=0.1
#taille des celluses
c = 10
uoi=0
dico_case_1=0
dico_case_2=0
dico_case_3=0
cbc=-1
nb_v=0
nb_n=0
nb_b=0
nb_r=0
#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=5

flag=0
dico_etats = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
dico_case = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
dico_cont = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
dico_cases = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
dico_historiques = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
dico_done = {}
dico_meurt ={}
dico_guerri = {}
poi = {}
#programme "principal" 
fen1 = Tk()
can1 = Canvas(fen1, width =width, height =height, bg ='white')

can1.pack(side =TOP, padx =5, pady =5)
#graph()

damier()

b1 = Button(fen1, text ='Go!', command =gos)

b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen1, text ='Stop', command =stop)
b2.pack(side =LEFT, padx =3, pady =3)
b3 = Button(fen1, text ='restart', command =restart_program)
b3.pack(side =LEFT, padx =3, pady =3)
entree = Entry(fen1)
entree.bind("<Return>", change_pbm)
entree.pack(side =RIGHT)
chaine = Label(fen1)
chaine.configure(text = "proba de mort:")
chaine.pack(side =RIGHT)
entree3 = Entry(fen1)
entree3.bind("<Return>", change_nbmouv)
entree3.pack(side =RIGHT)
chaine3 = Label(fen1)
chaine3.configure(text = "Nb mouv:")
chaine3.pack(side =RIGHT)
entree2 = Entry(fen1)
entree2.bind("<Return>", change_pbii)
entree2.pack(side =RIGHT)
chaine2 = Label(fen1)
chaine2.configure(text = "proba d'infecté:")
chaine2.pack(side =RIGHT)
fen1.mainloop()
