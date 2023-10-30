from gtts import gTTS

archivo = open("libro.txt", "r", encoding="utf-8")
texto= archivo.read()
archivo.close()

tss = gTTS(text = texto,lang="es")
tss.save("audio_libro.mp3")