## PROJET D'INFORMATIQUE : RESOLUTION D'UN SUDOKU

import numpy as np
from tkinter import *
global root
global numGrille

## Résolution du sudoku

# Numérotation des cases d'une grille : Les cases sont numérotées par grand carré (ils sont au nombre de 9 et de taille 3x3). Dans chaque grand carré, le numéro des cases est dans l'ordre croissant en allant de la gauche vers la droite puis du haut vers le bas. Les grands carrés sont 'remplis' dans le même ordre. On a ainsi des cases numérotées de 1 à 81. 

def numero(i,j):
    """
    La fonction numero(i,j) permet de passer du numéro d’une case (entre 1 et 81) à ses indices (ligne,colonne).
    """
    a=i//3
    b=j//3
    c=3*a+b
    num=9*c+j%3+3*(i%3)+1
    return(num)
        
def indices(num):
        """
        La fonction indices(num) permet de passer des indices d’une case à son numéro.
        """
        num=num-1
        a=(num)//9
        l=a//3
        c=3*(a-3*l)
        n=num-9*a
        i=3*l+n//3
        j=c+(n-3*(n//3))
        return(i,j)
        
def Donnees(grille):
        """
        La fonction Donnees(grille) permet d’initialiser le tableau à 3 dimensions (S).
        """
        S=np.zeros((9,9,10))
        S[:,:,0]=grille
        for i in range (9):
                for j in range (9):
                        if grille[i,j]!=0:
                                a=grille[i,j]
                                S[i,:,int(a)]=[numero(i,j) for z in range (9)]
                                S[:,j,int(a)]=[numero(i,j) for z in range (9)]
                                carre=(numero(i,j)-1)//9
                                for k in range (9):
                                        (n,p)=indices(9*carre+k+1)
                                        S[n,p,int(a)]=numero(i,j)
        return(S)

def Affectation(T,case,num):
        """
        Pour une case vide donnée, la fonction Affectation(T,case,num) permet d'affecter un chiffre(num) dans la case et de traduire dans S toutes les conditions impliquant la présence du chiffre num (compris entre 1 et 9) dans la case de numéro case.
        """
        (i,j)=indices(case)
        T[i,j,0]=num
        for k in range (9):
                if T[i,k,num]==0:
                        T[i,k,num]=case
        for k in range (9):
                if T[k,j,num]==0:
                        T[k,j,num]=case
        c=(case-1)//9
        for k in range (9):
                (n,p)=indices(9*c+k+1)
                if T[n,p,num]==0:
                        T[n,p,num]=case

def Desaffectation(T,case):
        """
        La fonction Desaffectation(T,case) vide la case de numéro [case] dans la profondeur 0 de S et supprime toute les cases qui contiennent [case] dans la profondeur associée de S.
        """
        (n,p)=indices(case)
        num=int(T[n,p,0])
        T[n,p,0]=0
        for i in range (9):
                for j in range (9):
                        if T[i,j,num]==case:
                                T[i,j,num]=0

def Resolution(grille):
        """
        La fonction Resolution grille résoud la grille de sudoku.
        """
        S=Donnees(grille)
        ListeAffectations=[]
        ListeCasesLibres=[]
        for i in range (9):
                for j in range (9):
                        if S[i,j,0]==0:
                                ListeCasesLibres.append(numero(i,j))
        k=1
        while len(ListeCasesLibres)>0:
                (i,j)=indices(ListeCasesLibres[-1])
                while k<10 and S[i,j,0]==0:
                        if S[i,j,k]==0:
                                Affectation(S,ListeCasesLibres[-1],k)
                                ListeAffectations.append(ListeCasesLibres[-1])
                                ListeCasesLibres.pop()
                                k=1
                        else:
                                k+=1
                if k==10:
                        ListeCasesLibres.append(ListeAffectations[-1])
                        ListeAffectations.pop()
                        (i,j)=indices(ListeCasesLibres[-1])
                        k=int(S[i,j,0]+1)
                        Desaffectation(S,ListeCasesLibres[-1])        
        return(S)


## Grilles de sudoku


grilleVide=np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])

grille1=np.array([[0,6,0,0,8,0,4,2,0],[0,1,5,0,6,0,3,7,8],[0,0,0,4,0,0,0,6,0],[1,0,0,6,0,4,8,3,0],[3,0,6,0,1,0,7,0,5],[0,8,0,3,5,0,0,0,0],[8,3,0,9,4,0,0,0,0],[0,7,2,1,3,0,9,0,0],[0,0,9,0,2,0,6,1,0]])

grille2=np.array([[9,6,0,1,0,0,0,0,0],[0,0,0,0,0,0,5,0,0],[0,0,0,0,0,7,0,8,2],[0,0,5,0,6,0,0,0,0],[0,0,1,0,2,0,0,9,8],[0,0,3,0,7,0,0,0,0],[0,0,0,0,0,8,0,1,3],[0,0,0,0,0,0,7,0,0],[7,4,0,2,0,0,0,0,0]])

grille3=np.array([[5,0,3,0,0,4,2,0,0],[2,7,0,0,0,0,0,0,1],[0,0,0,0,2,0,0,0,0],[0,2,0,4,0,0,0,0,7],[4,3,0,0,8,0,0,0,2],[0,5,0,0,0,0,8,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,5,9,0,0,0,4],[3,0,5,0,1,0,9,0,6]])

grille4=np.array([[0,9,0,4,0,0,0,3,0],[5,0,3,0,0,0,7,0,0],[1,0,0,0,2,7,0,0,8],[7,0,4,0,0,0,0,0,0],[0,0,0,1,8,4,0,0,0],[0,0,0,0,0,0,4,0,5],[4,0,0,5,6,0,0,0,3],[0,0,5,0,0,0,1,0,7],[0,3,0,0,0,2,0,4,0]])

grille5=np.array([[0,0,0,0,2,9,8,3,0],[0,0,0,0,0,0,0,0,0],[8,5,0,7,0,0,2,0,0],[0,0,3,6,7,0,0,4,0],[0,1,9,0,0,0,6,8,0],[0,6,0,0,8,1,3,0,0],[0,0,8,0,0,7,0,9,5],[0,0,0,0,0,0,0,0,0],[0,2,5,4,1,0,0,0,0]])

grille6=np.array([[0,5,0,6,0,2,9,0,0],[0,4,0,5,7,0,0,0,0],[0,7,9,0,0,0,3,0,0],[0,0,0,0,5,0,0,4,7],[4,3,0,0,0,0,0,1,0],[0,0,0,0,0,4,6,0,0],[7,2,0,0,1,0,0,0,0],[6,0,3,0,8,0,0,0,0],[5,9,0,0,0,0,7,6,0]])

grille7=np.array([[7,0,0,0,0,0,0,0,0],[2,6,0,3,0,8,0,0,0],[0,0,0,5,4,0,0,2,0],[0,3,2,0,9,0,4,0,5],[0,9,0,0,0,0,0,6,0],[6,0,7,0,5,0,1,3,0],[0,8,0,0,6,4,0,0,0],[0,0,0,2,0,1,0,9,3],[0,0,0,0,0,0,0,0,7]])

grille8=np.array([[0,0,0,5,6,0,0,7,0],[4,5,0,0,9,7,0,0,0],[0,0,6,0,0,0,0,0,1],[5,4,0,9,0,0,0,0,7],[0,0,0,0,0,0,0,9,4],[1,9,0,0,7,3,0,0,0],[0,7,4,0,0,0,1,0,3],[2,0,0,0,0,0,0,0,9],[0,0,0,2,1,0,0,0,6]])

grille9=np.array([[0,0,0,0,0,0,0,3,0],[3,4,9,0,0,1,2,0,0],[0,5,0,0,0,0,9,0,0],[0,2,0,5,0,8,0,0,0],[0,0,0,0,0,0,8,6,7],[6,0,0,0,0,0,0,0,4],[0,0,0,6,0,0,0,0,0],[5,9,8,7,0,4,0,0,0],[7,0,0,2,0,0,0,0,8]])

ListeGrilles=[grille1,grille2,grille3,grille4,grille5,grille6,grille7,grille8,grille9]
ListeCasesLibresGrilles=[]

for grille in ListeGrilles:
        L=[]
        for i in range(9):
                for j in range(9):
                        if grille[i,j]==0:
                                L.append(numero(i,j))
        ListeCasesLibresGrilles.append(L)
 
        
## Tkinter : Affichage du sudoku et mode joueur
  
  
# Création et affichage de la première fenêtre 

numGrille=0
root = Tk()
root.title("Debut")
root.geometry("600x600")
root.configure(background="gray99")
Titre=Label(root, text="SUDOKU",bg="gray99",fg="red3",font="Impact 60")
Titre.place(relx=0.29, rely=0.25)
Nom1=Label(root, text="COSQUER Sébastien",bg="gray99",fg="firebrick2",font="Calibri 12")
Nom1.place(relx=0.40, rely=0.42)
Nom2=Label(root, text="MICHEL Julien",bg="gray99",fg="firebrick2",font="Calibri 12")
Nom2.place(relx=0.43, rely=0.45)
Nom3=Label(root, text="MEZZADRI Apolline",bg="gray99",fg="firebrick2",font="Calibri 12")
Nom3.place(relx=0.405, rely=0.48)


def Menu():
        """
        La fonction Menu() affiche une fenêtre permettant de choisir entre choisir une grille ou l'entrer manuellement.
        """
        global fenetre,root
        fenetre.destroy()
        root=Tk()
        root.title("Menu")
        root.geometry("600x600")
        BoutonChoixGrille=Button(root, text="Choisir une grille",command=ChoixGrille)
        BoutonChoixGrille.place(relx = 0.25, rely=0.65)
        BoutonEntrerGrille=Button(root, text="Entrer une grille",command=EntrerGrille)
        BoutonEntrerGrille.place(relx = 0.60, rely=0.65)
        root.configure(background="gray99")
        Titre=Label(root, text="SUDOKU",bg="gray99",fg="red3",font="Impact 60")
        Titre.place(relx=0.29, rely=0.25)
        Nom1=Label(root, text="COSQUER Sébastien",bg="gray99",fg="firebrick2",font="Calibri 12")
        Nom1.place(relx=0.40, rely=0.42)
        Nom2=Label(root, text="MICHEL Julien",bg="gray99",fg="firebrick2",font="Calibri 12")
        Nom2.place(relx=0.43, rely=0.45)
        Nom3=Label(root, text="MEZZADRI Apolline",bg="gray99",fg="firebrick2",font="Calibri 12")
        Nom3.place(relx=0.405, rely=0.48)


def EntrerGrille():
        """
        La fonction EntrerGrille() affiche une fenêtre avec une grille vide que l'on peut remplir et sur laquelle on peut joue ou dont on peut afficher la solution à tout moment.
        """
        global canvas,T,ListeCasesLibresInit,fenetre,root,jeu
        root.destroy()
        fenetre=Tk()
        fenetre.title("Saisie manuelle")
        canvas=Canvas(fenetre,width=600,height=600,background="gray99")
        T=Donnees(grilleVide)
        Affichage(T)
        ListeCasesLibresInit=[k+1 for k in range(81)]
        fenetre.bind("<Button-1>", EntrerValeur)
        solution=Button(fenetre,text="Solution",command=Solution)
        solution.place(relx=0.45,rely=0.92)
        jeu=Button(fenetre,text="Jouer",command=Jouer1)
        jeu.place(relx=0.465,rely=0.85)
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        canvas.pack()
        fenetre.mainloop()

def ChoixGrille():
        """
        La fonction ChoixGrille() affiche une fenêtre contenant la première grille et permettant de sélectionner une grille.
        """
        global canvas,numGrille,Suivant,Precedent,fenetre,Resoudre,root,jeu,T,ListeCasesLibresInit
        root.destroy()
        fenetre=Tk()
        fenetre.title("Choix")
        canvas=Canvas(fenetre,width=600,height=600,background="gray99")
        T=Donnees(ListeGrilles[0])
        ListeCasesLibresInit=ListeCasesLibresGrilles[0]
        Affichage(T)
        numGrille=0
        jeu=Button(fenetre,text="Jouer",command=Jouer1)
        jeu.place(relx=0.465,rely=0.85)
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        Precedent=Button(fenetre,text="Grille précédente",command=GrillePrecedente)
        Precedent.place(relx = 0.08, rely=0.85)
        Suivant=Button(fenetre,text="Grille suivante",command=GrilleSuivante)
        Suivant.place(relx = 0.77, rely=0.85)
        Resoudre=Button(fenetre,text="Solution",command=Solution)
        Resoudre.place(relx = 0.45, rely=0.92)
        canvas.pack()
        fenetre.mainloop()

def GrillePrecedente():
        """
        La fonction GrillePrecedente baisse le numéro de la grille de 1 si il n'est pas à 0 et affiche la grille correspondante.
        """
        global numGrille,T,ListeCasesLibresInit
        if numGrille!=0:
                numGrille-=1
                T=Donnees(ListeGrilles[numGrille])
                ListeCasesLibresInit=ListeCasesLibresGrilles[numGrille]
                Affichage(T)

def GrilleSuivante():
        """
        La fonction GrilleSuivante augmente le numéro de la grille de 1 si il n'est pas à 8 et affiche la grille correspondante.
        """
        global numGrille,T,ListeCasesLibresInit
        if numGrille!=8:
                numGrille+=1
                T=Donnees(ListeGrilles[numGrille])
                ListeCasesLibresInit=ListeCasesLibresGrilles[numGrille]
                Affichage(T)


def Affichage(T):
        
        """
        La fonction Affichage(T) affiche la grille en cours.
        """
        canvas.delete("all")
        for k in range(4):
                canvas.create_line(50,10+k*500/3,550,10+k*500/3,width=3)
                canvas.create_line(50+k*500/3,10,50+k*500/3,510,width=3)
        for k in range(10):
                canvas.create_line(50,10+k*500/9,550,10+k*500/9)
                canvas.create_line(50+k*500/9,10,50+k*500/9,510)
        for i in range(9):
                for j in range(9):
                        if T[i,j,0]!=0:
                                if numero(i,j) in ListeCasesLibresInit :
                                        canvas.create_text(50+500/18+j*500/9,10+500/18+i*500/9,text=str(int(T[i,j,0])),font=("arial",11))
                                else :
                                        canvas.create_text(50+500/18+j*500/9,10+500/18+i*500/9,text=str(int(T[i,j,0])),font=("arial",11,"bold"))

def Affichage2(T):
        """
        La fonction Affichage2(T) affiche la solution de la grille.
        """
        global canvas2
        canvas2.delete("all")
        for k in range(4):
                canvas2.create_line(50,10+k*500/3,550,10+k*500/3,width=3)
                canvas2.create_line(50+k*500/3,10,50+k*500/3,510,width=3)
        for k in range(10):
                canvas2.create_line(50,10+k*500/9,550,10+k*500/9)
                canvas2.create_line(50+k*500/9,10,50+k*500/9,510)
        for i in range(9):
                for j in range(9):
                        if T[i,j,0]!=0:
                                if numero(i,j) in ListeCasesLibresInit :
                                        canvas2.create_text(50+500/18+j*500/9,10+500/18+i*500/9,text=str(int(T[i,j,0])),font=("arial",11))
                                else :
                                        canvas2.create_text(50+500/18+j*500/9,10+500/18+i*500/9,text=str(int(T[i,j,0])),font=("arial",11,"bold"))


def Jouer():
        """
        La fonction Jouer() crée la fenêtre de jeu avec les boutons correspondants et permet d'affecter des valeurs.
        """
        global T,ListeCasesLibresInit,jeu,fenetre,canvas,ListeCasesLibresJeu,S
        fenetre.destroy()
        fenetre=Tk()
        fenetre.title("JEU")
        canvas=Canvas(fenetre,width=600,height=600,background="gray99")
        verif=Button(fenetre,text="Vérifier",command=Verifier)
        verif.place(relx=0.455,rely=0.85)
        fenetre.bind("<Button-1>", EntrerValeurJeu)
        solution=Button(fenetre,text="Solution",command=SolutionJeu)
        solution.place(relx=0.45,rely=0.92)
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        Affichage(T)
        canvas.pack()
        fenetre.mainloop()        

def Jouer1():
        """
        La fonction Jouer1() initialise la liste des cases libres et la solution.
        """
        global T,S,ListeCasesLibresJeu,ListeCasesLibresInit
        S=Resolution(T[:,:,0])
        ListeCasesLibresJeu=ListeCasesLibresInit
        ModesJeu()
        
def JouerErreurs():
        """
        La fonction JouerErreurs() crée la fenêtre de jeu avec les boutons correspondants et permet d'affecter des valeurs.
        """
        global T,ListeCasesLibresInit,jeu,fenetre,canvas,ListeCasesLibresJeu,S
        fenetre.destroy()
        fenetre=Tk()
        fenetre.title("JEU")
        canvas=Canvas(fenetre,width=600,height=600,background="gray99")
        fenetre.bind("<Button-1>", EntrerValeurJeuErreurs)
        solution=Button(fenetre,text="Solution",command=SolutionJeu)
        solution.place(relx=0.45,rely=0.92)
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        Affichage(T)
        canvas.pack()
        fenetre.mainloop()
        

def ModesJeu():
        """
        La fonctions ModesJeu() crée la fenêtre de sélection du mode avec ou sans contraintes.
        """
        global fenetre
        fenetre.destroy()
        fenetre=Tk()
        fenetre.title("Mode de jeu")
        fenetre.geometry("600x600")
        sans=Button(fenetre,text="Sans contraintes",command=Jouer)
        sans.place(relx=0.1, rely=0.6)
        avec=Button(fenetre,text="Avec contraintes",command=Difficulte)
        avec.place(relx=0.7, rely=0.6)
        fenetre.configure(background="gray99")
        titre=Label(fenetre, text="Difficulté",bg="gray99",fg="black",font="Impact 40")
        titre.place(relx=0.31, rely=0.26)
        regles1=Label(fenetre, text="Sans contraintes : Vous êtes libres de vous tromper autant de fois que vous le voulez !",bg="gray99",fg="black",font="Arial 10")
        regles1.place(relx=0.1, rely=0.43)
        regles2=Label(fenetre, text="Avec contraintes : Attention à ne pas vous tromper trop de fois !",bg="gray99",fg="black",font="Arial 10")
        regles2.place(relx=0.18, rely=0.40)

def Difficulte():
        """
        La fonction Difficulte() crée la fenêtre de sélection du nombre d'erreurs possibles.
        """
        global fenetre,T,Tinit,erreurs
        erreurs=0
        Tinit=T.copy()
        fenetre.destroy()
        fenetre=Tk()
        fenetre.title("Difficulté")
        fenetre.configure(background="gray99")
        Titre=Label(fenetre, text="Combien d'erreurs autorisées ?",bg="gray99",font="Arial 25")
        Titre.place(relx=0.15, rely=0.15)
        fenetre.geometry("600x600")
        e1=Button(fenetre,text="1",command=b1)
        e1.place(relx=0.25,rely=0.4)
        e2=Button(fenetre,text="2",command=b2)
        e2.place(relx=0.5,rely=0.4)
        e3=Button(fenetre,text="3",command=b3)
        e3.place(relx=0.75,rely=0.4)
        e4=Button(fenetre,text="4",command=b4)
        e4.place(relx=0.25,rely=0.6)
        e5=Button(fenetre,text="5",command=b5)
        e5.place(relx=0.5,rely=0.6)
        e6=Button(fenetre,text="6",command=b6)
        e6.place(relx=0.75,rely=0.6)
        e7=Button(fenetre,text="7",command=b7)
        e7.place(relx=0.25,rely=0.8)
        e8=Button(fenetre,text="8",command=b8)
        e8.place(relx=0.5,rely=0.8)
        e9=Button(fenetre,text="9",command=b9)
        e9.place(relx=0.75,rely=0.8)
        fenetre.mainloop()

# Les fonctions b1 à b9 affecte le bon nombres d'erreurs maximal.

def b1():
        """
        La fonction b1() affecte la valeur 1 pour le nombres d'erreurs maximal.
        """
        global erreursmax
        erreursmax=1
        JouerErreurs()
        
def b2():
        global erreursmax
        erreursmax=2
        JouerErreurs()
def b3():
        global erreursmax
        erreursmax=3
        JouerErreurs()
def b4():
        global erreursmax
        erreursmax=4
        JouerErreurs()
def b5():
        global erreursmax
        erreursmax=5
        JouerErreurs()
        
def b6():
        global erreursmax
        erreursmax=6
        JouerErreurs()
        
def b7():
        global erreursmax
        erreursmax=7
        JouerErreurs()
        
def b8():
        global erreursmax
        erreursmax=8
        JouerErreurs()
        
def b9():
        global erreursmax
        erreursmax=9
        JouerErreurs()


def EntrerValeur(event):
        """
        La fonction EntrerValeur(event) fait apparaître la liste déroulante sur la case choisie.
        """
        global T,ListeCasesLibresInit,canvas,fenetre,ListeChiffres,case
        x=event.x
        y=event.y
        i=int(9*(y-10)/(500))
        j=int(9*(x-50)/(500))
        case=numero(i,j)
        ListeChiffres=Listbox(fenetre)
        if x <550 and x>50 and y >10 and y<510:
                ListeChiffres.insert(END,"Effacer")
                for k in range(9):
                       ListeChiffres.insert(END,str(k+1))
                ListeChiffres.place(relx=x/600,rely=y/600)
                if case not in ListeCasesLibresInit:
                        Desaffectation(T,case)
                        ListeCasesLibresInit=[case]+ListeCasesLibresInit
                fenetre.bind('<Button-1>',AffecterValeur)

def EntrerValeurJeu(event):
        """
        La fonction EntrerValeurJeu(event) fait apparaître la liste déroulante sur la case choisie.
        """
        global T,ListeCasesLibresInit,canvas,fenetre,ListeChiffres,case,ListeCasesLibresJeu
        x=event.x
        y=event.y
        i=int(9*(y-10)/(500))
        j=int(9*(x-50)/(500))
        case=numero(i,j)
        if x <550 and x>50 and y >10 and y<510:
                if case in ListeCasesLibresInit:
                        ListeChiffres=Listbox(fenetre)
                        ListeChiffres.insert(END,"Effacer")
                        for k in range(9):
                                ListeChiffres.insert(END,str(k+1))
                        ListeChiffres.place(relx=x/600,rely=y/600)
                        if case not in ListeCasesLibresJeu:
                                Desaffectation(T,case)
                                ListeCasesLibresJeu=[case]+ListeCasesLibresJeu
                        fenetre.bind('<Button-1>',AffecterValeurJeu)

def EntrerValeurJeuErreurs(event):
        """
        La fonction EntrerValeurJeuErreurs(event) fait apparaître la liste déroulante sur la case choisie.
        """
        global T,ListeCasesLibresInit,canvas,fenetre,ListeChiffres,case,ListeCasesLibresJeu
        x=event.x
        y=event.y
        i=int(9*(y-10)/(500))
        j=int(9*(x-50)/(500))
        case=numero(i,j)
        if x <550 and x>50 and y >10 and y<510:
                if case in ListeCasesLibresInit:
                        ListeChiffres=Listbox(fenetre)
                        ListeChiffres.insert(END,"Effacer")
                        for k in range(9):
                                ListeChiffres.insert(END,str(k+1))
                        ListeChiffres.place(relx=x/600,rely=y/600)
                        if case not in ListeCasesLibresJeu:
                                Desaffectation(T,case)
                                ListeCasesLibresJeu=[case]+ListeCasesLibresJeu
                        fenetre.bind('<Button-1>',AffecterValeurJeuErreurs)

def AffecterValeur(event):
        """
        La fonction AffecterValeur(event) détecte un clic sur la liste déroulante et affecte la valeur choisie.
        """
        global ListeChiffres,T,ListeCasesLibresInit,canvas,fenetre,case
        (i,j)=indices(case)
        num=int(ListeChiffres.curselection()[0])
        if num!=0:
                for k in range (len(ListeCasesLibresInit)):
                        if ListeCasesLibresInit[k]==case:
                                ListeCasesLibresInit=ListeCasesLibresInit[:k]+ListeCasesLibresInit[k+1:]
                                break
                Affectation(T,case,num)
        elif T[i,j,0]!=0:
                Desaffectation(T,case)
        ListeChiffres.destroy()
        Affichage(T)
        fenetre.bind("<Button-1>",EntrerValeur)
        
def AffecterValeurJeu(event):
        """
        La fonction AffecterValeurJeu(event) détecte un clic sur la liste déroulante et affecte la valeur choisie.
        """
        global ListeChiffres,T,ListeCasesLibresJeu,canvas,fenetre,case,S
        num=int(ListeChiffres.curselection()[0])
        (i,j)=indices(case)
        if num!=0:                
                for k in range (len(ListeCasesLibresJeu)):
                        if ListeCasesLibresJeu[k]==case:
                                ListeCasesLibresJeu=ListeCasesLibresJeu[:k]+ListeCasesLibresJeu[k+1:]
                                break
                Affectation(T,case,num)
        elif T[i,j,0]!=0:
                Desaffectation(T,case)
        ListeChiffres.destroy()
        Affichage(T)
        fenetre.bind("<Button-1>",EntrerValeurJeu)
        if (T[:,:,0]==S[:,:,0]).all():
                Victoire()
        
def AffecterValeurJeuErreurs(event):
        """
        La fonction AffecterValeurJeuErreurs(event) détecte un clic sur la liste déroulante et affecte la valeur choisie.
        """
        global ListeChiffres,T,ListeCasesLibresJeu,canvas,fenetre,case,S,erreurs,erreursmax
        num=int(ListeChiffres.curselection()[0])
        (i,j)=indices(case)
        if num!=0:                
                for k in range (len(ListeCasesLibresJeu)):
                        if ListeCasesLibresJeu[k]==case:
                                ListeCasesLibresJeu=ListeCasesLibresJeu[:k]+ListeCasesLibresJeu[k+1:]
                                break
                Affectation(T,case,num)
        elif T[i,j,0]!=0:
                Desaffectation(T,case)
        ListeChiffres.destroy()
        Affichage(T)
        for i in range(9):
                for j in range (9):
                        if T[i,j,0]!=0 and T[i,j,0]!=S[i,j,0]:
                                erreurs+=1
                                if erreurs== erreursmax:
                                        Defaite()
                                Verifier2()                
        fenetre.bind("<Button-1>",EntrerValeurJeuErreurs)
        if (T[:,:,0]==S[:,:,0]).all():
                Victoire()


def Victoire():
        """
        La fonction Victoire() affiche la fenêtre de victoire lorsque le sudoku est correctement rempli.
        """
        global fenetre
        fenetre.destroy()
        fenetre=Tk()
        fenetre.geometry("600x600")
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        fenetre.configure(background="gray99")
        titre=Label(fenetre, text="VICTOIRE",bg="gray99",fg="green3",font="Impact 60")
        titre.place(relx=0.26, rely=0.28)
        fenetre.mainloop()
        
def Defaite():
        """
        La fonction Defaite() affiche la fenêtre de défaite quand le  nombre d'erreurs commises est trop élevé en mode 'avec contraintes'.
        """
        global fenetre,Tinit,T,erreurs
        fenetre.destroy()
        fenetre=Tk()
        T=Tinit.copy()
        erreurs=0
        fenetre.geometry("600x600")
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        Rejoue=Button(fenetre,text='Rejouer',command=JouerErreurs)
        Rejoue.place(relx=0.45, rely=0.92)
        fenetre.configure(background="gray99")
        titre=Label(fenetre, text="DÉFAITE !",bg="gray99",fg="red3",font="Impact 60")
        titre.place(relx=0.26, rely=0.28)
        fenetre.mainloop()


def Verifier():
        """
        La fonction Verifier() affiche la grille en cours avec les erreurs encadrées en rouge.
        """
        global T,S,canvas,fenetre
        fenetre.destroy()
        fenetre=Tk()
        fenetre.title("Vérification")
        canvas=Canvas(fenetre,width=600,height=600)
        Continuer=Button(fenetre,text="Continuer",command=Jouer)
        Continuer.place(relx=0.445,rely=0.85)
        solution=Button(fenetre,text="Solution",command=SolutionJeu)
        solution.place(relx=0.45,rely=0.92)
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        Affichage(T)
        for i in range(9):
                for j in range(9):
                        if T[i,j,0]!=0 and T[i,j,0]!=S[i,j,0]:
                                pts=[(50+j*500/9,10+i*500/9),(50+(j+1)*500/9,10+i*500/9),(50+(j+1)*500/9,10+(i+1)*500/9),(50+j*500/9,10+(i+1)*500/9)]
                                canvas.create_polygon(pts,outline="red",fill='')
        canvas.pack()
        fenetre.mainloop()

def Verifier2():
        """
        La fonction Verifier2() affiche la grille en cours avec les erreurs encadrées en rouge.
        """
        global T,S,canvas,fenetre
        fenetre.destroy()
        fenetre=Tk()
        fenetre.title("Vérification")
        canvas=Canvas(fenetre,width=600,height=600)
        Continuer=Button(fenetre,text="Continuer",command=JouerErreurs)
        Continuer.place(relx=0.445,rely=0.85)
        solution=Button(fenetre,text="Solution",command=SolutionJeu)
        solution.place(relx=0.45,rely=0.92)
        Quitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
        Quitter.place(relx=0.83,rely=0.92)
        Accueil=Button(fenetre,text="Accueil",command=Menu)
        Accueil.place(relx=0.08,rely=0.92)
        Affichage(T)
        for i in range(9):
                for j in range(9):
                        if T[i,j,0]!=0 and T[i,j,0]!=S[i,j,0]:
                                pts=[(50+j*500/9,10+i*500/9),(50+(j+1)*500/9,10+i*500/9),(50+(j+1)*500/9,10+(i+1)*500/9),(50+j*500/9,10+(i+1)*500/9)]
                                canvas.create_polygon(pts,outline="red",fill='')
        canvas.pack()
        fenetre.mainloop()
        

def Solution():
        """
        La fonction Solution() affiche la fenêtre de solution en plus de la fenêtre courante.
        """
        global T,fenetre2,canvas2
        fenetre2=Tk()
        canvas2=Canvas(fenetre2,width=600,height=600,background="gray99")
        Quitter=Button(fenetre2,text="Quitter",command=fenetre2.destroy)
        Quitter.place(relx=0.45,rely=0.88)
        Affichage2(Resolution(T[:,:,0]))
        canvas2.pack()
        fenetre2.mainloop()

def SolutionJeu():
        """
        La fonction SolutionJeu() affiche la fenêtre de solution en plus de la fenêtre courante.
        """
        global S,fenetre2,canvas2
        fenetre2=Tk()
        canvas2=Canvas(fenetre2,width=600,height=600,background="gray99")
        Quitter=Button(fenetre2,text="Quitter",command=fenetre2.destroy)
        Quitter.place(relx=0.45,rely=0.88)
        Affichage2(S)
        canvas2.pack()
        fenetre2.mainloop()     
 

BoutonChoixGrille=Button(root, text="Choisir une grille",command=ChoixGrille)
BoutonChoixGrille.place(relx = 0.25, rely=0.65)
BoutonEntrerGrille=Button(root, text="Entrer une grille",command=EntrerGrille)
BoutonEntrerGrille.place(relx = 0.60, rely=0.65)
root.mainloop()


## Réalisé par Julien Michel, Sébastien Cosquer et Apolline Mezzadri
