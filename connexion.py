from subprocess import call  # Permet de faire appel à d'autre fenetre
import tkinter as tk
from tkinter import messagebox


# Fonction Se connecter
def se_conecter():
    username = username_entry.get()
    password = password_entry.get()

    if username == '' and password == '':
        messagebox.showerror("Erreur !!", "Veuillez entrez les bonnes informations")
        password_entry.delete("0", 'end')

    elif username == 'admin' and password == 'admin':
        messagebox.showinfo("Succès !!", "Bienvenue dans votre logiciel de gestion de missions")
        username_entry.delete('0', 'end')
        password_entry.delete('0', 'end')
        app_connexion.destroy()
        call(['python', 'main.py'])


# Creation de l'interface principale
app_connexion = tk.Tk()

# Définition des couleurs
primary_color = "#6c63ff"
secondary_color = "#ffffff"
color_3 = "#091821"
white = "white"
orange = "#FF4500"

# Paramètre de l'interface
app_connexion.geometry("800x500")
app_connexion.title("Se Connecter")
# app_connexion.resizable(width=False, height=False)  # ou (false false)
app_connexion.configure(background=color_3)  # Donner des propriétés css

# Créer un cadre pour le formulaire
form_frame = tk.Frame(app_connexion, bg=color_3, bd=2, relief="sunken")
# Centrer le cadre du formulaire
form_frame.place(relx=0.5, rely=0.5, anchor="center")

# Titre de la page
title_label = tk.Label(form_frame, text="Connectez Vous", background=color_3, fg=white, font=('Sans Serif', 25)
                       , borderwidth=3, relief='sunken')
title_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=0)  # ew permet d'étirer l'élément pour
# remplir tout l'espace

# # Ajouter une ligne vide pour espacer le titre des champs
spacer = tk.Label(form_frame, bg=color_3)  # Hauteur de 2 lignes
spacer.grid(row=1, column=0, columnspan=2, sticky="w")

# Champs du formulaire
username_label = tk.Label(form_frame, text="Nom d'utilisateur : ", font=("Helvetica", 12), bg=color_3, fg=white)
username_label.grid(row=2, column=0, sticky="w", padx=20, pady=20)
username_entry = tk.Entry(form_frame, font=("Helvetica", 12), bd=2)
username_entry.grid(row=2, column=1, sticky="ew", padx=20, pady=10)
username_entry.insert(0, "ivan06")

password_label = tk.Label(form_frame, text="Mot de passe :", font=("Helvetica", 12), bg=color_3, fg=white)
password_label.grid(row=3, column=0, sticky="w", padx=20, pady=10)
password_entry = tk.Entry(form_frame, font=("Helvetica", 12), show="*", bd=2)
password_entry.grid(row=3, column=1, sticky="ew", padx=20, pady=10)

login_button = tk.Button(form_frame, text="Connexion", bg=orange, fg=white, font=("Helvetica", 12), bd=2,
                         command=se_conecter)
login_button.grid(row=4, column=1, sticky="e", padx=20, pady=20)

# Ajuster la taille du cadre form_frame
form_frame.place(height=300)

# Boucle principale, execution de l'interface
app_connexion.mainloop()
