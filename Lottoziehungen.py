import random

def lottoziehung(ziehungen, zahlenbereichMax):
    ziehungenAnz = list(range(1, zahlenbereichMax + 1)) #von ChatGPT vorgeschlagen
    zahlen = random.sample(ziehungenAnz, ziehungen) #von ChatGPT vorgeschlagen
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