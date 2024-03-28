import tkinter as tk
from subprocess import call

app = tk.Tk()
app.title("Logiciel de Gestion des Missions")
app.geometry("800x600+300+100")


# Fonction pour ouvrir une autre fenêtre
def open_ajout_mission():
    call(["python", "ajout_mission.py"])


# Une autre fenetre
def fenetre():
    fene = tk.Toplevel()
    fene.title("Listes des Commandes")
    fene.geometry("600x400+300+100")
    fene.resizable(width=False, height=False)

    lb = tk.Label(fene, text="Commande1")
    lb2 = tk.Label(fene, text="Commande2")

    lb.grid()
    lb2.grid(row=0, column=1)


message_bienvenue = tk.Label(app, text="Bienvenue dans votre logiciel de gestion de missions", background="#091821",
                             fg="white", font=('Sans Serif', 25), borderwidth=3, relief='sunken')
message_bienvenue.pack(fill='both', ipady=20)

# Barre de menu
mainMenu = tk.Menu(app)

# Menu gestion des Missions
menu1 = tk.Menu(mainMenu, tearoff=0)
menu1.add_command(label="Ajouter une mission")
menu1.add_separator()
menu1.add_command(label="Liste des missions", command=open_ajout_mission)

# Menu gestion des Employés
menu2 = tk.Menu(mainMenu, tearoff=0)
menu2.add_command(label="Ajouter un employé")
menu2.add_separator()
menu2.add_command(label="Liste des employés")

# Menu gestion des Villes
menu3 = tk.Menu(mainMenu, tearoff=0)
menu3.add_command(label="Ajouter une ville")
menu3.add_separator()
menu3.add_command(label="Liste des villes")

# Menu gestion des Véhicules
menu4 = tk.Menu(mainMenu, tearoff=0)
menu4.add_command(label="Ajouter un véhicule")
menu4.add_separator()
menu4.add_command(label="Liste des véhicules")

mainMenu.add_cascade(label="Gestion des Missions", menu=menu1)
mainMenu.add_cascade(label="Gestion des Employés", menu=menu2)
mainMenu.add_cascade(label="Gestion des Villes", menu=menu3)
mainMenu.add_cascade(label="Gestion des Véhicules", menu=menu4)
mainMenu.add_cascade(label="Quitter", command=app.quit)

# On attache le menu à la fenêtre principale
app.config(menu=mainMenu)
app.mainloop()
