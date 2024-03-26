import tkinter as tk
from tkinter import ttk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Se Connecter - Vito")

# Définir les couleurs
primary_color = "#6c63ff"
secondary_color = "#ffffff"

# Configurer la fenêtre
root.geometry("800x500")
root.configure(bg=primary_color)

# Créer un cadre pour le formulaire
form_frame = ttk.Frame(root, padding=20)
form_frame.pack(pady=50)

# Créer les champs du formulaire
username_label = ttk.Label(form_frame, text="Nom d'utilisateur :", font=("Helvetica", 14))
username_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
username_entry = ttk.Entry(form_frame, font=("Helvetica", 14))
username_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
username_entry.insert(0, "Ivan")

password_label = ttk.Label(form_frame, text="Mot de passe :", font=("Helvetica", 14))
password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
password_entry = ttk.Entry(form_frame, font=("Helvetica", 14), show="*")
password_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# Créer le bouton de connexion
login_button = ttk.Button(form_frame, text="Connexion", command=None)
login_button.grid(row=2, column=1, sticky="e", padx=5, pady=10)

# Créer un cadre pour le contenu supplémentaire
content_frame = ttk.Frame(root, padding=20)
content_frame.pack(fill="both", expand=True)

# Ajouter l'image et le texte
# image = tk.PhotoImage(file="cars.png")
# image_label = ttk.Label(content_frame, image=image)
# image_label.pack(pady=20)

title_label = ttk.Label(content_frame, text="Vito", font=("Helvetica", 24, "bold"), foreground=secondary_color)
title_label.pack(pady=10)

description_label = ttk.Label(content_frame, text="Gérez vos informations en toute simplicité", font=("Helvetica", 16), foreground=secondary_color, wraplength=400)
description_label.pack(pady=10)

# Démarrer la boucle principale
root.mainloop()