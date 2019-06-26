def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors
#La fonction d prend en paramètre un nombre et retourne la somme des
#diviseurs de n, n étant exclu
def d(nb):
    return 1 + sum(divisors(nb))
resultat = 0
for a in range(1, 10000):
    b = d(a)
    if d(b) == a and a != b:
        resultat += a
print(resultat)
