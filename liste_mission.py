from cProfile import label
# import mysql.connector
from subprocess import call  # Permet de faire appel à d'autre fenetre
import tkinter as tk
from tkinter import messagebox


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

# Titre de la page
title_label = tk.Label(form_frame, text="Liste des missions", background=color_3, fg=white, font=('Sans Serif', 25)
                       , borderwidth=3, relief='sunken')
# title_label.pack(fill='x', ipady=10)
title_label.pack(pady=20)
# title_label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=0)
# # # Ajouter une ligne vide pour espacer le titre des champs
# spacer = tk.Label(form_frame, bg=color_3)  # Hauteur de 2 lignes
# spacer.grid(row=1, column=0, columnspan=2, sticky="w")
#
# Champs du formulaire
# mission_label = tk.Label(app_connexion, text="Nom de la mission : ", font=("Helvetica", 12), bg=color_3, fg=white)
# # mission_label.grid(row=2, column=0, sticky="ew", padx=20, pady=20)
# mission_label.pack(anchor='w', padx=10, pady=10)
#

# Champ de saisie pour ajouter une nouvelle mission
mission_label = tk.Label(form_frame, text="Nouvelle mission : ", font=("Helvetica", 12), bg=color_3, fg=white)
mission_label.pack(side="left", padx=10, pady=10)

mission_entry = tk.Entry(form_frame, font=("Helvetica", 12), bd=2)
mission_entry.pack(side="left", padx=10, pady=10)

# Champ de saisie pour la ville
ville_label = tk.Label(form_frame, text="Ville : ", font=("Helvetica", 12), bg=color_3, fg=white)
ville_label.pack(side="left", padx=10, pady=10)

ville_entry = tk.Entry(form_frame, font=("Helvetica", 12), bd=2)
ville_entry.pack(side="left", padx=10, pady=10)

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

# Boucle principale, execution de l'interface
app_connexion.mainloop()
