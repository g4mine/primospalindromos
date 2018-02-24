rng = raw_input('Ate qual numero deseja fazer a verificacao: ')
apt = int(raw_input('A partir de que numero deseja fazer a verificacao: '))
palindromos = []
primos = []
primoepalindromo = []
rng = int(rng)
for num in range(apt,rng+1):
    par = False
    x = 0
    if num %2 == 0:
        par = True
    if len(str(num)) < 3:
        digit = True
    if len(str(num)) >= 3:
        digit = False
    if str(num) == str(num)[::-1] and digit == False:
        palindromos.append(num)
    for i in range(3,num):
        if num %i == 0 or par == True:
            x = 0
            break
        else:
            x = 1
    if x == 1:
        primos.append(num)
    if num in primos and num in palindromos:
        primoepalindromo.append(num)
print 'Numeros palindromos e primos ate '+str(rng)+':'
print primoepalindromo
