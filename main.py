"""
Application tkinter permettant de dessiner (dans un style pixel art) des images (sprites...)
Devra également permettre d'utiliser des images prééxistantes (avec drag and drop ?)
"""
from Globals import show_version, __VERSION__, x, y
from drawing import * # scène de dessin
from toolbar import * # barre d'outils (choix de couleur...)
from menu import * # menu pour choix de fichier/sauvegarde

class TopLevel(Tk):
    def __init__(self, x=x, y=y) -> None:
        super().__init__()
        self.iconphoto(True, PhotoImage(file="Assets/pen-tool.png"))
        self.file = None
        self.title(
            f"Pyxel art app v{__VERSION__} : Nouveau fichier")
        self.geometry("{}x{}".format(x, y))
        # Placement des Frames
        self.setup_frames()

    def setup_frames(self):
        print("Placement Frames...")
        # Placement Frames (initialisation des classes)
        print("Création zone de dessin...")
        self.DrawingScene = DrawingScene(self)
        print("Création barre d'outils...")
        self.Toolbar = Toolbar(self)
        print("Création menu...")
        self.Menu = Menubar(self)
        self.config(menu=self.Menu)

def main():
    show_version() # affichage info prog
    # Création fenêtre
    app = TopLevel()
    app.mainloop()

if __name__ == '__main__':
    main()