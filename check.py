import pyttsx3
import time

def sprawdz_drukarke():
    podlaczona = True
    toner = True
    tusz = True

    return podlaczona, toner, tusz

def informuj_o_stanie_drukarki(podlaczona, toner, tusz):
    engine = pyttsx3.init()
    if not podlaczona:
        engine.say("Uwaga! Drukarka nie jest podłączona.")
    else:
        if not toner:
            engine.say("Uwaga! Brakuje tonera w drukarce.")
        if not tusz:
            engine.say("Uwaga! Brakuje tuszu w drukarce.")
        if toner and tusz:
            engine.say("Drukarka jest gotowa do pracy.")
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        podlaczona, toner, tusz = sprawdz_drukarke()
        informuj_o_stanie_drukarki(podlaczona, toner, tusz)
        # Odczekaj 60 sekund (1 minuta) przed ponownym sprawdzeniem
        time.sleep(60)
