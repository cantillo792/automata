from ventana.ventana import Ventana
import threading
import speech_recognition as sr
from tkinter import *
import time

#Inicializar ventana
ventana = Ventana()

#Inicializar reconocimiento de voz
r = sr.Recognizer()


def reconocer():
    while 1:
        with sr.Microphone() as source:
            print("Escuchando")
            ventana.raiz.title("Automata de pila - Escuchando")
            audio = r.record(source, offset=0.05,duration=2.15)
        try:
            texto = r.recognize_google(audio, language='es-es')
            print("Reconocido:  "+texto)
            if(texto == "lento"):
                ventana.modo.set(1)
            elif texto=="rápido":
                ventana.modo.set(2)
            elif texto=="rapidez":
                ventana.modo.set(2)
            elif texto=="iniciar":
                ventana.validar()
        except:
            ventana.raiz.title("Automata de pila - No reconocido")
            print("no reconocido")
            time.sleep(2.2)


#Reconocer en segundo plano
reconocimiento = threading.Thread(target=reconocer, args=())
reconocimiento.setDaemon(True)
reconocimiento.start()

#Abrir ventana
ventana.raiz.mainloop()





