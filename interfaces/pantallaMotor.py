from tkinter import *
from tkinter import messagebox
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Motor(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Incubadora | Leds")
        self.geometry("700x550")
        self.resizable(0, 0)
        self.config(bg="#ffffff")
        self.x_values = [0]
        self.y_values = [0]

        fig, self.ax = plt.subplots(figsize=(4, 3))
        self.line, = self.ax.plot(self.x_values, self.y_values, label='Velocidad')
        self.ax.set_title('Gráfico velocidad del motor')
        self.ax.legend()
        Label(self, text="Manipulacion del motor",font=('Arial',15,"bold"),background="#ffffff",fg="#283f9b").pack(pady=10)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.scale = Scale(self, from_=0, to=8, orient=HORIZONTAL, length=300, 
                           tickinterval=2, bg="#ffffff", troughcolor="lightblue", 
                           width=20, sliderlength=20, label="Selecciona la velocidad:")
        self.scale.pack()
        self.update_button = Button(self, text="Actualizar",
                                    foreground="#ffffff",
                                    background="#015fb6",
                                    font=('Arial',11),
                                    border=1,command=self.actualizar_grafica)
        self.update_button.pack(pady=5)
         # Asocia el evento de cierre de la ventana con el método on_closing
    #     self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    # def on_closing(self):
    #     # Cierra la ventana y termina el programa
    #     self.destroy()
    #     sys.exit()

    def actualizar_grafica(self):
        try:
            nuevo_valor = float(self.scale.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un valor numérico.")
            return

        self.x_values.append(self.x_values[-1] + 1)
        self.y_values.append(nuevo_valor)
        self.line.set_data(self.x_values, self.y_values)

        # Actualiza los límites de los ejes
        self.ax.set_xlim(min(self.x_values), max(self.x_values))
        self.ax.set_ylim(min(self.y_values), max(self.y_values))

        self.canvas.draw()
