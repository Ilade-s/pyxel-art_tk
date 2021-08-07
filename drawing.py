"""
Frame qui permet de dessiner
L'image est représentée en grid de pixels
"""
from tkinter import *
from tkinter import ttk
from Globals import x as win_x, y as win_y

class DrawingScene(Frame):
    def __init__(self, master) -> None:
        self.bg_color = '#ffffff'
        self.bindings = []
        super().__init__(master, background="#A8B8FF", relief=RAISED)
        self.create_grid()
        self.place(relx=.25, rely=0, relheight=1, relwidth=.75)
    
    def create_grid(self):
        """
        Place les labels et initialise les actions
        """
        if not self.master.file:
            self.img_width = 50
            self.img_height = 50
        else:
            pass
            # TODO

        self.cells = [['' for y in range(self.img_height)] for x in range(self.img_width)]
        for x in range(self.img_width):
            for y in range(self.img_height):
                w = Label(self, borderwidth=0.5, relief=SOLID,
                          bg='#ffffff')         
                self.cells[x][y] = w
                self.cells[x][y].grid(row=x, column=y, 
                    ipadx=win_x*.75/self.img_width/2-2, ipady=win_y*.9/self.img_height/2-2)
        self.set_binding()
    
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
    
    def set_binding(self, bind=0):
        """
        bind : int : 0 for brush ; 1 for click
        """
        def click_pixel(event):
            event.widget['bg'] = self.master.Toolbar.current_color
        if not self.bindings:    
            binded_labels = 0
            self.bindings = [['' for y in range(self.img_height)] for x in range(self.img_width)]
        else:
            binded_labels = 1
        for x in range(self.img_width):
            for y in range(self.img_height):
                if bind:
                    if binded_labels:
                        self.cells[x][y].unbind('<Enter>', self.bindings[x][y])
                    self.bindings[x][y] = self.cells[x][y].bind('<1>', click_pixel) 
                else:    
                    if binded_labels:
                        self.cells[x][y].unbind('<1>', self.bindings[x][y])
                    self.bindings[x][y] = self.cells[x][y].bind('<Enter>', click_pixel)  