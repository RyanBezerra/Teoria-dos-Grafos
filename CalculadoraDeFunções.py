import TKinterModernThemes as TKMT
import tkinter as tk
import math

class App(TKMT.ThemedTKinterFrame):

    def textupdate(self, _var, _indx, _mode):

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

    def handleButton2Click(self):

        global Perímetro
        global Área

        if self.checkbox2.get() == True and self.optionmenuvar.get() == "Triângulo":
            print(PTriângulo)

        if self.checkbox2.get() == True and self.optionmenuvar.get() == "Quadrado":
            print(PQuadrado)

        if self.checkbox2.get() == True and self.optionmenuvar.get() == "Retângulo":
            print(PRetângulo)

        if self.checkbox2.get() == True and self.optionmenuvar.get() == "Paralelogramo":
            print(PParalelogramo)

        if self.checkbox2.get() == True and self.optionmenuvar.get() == "Losango":
            print(PLosango)

        if self.checkbox2.get() == True and self.optionmenuvar.get() == "Trapézio":
            print(PTrapézio)

        if self.checkbox2.get() == True and self.optionmenuvar.get() == "Círculo":
            print(PCírculo)

    def handleButtonClick(self):
        print("Opção escolhida:", self.optionmenuvar.get())

        escolha1.destroy()
        escolha2.destroy()
        escolha3.destroy()
        escolha4.destroy()

        if self.optionmenuvar.get() == "Triângulo":

            self.textinputvar = tk.StringVar()
            self.textinputvar.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar)
            self.textinputvar2 = tk.StringVar()
            self.textinputvar2.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar2)
            self.textinputvar3 = tk.StringVar()
            self.textinputvar3.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar3)

        if self.optionmenuvar.get() == "Quadrado":

            self.textinputvar = tk.StringVar()
            self.textinputvar.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar)

        if self.optionmenuvar.get() == "Retângulo":

            self.textinputvar = tk.StringVar()
            self.textinputvar.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar)
            self.textinputvar2 = tk.StringVar()
            self.textinputvar2.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar2)

        if self.optionmenuvar.get() == "Paralelogramo":

            self.textinputvar = tk.StringVar()
            self.textinputvar.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar)
            self.textinputvar2 = tk.StringVar()
            self.textinputvar2.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar2)

        if self.optionmenuvar.get() == "Losango":

            self.textinputvar = tk.StringVar()
            self.textinputvar.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar)

        if self.optionmenuvar.get() == "Trapézio":

            self.textinputvar = tk.StringVar()
            self.textinputvar.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar)
            self.textinputvar2 = tk.StringVar()
            self.textinputvar2.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar2)
            self.textinputvar3 = tk.StringVar()
            self.textinputvar3.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar3)
            self.textinputvar4 = tk.StringVar()
            self.textinputvar4.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar4)

        if self.optionmenuvar.get() == "Círculo":

            self.textinputvar = tk.StringVar()
            self.textinputvar.trace_add('write', self.textupdate)
            self.input_frame.Entry(self.textinputvar)

        self.input_frame.Button("Confirmar", self.handleButton2Click)

    def __init__(self):
        super().__init__("Funções", "park", "dark")

        global escolha1
        global escolha2
        global escolha3
        global escolha4

        self.option_menu_list = ["Triângulo", "Quadrado", "Retângulo", "Paralelogramo", "Losango", "Trapézio", "Círculo"]
        self.optionmenuvar = tk.StringVar(value=self.option_menu_list[0])
        self.input_frame = self.addLabelFrame("Menu:", rowspan=2)
        escolha1 = self.input_frame.OptionMenu(self.option_menu_list, self.optionmenuvar)
        
        self.checkbox1 = tk.BooleanVar()
        self.checkbox2 = tk.BooleanVar()
        self.togglebuttonvar = tk.BooleanVar()
        escolha2 = self.input_frame.Checkbutton("Perímetro", self.checkbox2)
        escolha3 = self.input_frame.Checkbutton("Área", self.checkbox1)

        escolha4 = self.input_frame.Button("Confirmar", self.handleButtonClick)

        self.run()

App()