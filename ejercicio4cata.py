print("inegres los partido ganado,empatados y perdidos");

ganado=int(input("partidos ganados "))
perdido=int(input("partidos perdidos "))
empatado=int(input("partidos empatados"))

tg=ganado*3
tp=perdido*0
te=empatado*1

puntaje=tg+tp+te

print("puntaje total de partidos ",puntaje)