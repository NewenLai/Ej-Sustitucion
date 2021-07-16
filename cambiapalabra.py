original = "tizas"
nueva = "yesos"

nombreF = "texto.txt"

f = open(nombreF, "r")

texto_original =  f.read()

f.close()


Nuevo_texto = texto_original.replace(original, nueva)

f = open(nombreF, "w")
f.write(Nuevo_texto)
f.close()
