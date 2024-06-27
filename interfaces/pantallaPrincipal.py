from tkinter import *
from tkinter import ttk, Menu
from interfaces.pantallaLeds import Leds

class pantallaPrincipal(Tk):

    def __init__(self):
        super().__init__()
        self.title("Proyecto Incubadora")
        self.geometry("900x500")
        menuprincipal = Menu(self)
        self.config(menu=menuprincipal)
        menuModulos = Menu(menuprincipal,tearoff=False)
        self.icon_leds=PhotoImage(file="assets/luz-led.png")
        menuModulos.add_command(
            label="Leds",
            accelerator="Ctrl+L",
            image=self.icon_leds,
            compound=LEFT,
            command=self.Leds)
        menuModulos.add_command(
            label="Motor",
            accelerator="Ctrl+M",
            image=self.icon_leds,
            compound=LEFT,
            command=self.Leds)
        menuprincipal.add_cascade(label="Modulos", menu=menuModulos)
        self.bind_all("<Control-l>", self.Leds)
        Label(self,text="ASDDDD").pack()
    
    def Leds(self):
        print("Estamos en leds")
        led = Leds()
        led.focus()
        led.grab_set()