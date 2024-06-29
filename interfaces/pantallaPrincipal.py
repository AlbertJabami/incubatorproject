from tkinter import *
from tkinter import ttk, Menu
from interfaces.pantallaLeds import Leds
from interfaces.pantallaMotor import Motor

class pantallaPrincipal(Tk):

    def __init__(self, usuario):
        super().__init__()
        self. usuariosesion = usuario
        self.title("Proyecto Incubadora")
        self.geometry("600x400")
        self.config(bg="#ffffff")
        self.resizable(0,0)
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
            command=self.Motor)
        menuprincipal.add_cascade(label="Modulos", menu=menuModulos)
        menuprincipal.add_command(label='Cerrar sesion', command=self.cerrarsesion)
        menuprincipal.add_command(label='Salir', command=self.salirprograma)
        self.bind_all("<Control-l>", self.Leds)
        
        Label(self,text="Bienvenido al sistema de incubadora",
              font=('Arial',14,"bold"),
              background="#ffffff",
              fg="#283f9b").pack(pady=15)
        Label(self,text="Para navegar por el sistema utiliza el menu que se encuentra en la parte superior",
              font=('Arial',10,"bold"),
              background="#ffffff",
              fg="#000000").pack(pady=1)
        Label(self,text="Has iniciado sesion correctamente, estas identificado como:",
              font=('Arial',12,"bold"),
              background="#ffffff",
              fg="#000000").pack(pady=14)
        Label(self,text="Correo: "+self.usuariosesion[1],
              font=('Arial',9,"bold"),
              background="#ffffff",
              fg="#000000").pack(pady=1)
        Label(self,text="Ultima vez que te conectaste: "+self.usuariosesion[2],
              font=('Arial',9,"bold"),
              background="#ffffff",
              fg="#000000").pack(pady=1)
        print(self.usuariosesion)
    
    def Leds(self):
        print("Estamos en leds")
        led = Leds()
        led.focus()
        led.grab_set()

    def Motor(self):
        print("Estamos en motor")
        motor = Motor()
        motor.focus()
        motor.grab_set()  
         
    def salirprograma(self):
        self.destroy()
    
    def cerrarsesion(self):
        self.destroy()
        from interfaces.loginreg import main  # Importación local para evitar circularidad
        main_instance = main()
        main_instance.mainloop()

if __name__ == "__main__":
    programa = pantallaPrincipal([1, 'albertq703@gmail.com', '2024-06-29 12:22:46'])
    programa.mainloop()