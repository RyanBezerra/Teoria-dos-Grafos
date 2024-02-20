import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter", "TKinterModernThemes"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CalculadoraDeFunções",
    version="1.0",
    description="Calcula a área e o perémetro de algumas figuras geometricas planas",
    options= {"build_exe": build_exe_options},
    executables= [Executable("CalculadoraDeFunções.py", base=base)]
)
