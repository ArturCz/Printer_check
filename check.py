import pyttsx3
import time
from tkinter import messagebox

def sprawdz_drukarke():
    podlaczona = True
    toner = True
    tusz = True

    return podlaczona, toner, tusz

def informuj_o_stanie_drukarki(podlaczona, toner, tusz):
    engine = pyttsx3.init()
    if not podlaczona:
        messagebox.showerror("Błąd", "Uwaga! Drukarka nie jest podłączona.")
    else:
        if toner:
            messagebox.showerror("Błąd", "Uwaga! Brakuje tonera w drukarce.")
        if tusz:
            messagebox.showerror("Błąd", "Uwaga! Brakuje tuszu w drukarce.")

if __name__ == "__main__":
    while True:
        podlaczona, toner, tusz = sprawdz_drukarke()
        informuj_o_stanie_drukarki(podlaczona, toner, tusz)
        time.sleep(60)
