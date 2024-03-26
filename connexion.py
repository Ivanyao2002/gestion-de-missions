from subprocess import call  # Permet de faire appel à d'autre fenetre
import tkinter as tk

# Creation de l'interface
app_connexion = tk.Tk()


# Fonction permettant de centrer la fenetre
def center(pos_x, pos_y):
    x = mainapp.winfo_screenmmwidth()  # largeur de l'ecran, pos_x:largeur de la fenetre
    y = mainapp.winfo_screenmmheight()  # Hauteur de l'ecran, pos_y:hauteur
    centrer_x = (x // 2) - (pos_x // 2)  # calcul pour effectuer le centre de la largeur
    centrer_y = (y // 2) - (pos_y // 2)
    return f"{pos_x}x{pos_y}+{x}+{y}"


# Paramètre de l'interface
app_connexion.geometry("600x400+400+100")  # center(800,600)
app_connexion.title("Se connecter")
app_connexion.resizable(width=False, height=False)  # ou (false false)
app_connexion.configure(background='#091821')  # Donner des propriétés css

#Titre de la page
Label_ap = tk.Label(app_connexion, text="Connectez vous")

# Boucle principale, execution de l'interface
app_connexion.mainloop()
