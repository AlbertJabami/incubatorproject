from tkinter import *
from tkinter import ttk, Menu, messagebox
from PIL import Image, ImageTk

class Leds(Toplevel):
    estadoboton = True
    estadoarduino = True
    def __init__(self):
        super().__init__()
        self.title("Proyecto Incubadora | Leds")
        self.geometry("700x400")
        self.resizable(0,0)
        self.imagenframe = PhotoImage(file="assets/0000.png")
        self.frame_Leds = Frame(self,background="#283f9b")
        self.frame_funcionLeds=Frame(self,bg="#ffffff")
        self.frame_Leds.place(x=0,y=0,width=350,height=400)
        self.frame_funcionLeds.place(x=350,y=0,width=350,height=400)
        Label(self.frame_Leds, text="Previsualizacion de leds",font=('Arial',14,"bold"),background="#283f9b",fg="#ffffff").place(y=120,x=60)
        self.imagen_led = Label(self.frame_Leds, image=self.imagenframe,background="#283f9b")
        self.imagen_led.place(y=160,x=50)
        Label(self.frame_funcionLeds, text="Configuracion de los leds",
              font=("Arial",14,"bold"),bg="#ffffff",fg="#283f9b").pack(pady=20)
        Label(self.frame_funcionLeds,text="Selecciona los leds a usar:",
              font=("Arial",11,"bold"),bg="#ffffff",fg="#283f9b").pack(pady=20)
        
        
        #Variable de los leds
        self.led1_var = IntVar()
        self.led2_var = IntVar()
        self.led3_var = IntVar()
        self.led4_var = IntVar()
        #Leds de la interfaz
        self.led1 = Checkbutton(self.frame_funcionLeds, text="1", font=("Arial",11,"bold"),bg="#ffffff" ,variable=self.led1_var)
        self.led2 = Checkbutton(self.frame_funcionLeds, text="2", font=("Arial",11,"bold"),bg="#ffffff" ,variable=self.led2_var)
        self.led3 = Checkbutton(self.frame_funcionLeds, text="3", font=("Arial",11,"bold"),bg="#ffffff" ,variable=self.led3_var)
        self.led4 = Checkbutton(self.frame_funcionLeds, text="4", font=("Arial",11,"bold"),bg="#ffffff" ,variable=self.led4_var)
        #Mostrar los leds
        self.led1.place(y=120, x=60)
        self.led2.place(y=120, x=120)
        self.led3.place(y=120, x=180)
        self.led4.place(y=120, x=240)
        Label(self.frame_funcionLeds,text="Selecciona la funcion para los leds:",
              font=("Arial",11,"bold"),bg="#ffffff", fg="#283f9b").pack(pady=40)
        Label(self.frame_funcionLeds, text="Conexión del Arduino:",
              font=("Arial",11,"bold"),bg="#ffffff",fg="#283f9b").pack(pady=10)
        #Variable del combobox
        self.combox = StringVar()
        #Combobox Interfaz
        self.comboopciones = ttk.Combobox(self.frame_funcionLeds,state="readonly",textvariable=self.combox,
                     values=['Encender', 'Parpadeo','Encender desde izquierda','Encender desde derecha','Apagar'])
        self.comboopciones.place(y=210, x=70, width=220, height=25)
        #Arduino Widgets
        self.botonarduino = Button(self.frame_funcionLeds,
                                   text="Conectar Arduino",
                                   fg="#ffffff",
                                   bg="#2ed32a",
                                   border=0,
                                   font=("Arial",11,"bold"),
                                   )
        self.botonarduino.place(x=110, y=280)
        #Boton de inicio
        self.imagenplay = PhotoImage(file="assets/play32.png")
        self.imagenstop = PhotoImage(file="assets/stop16.png")
        self.botonaccion = Button(self.frame_funcionLeds,
                                  image=self.imagenplay,
                                  fg="#ffffff",
                                  bg="#2ed32a",
                                  font=("Arial",12,'bold'),
                                  width=32,height=32,
                                  border=0,
                                  command=self.Ledstart)
        self.botonaccion.place(x=300, y=350)
    def Ledstart(self):
        confirmacion = False
        modo = self.combox.get()
        leds = str(self.led1_var.get())+str(self.led2_var.get())+str(self.led3_var.get())+str(self.led4_var.get())
        if self.estadoboton:
            if modo == "":
                messagebox.showerror(title="Error", message="No has seleccionado un modo para los leds")
            elif modo == "Encender":
                print(modo)
                print(leds)
                self.imagenmostrar= PhotoImage(file="assets/"+leds+".png")
                self.imagen_led.config(image=self.imagenmostrar)
                confirmacion = True
            elif modo == "Parpadeo":
                print(modo)
                gif_path = "assets/leds/Parpadeo/"+ leds + ".gif"
                print(gif_path)
                self.frames_num = 2
                self.gif_path = gif_path
                self.frames = [PhotoImage(file=self.gif_path, format=f"gif -index {i}") for i in range(self.frames_num)]
                self.current_frame = 0
                self.animacionled = True
                self.update_frame()
                confirmacion = True

            if confirmacion == True:
                self.botonaccion.config(text="Detener",
                                fg="#ffffff",
                                bg="#d32a2a",
                                image=self.imagenstop)
                for led in [self.led1,self.led2,self.led3,self.led4,self.comboopciones,self.botonarduino]:
                    led.config(state="disable")
                self.estadoboton = False
        else:
            self.botonaccion.config(text="Comenzar",
                                    fg="#ffffff",
                                    bg="#2ed32a",
                                    image=self.imagenplay)
            for led in [self.led1,self.led2,self.led3,self.led4,self.comboopciones,self.botonarduino]:
                led.config(state="normal")
            self.imagenmostrar= PhotoImage(file="assets/0000.png")
            self.imagen_led.config(image=self.imagenmostrar)
            self.animacionled = False
            self.estadoboton = True 

    def update_frame(self):
        """Actualiza la imagen del gif"""
        if self.animacionled:
            frame = self.frames[self.current_frame]
            self.current_frame = (self.current_frame + 1) % self.frames_num
            self.imagen_led.configure(image=frame)
            self.imagen_led.after(1000, self.update_frame) 
# app = Leds()
# app.mainloop() 