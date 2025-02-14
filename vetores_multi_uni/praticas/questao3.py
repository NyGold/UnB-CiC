inteiros = [int(i) for i in input().split()]
fatias = []

while True:
    fatia = input()
    
    if fatia == "0:0":
        break
    
    fatias.append(fatia)

for fat in fatias:
    fatI, fatF = [int(i) for i in fat.split(":")]

    print(inteiros[fatI:fatF])