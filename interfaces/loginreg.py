from interfaces.pantallaPrincipal import pantallaPrincipal
from interfaces.pantallaLeds import Leds
from models.systemdb import Pydb
from tkinter import *
from tkinter import ttk, messagebox

class main (Tk):
    
    modoDefault = 'login'
    database = Pydb()
    def __init__(self):
        super().__init__()  
        self.title("Proyecto Incubadora")
        self.geometry("900x500")
        self.config(bg="blue")   
        self.imagenframe = PhotoImage(file="assets/Fondoprincipal.png")
        self.frame_imagen = Frame(self)
        self.frame_login = Frame(self, bg="#ffffff")

        self.frame_imagen.place(x=0,y=0,width=450,height=500)
        self.frame_login.place(x=450,y=0,width=450,height=500)
        
        imagen_frame = Label(self.frame_imagen, image=self.imagenframe)
        imagen_frame.pack()

        #widgets de la ventana
        Label(self.frame_login, text="Bienvenido Nuevamente", font=("Arial",25)).pack(anchor=CENTER, pady=20)
        Label(self.frame_login, text="Ingresa tu credenciales para continuar",font=20).pack(anchor=CENTER)

        #Widgets del Login
        self.titleCorreo = Label(self.frame_login, text="Correo Electronico:")
        self.InCorreo = Entry(self.frame_login, width=40)
        self.titleContrasena = Label(self.frame_login, text="Contraseña:")
        self.InContrasena = Entry(self.frame_login, width=40, show="*")
        self.botonLogin = Button(self.frame_login,
                text='Iniciar Sesión',
                foreground="#ffffff",
                background="#015fb6",
                font=('Arial',11),
                border=1,
                command=self.authUser)
        self.botonRegistro = Button(self.frame_login,
                text='Registrarme',
                foreground="#015fb6",
                background="#ffffff",
                font=('Arial',11),
                border=1,
                command=self.loadForms)
        
        #Widgets del registro
        self.botonRegresar = Button(self.frame_login,
                text='Regresar a Inicio de Sesión',
                foreground="#ffffff",
                background="#015fb6",
                font=('Arial',11),
                command=self.loadForms)
        self.titleContrasenac = Label(self.frame_login, text="Confirmar Contraseña:")
        self.InContrasenac = Entry(self.frame_login, width=40, show="*")
        self.loadForms()
        

    def loadForms(self):
        if self.modoDefault == 'login': 
            self.titleCorreo.place(y=133, x=100)     
            self.InCorreo.pack(pady=50)        
            self.titleContrasena.place(y=200, x=100)  
            self.InContrasena.pack()     
            self.botonLogin.place(y=270, x=240)
            self.botonRegistro.place(y=270, x=100)
            self.botonRegresar.place_forget()
            self.titleContrasenac.place_forget()
            self.InContrasenac.pack_forget()
            self.botonRegistro.config(command=self.loadForms)
            self.modoDefault = 'registro'
        elif self.modoDefault == 'registro':
            # self.titleCorreo.place_forget()
            # self.InCorreo.pack_forget()
            # self.titleContrasena.place_forget()
            # self.InContrasena.pack_forget()
            self.botonLogin.place_forget()
            self.titleContrasenac.place(y=270, x=100)  
            self.InContrasenac.pack(pady=50)
            self.botonRegistro.config(command=self.authUser)
            self.botonRegistro.place(y=400, x=70)
            self.botonRegresar.place(y=400, x=200)
            self.modoDefault = 'login'
            

    def authUser(self):
        if self.modoDefault == 'registro':
            correo = self.InCorreo.get()
            contrasena = self.InContrasena.get()
            if correo == '' and contrasena == '':
                 messagebox.showerror(title='Proyecto Incubadora', message='No puedes dejar el campo correo electronico y contrasena vacio')
                
            elif contrasena == "":
                messagebox.showerror(title='Proyecto Incubadora', message='No puedes dejar el campo contrasena vacio')
            elif correo == '':
                messagebox.showerror(title='Proyecto Incubadora', message='No puedes dejar el campo correo electronico vacio')
            else:
                vef = self.database.verificar_usuario(correo,contrasena)
                if vef:
                    print('Vamos a iniciar sesion '+ correo +' '+contrasena)
                    messagebox.showinfo(title='Proyecto Incubadora', message='Has iniciado sesion correctamente')
                    self.destroy()
                    succes= pantallaPrincipal(vef)
                    succes.mainloop()
                else:
                    messagebox.showerror(title="Proyecto Incubadora", message='Correo o contrasena incorrectos')
        elif self.modoDefault == 'login':
            correo = self.InCorreo.get()
            contrasena = self.InContrasena.get()
            contrasenac = self.InContrasenac.get()
            if contrasena == contrasenac:
                self.database.registrar_usuario(correo, contrasena)
                print('Vamos a crear una cuenta')
                messagebox.showinfo(title='Proyecto Incubadora', message='Te has registrado exitosamente, ahora inicia sesion')
                self.loadForms()
            else:
                messagebox.showerror(title='Proyecto Incubadora', message='Las contrasenas no coinciden')

