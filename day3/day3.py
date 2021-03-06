from collections import defaultdict

with open("input3") as f:
    lineas = f.read().splitlines()

puntos = defaultdict(list)
i = 0
for l in lineas:
    movimientos = l.split(",")
    x = 0
    y = 0
    #puntos[i].append((x,y))

    for m in movimientos:
        unidad = int(m[1:])
        if   "R" in m:
            for u in range(1,unidad+1):
                x += 1
                puntos[i].append((x,y))

        elif "L" in m:
            for u in range(1,unidad+1):
                x -= 1
                puntos[i].append((x,y))


        elif "U" in m:
            for u in range(1,unidad+1):
                y += 1
                puntos[i].append((x,y))


        elif "D" in m:
            for u in range(1,unidad+1):
                y -= 1
                puntos[i].append((x,y))

    i = i + 1

res = set(puntos[0]) & set(puntos[1])


#PART 1
minx = min([abs(punto[0]) + abs(punto[1]) for punto in res])

print(minx) 

#PART 2
minx = min([puntos[0].index(punto) + puntos[1].index(punto) + 2 for punto in res])

print(minx)
    

