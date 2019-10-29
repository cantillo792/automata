from ventana.ventana import Ventana
import threading
import speech_recognition as sr
from tkinter import *

r = sr.Recognizer()

threads = []

ventana = Ventana()


def recon():
    while 1:
        with sr.Microphone() as source:
            print("SAY")
            audio = r.record(source, offset=0.5,duration=2)
            print("TIME OVER")

        try:
            texto = r.recognize_google(audio, language='es-es')
            print("TEXT:  "+texto)
            if(texto == "lento"):
                ventana.modo.set(1)
            elif texto=="rápido":
                ventana.modo.set(2)
            elif texto=="rapidez":
                ventana.modo.set(2)
            elif texto=="iniciar":
                ventana.validar()
        except:
            print("no reconocido")

reconocimiento = threading.Thread(target=recon, args=())
reconocimiento.setDaemon(True)
threads.append(reconocimiento)
reconocimiento.start()

ventana.raiz.mainloop()





