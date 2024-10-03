import random

def lottoziehung(ziehungen, zahlenbereichMax):
    zahlen = []
    check = False
    for i in range(ziehungen):         
        zufallszahl = random.randint(1, zahlenbereichMax) 
        for j in range(len(zahlen)):
            if(zufallszahl == zahlen[j]): 
                check = True
                break
        if(check == False):
            zahlen.append(zufallszahl)
    return zahlen


if __name__ == "__main__":
    statistic = {}
    for i in range(1, 1000):
        ziehungen = 6  
        zahlenbereichMax = 45 
        zahlen = lottoziehung(ziehungen, zahlenbereichMax)
        for zahl in zahlen:
            if zahl in statistic:
                statistic[zahl] += 1
            else:
                statistic[zahl] = 1

    sorted_stat = dict(sorted(statistic.items())) #von ChatGPT vorgeschlagen
    for i in sorted_stat:
        print(i, ":", str(sorted_stat[i]) + " mal gezogen")