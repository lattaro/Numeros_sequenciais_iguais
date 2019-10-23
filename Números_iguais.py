n = int(input("Digite um número inteiro"))

i = 10
x = 0
y = 0
decisão = False

while (n // i) > 0:
    x = n % i 
    n = n // i
    y = n % i
    if x == y:
        decisão = True
if decisão == True:
    print("sim")
else:
    print("não")