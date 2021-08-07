"""
Frame qui permet de dessiner
L'image est représentée en grid de pixels
"""
from tkinter import *
from tkinter import ttk, colorchooser
from Globals import x as win_x, y as win_y

class DrawingScene(Frame):
    def __init__(self, master) -> None:
        self.bg_color = '#ffffff'
        super().__init__(master, background="#A8B8FF", relief=RAISED)
        self.create_grid()
        self.place(relx=.25, rely=0, relheight=1, relwidth=.75)
    
    def create_grid(self):
        """
        Place les labels et initialise les actions
        """
        if not self.master.file:
            width = 50
            height = 50
        else:
            pass
            # TODO

        def click_pixel(event):
            event.widget['bg'] = self.master.Toolbar.current_color

        self.cells = [['' for y in range(height)] for x in range(width)]
        for x in range(width):
            for y in range(height):
                w = Label(self, borderwidth=0.5, relief=SOLID,
                          bg='#ffffff') 
                w.bind('<Enter>', click_pixel) 
                #w.bind('<B1-Motion>', click_pixel)          
                self.cells[x][y] = w
                self.cells[x][y].grid(row=x, column=y, 
                    ipadx=win_x*.75/width, ipady=win_y/height)
    
    def set_background(self, color):
        """
        remplace tout les pixels blancs par la couleur donnée
        """
        for line in self.cells:
            for cell in line:
                if cell['bg'] == self.bg_color:
                    cell['bg'] = color
        self.bg_color = color
    
    def reset_drawing(self):
        for line in self.cells:
            for cell in line:
                cell['bg'] = '#ffffff'
        self.bg_color = '#ffffff'