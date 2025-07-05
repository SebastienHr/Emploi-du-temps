import tkinter 
from tkinter import * 
import time 
from datetime import datetime 


# petite application pour afficher complètement la date , entre la date et l'application va compléter le jour


# decription des variables 

""" 
	j = indice du jour
	m = indice de mois 
	a = annee de la date inserée
	na = nombre de année entre l'année de la date inserée et l'année initial 1925
	nbjm = nombre de jours dans un mois 
	ji,mi,ai = jour, moi, année de la date entrée 

"""

j=0
m=0
ji=0
mi=0
ai=0
na=0
nbjm=0

lst_jours = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche'] # liste jour* 

lst1_nbjm = [31,28,31,30,31,30,31,31,30,31,30,31]
lst2_nbjm = [31,29,31,30,31,30,31,31,30,31,30,31] # année bissextile 

# j = 3 # Jeudi 1 Janvier 1925 
j = 4 # vendredi 1 janvier 2021


fen = Tk()
fen.title('Le Jour')
fen.geometry("240x220")
var_date = StringVar()
aff = StringVar()
Label(fen,text='').pack()
Label(fen,text='Entrer la date,\n on va vous donner le jour').pack()
Label(fen,text='',width=30).pack()
Entry(fen, textvariable=var_date, width=20,bg='cyan').pack()
var_date.set('31-12-2021')
Label(fen,text='').pack()
aff_label = Label(fen, textvariable=aff,width=20).pack()
aff.set('date complete')
Label(fen,text='').pack()
Button(fen, text="valider",width=10,command=lambda:afficher()).pack()

Label(fen,text='').pack()

def decomposition():
	global ji,mi,ai
	dti = var_date.get() # dti : date inseréé
	dti = dti.split('-')
	ji,mi,ai = int(dti[0]),int(dti[1]),int(dti[2])
	


def jour_indice():	
	global ji,ai, mi
	na = ai - 1925
	j=3
	past = True
	lst0_nbjm = []
	present = False

	for n in range(na):
		a_suivant = 1926 + n 
		# print(a_suivant)
		if(a_suivant%4==0):
			lst0_nbjm = lst2_nbjm 
			# print('année bissextile')		
			
		else : 
			lst0_nbjm = lst1_nbjm 
	 	
		for m in range(12): 
			for nj  in range(lst0_nbjm[m]) :
				if present == False : 
					if j<6 : 
						j+= 1 
					else : 
						j=0 	
				if(a_suivant==ai and m == mi-1 and nj == ji-1):
					present = True
		
	aff.set(lst_jours[j])
	j = 0 


def afficher():
	decomposition()
	jour_indice()
	

	

fen.mainloop()