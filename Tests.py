from collections import deque
data = [(0,0.657)]
liste = []
nombre = 1000000
tests = 100
for i in range(nombre) :
    liste.append(i)
doubleliste = deque(liste)
for i in range(tests) :
    del doubleliste[nombre//2]