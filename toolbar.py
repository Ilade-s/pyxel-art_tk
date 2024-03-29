from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

class Toolbar(LabelFrame):
    def __init__(self, master) -> None:
        self.current_color = "#000000"
        super().__init__(master, background="#292D3E",
                         relief=SOLID, text="Barre d'outils", foreground="white")
        self.create_widgets()
        self.place(relx=0, rely=0, relheight=1, relwidth=.25)
    
    def create_widgets(self):
        def choose_color():
            color = colorchooser.askcolor()[1]
            if not color:
                self.current_color = "#000000"
            else:
                self.current_color = color
            color_button['bg'] = color
        
        def set_background():
            color = colorchooser.askcolor()[1]
            if not color:
                color = self.master.DrawingScene.bg_color
            self.master.DrawingScene.set_background(color)
            bg_button['bg'] = color
        
        def reset_drawing():
            self.master.DrawingScene.reset_drawing()
            bg_button['bg'] = "#ffffff"
        
        def change_binding(event):
            if event.widget.get() == 'click':
                binding = 1
            else:
                binding = 0
            self.master.DrawingScene.set_binding(binding)

        color_button = Button(self, text='Choose color', command=choose_color, foreground='#ffffff', background='#000000')
        color_button.pack(pady=10, ipadx=5, ipady=5)

        bg_button = Button(self, text='Set background', command=set_background)
        bg_button.pack(pady=10, ipadx=5, ipady=5)

        reset_button = Button(self, text='Reset drawing', command=reset_drawing)
        reset_button.pack(pady=10, ipadx=5, ipady=5)

        tool_box = ttk.Combobox(self, state='readonly', values=('brush', 'click'))
        tool_box.current(0)
        tool_box.bind('<<ComboboxSelected>>', change_binding)
        tool_box.pack(pady=10, ipadx=5, ipady=5)