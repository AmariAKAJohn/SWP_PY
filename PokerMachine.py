import random
import copy  # Import the copy module to perform deep copy

random.seed()

numbers2 = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"}

def drawRandomCards(amount):
    drawnCards = set()
    cards = [[], []]
    
    while len(cards[0]) < amount:
        numberFind = random.randint(1, 13)  # Random number between 1 and 13
        numberChoice = numbers2[numberFind]
        symbol = random.choice(["♠", "♦", "♣", "♥"])
        card = numberChoice + symbol
        if card not in drawnCards:
            cards[0].append(numberChoice)
            cards[1].append(symbol)
            drawnCards.add(card)
    return cards

def sortCards(cards):
    sortedCards = [ [],[] ]
    for i in range(1, 14):
        for j in range(len(cards[0])):
            if cards[0][j] == numbers2[i]:
                sortedCards[0].append(cards[0][j])
                sortedCards[1].append(cards[1][j])
    return sortedCards

def ConvertCardAJQK(cardis):
    # Make a deep copy of the input list to avoid modifying the original
    cardCopy = copy.deepcopy(cardis)
    
    for i in range(len(cardCopy[0])):
        if cardCopy[0][i] == "A":
            cardCopy[0][i] = 1
        elif cardCopy[0][i] == "J":
            cardCopy[0][i] = 11
        elif cardCopy[0][i] == "Q":
            cardCopy[0][i] = 12
        elif cardCopy[0][i] == "K":
            cardCopy[0][i] = 13
        else:
            cardCopy[0][i] = int(cardCopy[0][i])
    return cardCopy

def Flush(cards):
    if cards[1].count(cards[1][0]) == 5:
        return True
    else:
        return False
    
def Straight(cards):
    cards = ConvertCardAJQK(cards)
    cards[0].sort()

    if cards[0][0] == 1 and cards[0][len(cards[0])-1] == 13:
        cards[0][0] = 14
        cards[0].sort()
    for i in range(1, len(cards[0])):
        if cards[0][i] != cards[0][i-1]+1:
            return False
    return True

def StraightFlush(cards):
    if Straight(cards) and Flush(cards):
        return True
    else:
        return False

def FourOfAKind(cards):
    cards = ConvertCardAJQK(cards)
    for i in range(1, 14):
        if cards[0].count(i) == 4:
            return True
    return False

def ThreeOfAKind(cards):
    cards = ConvertCardAJQK(cards)
    for i in range(1, 14):
        if cards[0].count(i) == 3:
            return True
    return False

def FullHouse(cards):
    if ThreeOfAKind(cards):
        cards = ConvertCardAJQK(cards)
        for i in range(1, 14):
            if cards[0].count(i) == 2:
                return True
    return False

def Pair(cards):
    cards = ConvertCardAJQK(cards)
    for i in range(1, 14):
        if cards[0].count(i) == 2:
            return True
    return False

def TwoPair(cards):
    cards = ConvertCardAJQK(cards)
    countPair = 0
    for i in range(1, 14):
        if cards[0].count(i) == 2:
            countPair += 1
    if countPair == 2:
        return True
    else:
        return False
    
def RoyalFlush(cards):
    if StraightFlush(cards) and (cards[0][0] == "A" and cards[0][len(cards[0])-1] == "K"):
        return True
    else:
        return False
    


def CreateStatistic(rounds):
    statistic = {"RoyalFlush": 0, "StraightFlush": 0, "FourOfAKind": 0, "FullHouse": 0, "Flush": 0, "Straight": 0, "ThreeOfAKind": 0, "TwoPair": 0, "Pair": 0, "HighCard": 0}
    for i in range(rounds):
        cards = drawRandomCards(5)
        if RoyalFlush(cards):
            statistic["RoyalFlush"] += 1
        elif StraightFlush(cards):
            statistic["StraightFlush"] += 1
        elif FourOfAKind(cards):
            statistic["FourOfAKind"] += 1
        elif FullHouse(cards):
            statistic["FullHouse"] += 1
        elif Flush(cards):
            statistic["Flush"] += 1
        elif Straight(cards):
            statistic["Straight"] += 1
        elif ThreeOfAKind(cards):
            statistic["ThreeOfAKind"] += 1
        elif TwoPair(cards):
            statistic["TwoPair"] += 1
        elif Pair(cards):
            statistic["Pair"] += 1
        else:
            statistic["HighCard"] += 1

    print("HighCard ", str(statistic["HighCard"]) + " -> " + str(statistic["HighCard"]/rounds*100) + "%")
    print("Pair ", str(statistic["Pair"]) + " -> " + str(statistic["Pair"]/rounds*100) + "%")
    print("TwoPair ", str(statistic["TwoPair"]) + " -> " + str(statistic["TwoPair"]/rounds*100) + "%")
    print("ThreeOfAKind ", str(statistic["ThreeOfAKind"]) + " -> " + str(statistic["ThreeOfAKind"]/rounds*100) + "%")
    print("Straight ", str(statistic["Straight"]) + " -> " + str(statistic["Straight"]/rounds*100) + "%")
    print("Flush ", str(statistic["Flush"]) + " -> " + str(statistic["Flush"]/rounds*100) + "%")
    print("FullHouse ", str(statistic["FullHouse"]) + " -> " + str(statistic["FullHouse"]/rounds*100) + "%")
    print("FourOfAKind ", str(statistic["FourOfAKind"]) + " -> " + str(statistic["FourOfAKind"]/rounds*100) + "%")
    print("StraightFlush ", str(statistic["StraightFlush"]) + " -> " + str(statistic["StraightFlush"]/rounds*100) + "%")
    print("RoyalFlush ", str(statistic["RoyalFlush"]) + " -> " + str(statistic["RoyalFlush"]/rounds*100) + "%")
    return statistic

