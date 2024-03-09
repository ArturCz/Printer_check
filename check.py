import cups
import tkinter as tk
from tkinter import messagebox
import time


def sprawdz_drukarke(prefix):
    conn = cups.Connection()
    printers = conn.getPrinters()

    for printer in printers:
        if printer.startswith(prefix):
            printer_info = printers[printer]
            status = printer_info['printer-state']
            toner = printer_info.get('printer-toner-low', False)
            ink = printer_info.get('printer-ink-low', False)

            return True, status == 3, toner, ink

    return False, False, False, False


def informuj_o_stanie_drukarki():
    prefix = "HP"
    podlaczona, offline, toner, tusz = sprawdz_drukarke(prefix)

    if not podlaczona:
        messagebox.showerror("Błąd", "Uwaga! Drukarka nie jest podłączona.")
    elif offline:
        messagebox.showerror("Błąd", "Uwaga! Drukarka jest offline.")
    else:
        if toner:
            messagebox.showerror("Błąd", "Uwaga! Brakuje tonera w drukarce.")
        if tusz:
            messagebox.showerror("Błąd", "Uwaga! Brakuje tuszu w drukarce.")


def sprawdz_co_minute():
    while True:
        informuj_o_stanie_drukarki()
        time.sleep(15)



root = tk.Tk()
root.withdraw()
sprawdz_co_minute()
root.mainloop()
