from cProfile import label
from database import create_connection, create_mission_table, insert_mission
from subprocess import call
import tkinter as tk
from tkinter import messagebox, ttk

# Créer une connexion à la base de données
db_connection = create_connection()
# Créer la table Mission si elle n'existe pas
if db_connection:
    create_mission_table(db_connection)
    # Vous pouvez fermer la connexion ici ou la garder ouverte pour d'autres opérations


def ajouter():
    libele = libele_entry.get()
    description = description_entry.get()
    duree = duree_entry.get()

    try:
        insert_mission(db_connection, libele, description, duree)
        response = messagebox.askokcancel('', 'Mission ajoutée avec succès..\n\nVoulez-vous voir la liste des missions ?')
        if response:
            afficher_liste_missions()

        libele_entry.delete('0', 'end')
        description_entry.delete('0', 'end')
        duree_entry.delete('0', 'end')
    except Exception as e:
        messagebox.showerror('Erreur', str(e))


def afficher_liste_missions():
    # Code pour afficher l'interface de liste des missions
    liste_missions = tk.Toplevel(app_connexion)
    liste_missions.title("Liste des missions")
    # Ajoutez ici le code pour afficher la liste des missions dans cette nouvelle fenêtre


# Creation de l'interface principale
app_connexion = tk.Tk()

# Définition des couleurs
primary_color = "#6c63ff"
secondary_color = "#ffffff"
color_3 = "#091821"
white = "white"
orange = "#FF4500"

# Paramètre de l'interface
app_connexion.geometry("1350x700")
app_connexion.title("Logiciel de Gestion des Missions")
# app_connexion.resizable(width=False, height=False)  # ou (false false)
app_connexion.configure(background=color_3)  # Donner des propriétés css

# Créer un cadre pour le formulaire
form_frame = tk.Frame(app_connexion, bg=color_3, bd=2, relief="sunken")
# Centrer le cadre du formulaire
form_frame.pack(expand=True, fill="both", padx=20, pady=20)
# form_frame.place(relx=0.5, rely=0.5, anchor="center")

# Titre de la page
title_label = tk.Label(form_frame, text="Enregistrer une nouvelle mission", background=color_3, fg=white,
                       font=('Sans Serif', 25), borderwidth=3, relief='sunken')
# title_label.pack(fill='x', ipady=10)
# title_label.pack(pady=0, fill='x')

title_label.grid(row=0, column=0, columnspan=2, pady=20)


# Champ de saisie pour le libele de la mission
libele_label = tk.Label(form_frame, text="Libele de la mission : ", font=("Helvetica", 12), bg=color_3, fg=white)
# libele_label.pack(side="left", padx=10, pady=10)
libele_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

libele_entry = tk.Entry(form_frame, font=("Helvetica", 12), bd=2)
libele_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

# Champ de saisie pour la description
description_label = tk.Label(form_frame, text="Description : ", font=("Helvetica", 12), bg=color_3, fg=white)
description_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

description_entry = tk.Entry(form_frame, font=("Helvetica", 12), bd=2)
description_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

# Champ de saisie pour la durée
duree_label = tk.Label(form_frame, text="Durée : ", font=("Helvetica", 12), bg=color_3, fg=white)
duree_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

duree_entry = tk.Entry(form_frame, font=("Helvetica", 12), bd=2)
duree_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

# Bouton ou un événement pour appeler la fonction ajouter()
bouton_ajouter = tk.Button(form_frame, text="Ajouter", command=ajouter, bg=orange, fg=white)
bouton_ajouter.grid(row=4, column=1, sticky="w", padx=10, pady=10)

# mission_entry = tk.Entry(app_connexion, font=("Helvetica", 12), bd=2)
# mission_entry.pack(anchor='w', padx=15, pady=15)
# username_entry.insert(0, "ivan06")
#
# password_label = tk.Label(form_frame, text="Mot de passe :", font=("Helvetica", 12), bg=color_3, fg=white)
# password_label.grid(row=3, column=0, sticky="w", padx=20, pady=10)
# password_entry = tk.Entry(form_frame, font=("Helvetica", 12), show="*", bd=2)
# password_entry.grid(row=3, column=1, sticky="ew", padx=20, pady=10)
#
# login_button = tk.Button(form_frame, text="Connexion", bg=orange, fg=white, font=("Helvetica", 12), bd=2,
#                          command=se_conecter)
# login_button.grid(row=4, column=1, sticky="e", padx=20, pady=20)
#
# # Ajuster la taille du cadre form_frame
# form_frame.place(height=300)

# table = ttk.Treeview(app_connexion, columns=1, height=5, show='headings')
# table.place(x=500, y=150, width=790, height=450)
#
# # Entete de la BD
# table.heading(1, text='libele')
#
# # Dimension des colonnes
# table.column(1, width=50)
#
# maBase = mysql.connector.connect(host='localhost', user='root', password='', database='gestion_mission')
# meConnect = maBase.cursor()
# meConnect.execute(' select * from libele')
# for row in meConnect:
#     table.insert('', 'end', values=row)
#
# maBase.close()

# Boucle principale, execution de l'interface
app_connexion.mainloop()
