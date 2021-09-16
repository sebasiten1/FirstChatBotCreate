#!/usr/bin/python3
from tkinter import *
import webbrowser


def open_ARIS_chanel():
    webbrowser.open_new("http://127.0.0.1:5000/")


# Creer une premmiere fenetre
window = Tk()

# personaliser cette fenetre
window.title("A.R.I.S")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("@/home/seb/chat-bots_first_part/img/IA_ARIS.XBM")
window.config(background='#9dd4d4')

# creer la frame
frame = Frame(window, bg='#9dd4d4', bd=1, relief=SUNKEN)

# ajout d'un premier texte
label_title = Label(frame, text="Bienvenue sur l'interface d'A.R.I.S", font=(
    "Courrier", 40), bg='#9dd4d4', fg='white')
label_title.pack()

# ajouter un bouton
bot_button = Button(frame, text="ouvrir A.R.I.S", font=(
    "Courrier", 25), bg='white', fg='#9dd4d4', command=open_ARIS_chanel)
bot_button.pack()

# ajouter
frame.pack(expand=YES)

# affichage
window.mainloop()
