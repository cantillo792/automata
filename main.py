##from ventana.ventana import Ventana
##import threading

##ventana = Ventana()
##ventana.raiz.mainloop()

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("SAY")
    audio = r.listen(source)
    print("TIME OVER")


print("TEXT:  "+r.recognize_google(audio, language='es-es'))