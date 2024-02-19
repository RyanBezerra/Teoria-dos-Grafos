import TKinterModernThemes as TKMT
from TKinterModernThemes.WidgetFrame import Widget
import tkinter as tk
import math

math.pi = 3.14

class App(TKMT.ThemedTKinterFrame):

    global contador2ToF
    contador2ToF = False

    global contador
    contador = 0

    global contador1
    contador1 = 0

    global contador2
    contador2 = 0

    global contador3
    contador3 = 0

    def textupdate(self, _var, _indx, _mode):

        #Calculo do perimetro 

        if self.checkbox2.get() == True:

            if self.optionmenuvar.get() == "Triângulo":
                lado1_str = self.textinputvar.get()
                lado2_str = self.textinputvar2.get()
                lado3_str = self.textinputvar3.get()

                try:
                    lado1 = float(lado1_str)
                    lado2 = float(lado2_str)
                    lado3 = float(lado3_str)

                    global PTriângulo
                    PTriângulo = lado1 + lado2 + lado3 

                except ValueError:
                    return     

            if self.optionmenuvar.get() == "Quadrado":
                lado1_str = self.textinputvar.get()

                try:
                    lado1 = float(lado1_str)

                    global PQuadrado
                    PQuadrado = lado1 * 4

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Retângulo":
                lado1_str = self.textinputvar.get()
                lado2_str = self.textinputvar2.get()

                try:
                    lado1 = float(lado1_str)
                    lado2 = float(lado2_str)

                    global PRetângulo
                    PRetângulo = (2*lado1) + (2*lado2)

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Paralelogramo":
                lado1_str = self.textinputvar.get()
                lado2_str = self.textinputvar2.get()

                try:
                    lado1 = float(lado1_str)
                    lado2 = float(lado2_str)

                    global PParalelogramo
                    PParalelogramo = (2*lado1) + (2*lado2)

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Losango":
                lado1_str = self.textinputvar.get()

                try:
                    lado1 = float(lado1_str)

                    global PLosango
                    PLosango = lado1 * 4

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Trapézio":
                lado1_str = self.textinputvar.get()
                lado2_str = self.textinputvar2.get()
                lado3_str = self.textinputvar3.get()
                lado4_str = self.textinputvar4.get()

                try:
                    lado1 = float(lado1_str)
                    lado2 = float(lado2_str)
                    lado3 = float(lado3_str)
                    lado4 = float(lado4_str)

                    global PTrapézio
                    PTrapézio = lado1 + lado2 + lado3 + lado4

                except ValueError:
                    return 

            if self.optionmenuvar.get() == "Círculo":
                lado1_str = self.textinputvar.get()

                try:
                    lado1 = float(lado1_str)

                    global PCírculo
                    PCírculo = 2 * math.pi * lado1

                except ValueError:
                    return

        if self.checkbox1.get() == True:

            if self.optionmenuvar.get() == "Triângulo":
                base_str = self.textinputvar.get()
                altura_str = self.textinputvar2.get()

                try:
                    base = float(base_str)
                    altura = float(altura_str)

                    global ATriângulo
                    ATriângulo = (base * altura) / 2

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Quadrado":
                lado_str = self.textinputvar.get()

                try:
                    lado = float(lado_str)

                    global AQuadrado
                    AQuadrado = lado ** 2

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Retângulo":
                altura_str = self.textinputvar.get()
                base_str = self.textinputvar2.get()

                try:
                    altura = float(altura_str)
                    base = float(base_str)

                    global ARetângulo
                    ARetângulo = altura * base

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Paralelogramo":
                altura_str = self.textinputvar.get()
                base_str = self.textinputvar2.get()

                try:
                    altura = float(altura_str)
                    base = float(base_str)

                    global AParalelogramo
                    AParalelogramo = altura * base

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Losango":
                diagonalmaior_str = self.textinputvar.get()
                diagonalmenor_str = self.textinputvar2.get()

                try:
                    diagonalmaior = float(diagonalmaior_str)
                    diagonalmenor = float(diagonalmenor_str)

                    global ALosango
                    ALosango = (diagonalmaior * diagonalmenor) / 2

                except ValueError:
                    return

            if self.optionmenuvar.get() == "Trapézio":
                basemaior_str = self.textinputvar.get()
                basemenor_str = self.textinputvar2.get()
                altura_str = self.textinputvar3.get()

                try:
                    basemaior = float(basemaior_str)
                    basemenor = float(basemenor_str)
                    altura = float(altura_str)

                    global ATrapézio
                    ATrapézio = (basemaior + basemenor) * altura / 2

                except ValueError:
                    return   

            if self.optionmenuvar.get() == "Círculo":
                raio_str = self.textinputvar.get()

                try:
                    raio = float(raio_str)

                    global ACírculo
                    ACírculo = math.pi * raio ** 2

                except ValueError:
                    return  

    def handleButton2Click(self):

        global Perímetro
        global Área
        global contador
        global contador1
        global log
        global log1

        if self.checkbox2.get() == True:

            if contador >= 1:
                log.destroy()
                contador = contador - 1

            if self.checkbox2.get() == True and self.optionmenuvar.get() == "Triângulo":
                log = self.input_frame3.Text(f"Perímetro: {PTriângulo}")

            if self.checkbox2.get() == True and self.optionmenuvar.get() == "Quadrado":
                log = self.input_frame3.Text(f"Perímetro: {PQuadrado}")

            if self.checkbox2.get() == True and self.optionmenuvar.get() == "Retângulo":
                log = self.input_frame3.Text(f"Perímetro: {PRetângulo}")

            if self.checkbox2.get() == True and self.optionmenuvar.get() == "Paralelogramo":
                log = self.input_frame3.Text(f"Perímetro: {PParalelogramo}")

            if self.checkbox2.get() == True and self.optionmenuvar.get() == "Losango":
                log = self.input_frame3.Text(f"Perímetro: {PLosango}")

            if self.checkbox2.get() == True and self.optionmenuvar.get() == "Trapézio":
                log = self.input_frame3.Text(f"Perímetro: {PTrapézio}")

            if self.checkbox2.get() == True and self.optionmenuvar.get() == "Círculo":
                log = self.input_frame3.Text(f"Perímetro: {PCírculo}")

            contador = contador + 1

        if self.checkbox1.get() == True:

            if contador1 >= 1:
                log1.destroy()
                contador1 = contador1 - 1

            if self.checkbox1.get() == True and self.optionmenuvar.get() == "Triângulo":
                log1 = self.input_frame3.Text(f"Área: {ATriângulo}")

            if self.checkbox1.get() == True and self.optionmenuvar.get() == "Quadrado":
                log1 = self.input_frame3.Text(f"Área: {AQuadrado}")

            if self.checkbox1.get() == True and self.optionmenuvar.get() == "Retângulo":
                log1 = self.input_frame3.Text(f"Área: {ARetângulo}")

            if self.checkbox1.get() == True and self.optionmenuvar.get() == "Paralelogramo":
                log1 = self.input_frame3.Text(f"Área: {AParalelogramo}")

            if self.checkbox1.get() == True and self.optionmenuvar.get() == "Losango":
                log1 = self.input_frame3.Text(f"Área: {ALosango}")

            if self.checkbox1.get() == True and self.optionmenuvar.get() == "Trapézio":
                log1 = self.input_frame3.Text(f"Área: {ATrapézio}")

            if self.checkbox1.get() == True and self.optionmenuvar.get() == "Círculo":
                log1 = self.input_frame3.Text(f"Área: {ACírculo}")

            contador1 = contador1 + 1

    def handleButtonClick(self):

        global contador2
        global contador3
        global delete_entry
        global delete_buttons
        global delete_entry2
        global delete_buttons2

        if self.checkbox2.get() == True:

            if contador2 == 1:
                for entry in delete_entry:
                    print(entry)
                    entry.destroy()
                for button in delete_buttons:
                    button.destroy()

            if self.optionmenuvar.get() == "Triângulo":

                delete_entry = []
                delete_buttons = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar2))
                self.textinputvar3 = tk.StringVar()
                self.textinputvar3.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar3))

                delete_buttons.append(self.input_frame2.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Quadrado":

                delete_entry = []
                delete_buttons = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar))

                delete_buttons.append(self.input_frame2.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Retângulo":

                delete_entry = []
                delete_buttons = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar2))

                delete_buttons.append(self.input_frame2.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Paralelogramo":

                delete_entry = []
                delete_buttons = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar2))

                delete_buttons.append(self.input_frame2.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Losango":

                delete_entry = []
                delete_buttons = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar))

                delete_buttons.append(self.input_frame2.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Trapézio":

                delete_entry = []
                delete_buttons = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar2))
                self.textinputvar3 = tk.StringVar()
                self.textinputvar3.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar3))
                self.textinputvar4 = tk.StringVar()
                self.textinputvar4.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar4))

                delete_buttons.append(self.input_frame2.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Círculo":

                delete_entry = []
                delete_buttons = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry.append(self.input_frame2.Entry(self.textinputvar))

                delete_buttons.append(self.input_frame2.Button("Confirmar", self.handleButton2Click))

            contador2 = 1

        if self.checkbox1.get() == True:

            if contador3 == 1:
                for entry in delete_entry2:
                    print(entry)
                    entry.destroy()
                for button in delete_buttons2:
                    button.destroy()

            if self.optionmenuvar.get() == "Triângulo":

                delete_entry2 = []
                delete_buttons2 = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar2))

                delete_buttons2.append(self.input_frame4.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Quadrado":

                delete_entry2 = []
                delete_buttons2 = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar))

                delete_buttons2.append(self.input_frame4.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Retângulo":

                delete_entry2 = []
                delete_buttons2 = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar2))

                delete_buttons2.append(self.input_frame4.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Paralelogramo":

                delete_entry2 = []
                delete_buttons2 = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar2))

                delete_buttons2.append(self.input_frame4.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Losango":

                delete_entry2 = []
                delete_buttons2 = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar2))

                delete_buttons2.append(self.input_frame4.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Trapézio":

                delete_entry2 = []
                delete_buttons2 = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar))
                self.textinputvar2 = tk.StringVar()
                self.textinputvar2.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar2))
                self.textinputvar3 = tk.StringVar()
                self.textinputvar3.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar3))

                delete_buttons2.append(self.input_frame4.Button("Confirmar", self.handleButton2Click))

            if self.optionmenuvar.get() == "Círculo":

                delete_entry2 = []
                delete_buttons2 = []

                self.textinputvar = tk.StringVar()
                self.textinputvar.trace_add('write', self.textupdate)
                delete_entry2.append(self.input_frame4.Entry(self.textinputvar))

                delete_buttons2.append(self.input_frame4.Button("Confirmar", self.handleButton2Click))

            contador3 = 1

    def __init__(self):
        super().__init__("Funções", "park", "dark")

        self.input_frame3 = self.addLabelFrame("Log:", rowspan=1)
        self.input_frame3.Text("Resultados")

        self.nextCol()
        self.option_menu_list = ["Triângulo", "Quadrado", "Retângulo", "Paralelogramo", "Losango", "Trapézio", "Círculo"]
        self.optionmenuvar = tk.StringVar(value=self.option_menu_list[0])
        self.input_frame = self.addLabelFrame("Menu:", rowspan=1)

        self.input_frame.OptionMenu(self.option_menu_list, self.optionmenuvar)
        
        self.checkbox1 = tk.BooleanVar()
        self.checkbox2 = tk.BooleanVar()
        self.togglebuttonvar = tk.BooleanVar()
        self.input_frame.Checkbutton("Perímetro", self.checkbox2)
        self.input_frame.Checkbutton("Área", self.checkbox1)

        self.input_frame.Button("Confirmar", self.handleButtonClick)

        self.nextCol()
        self.input_frame2 = self.addLabelFrame("Perímetro:", rowspan=1)

        self.nextCol()
        self.input_frame4 = self.addLabelFrame("Área:", rowspan=1)

        self.run()

App()