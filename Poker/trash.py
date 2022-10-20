def Card_Deck():
    whole = []
    diamonds = []
    clubs = []
    hearts = []
    spades = []
    for i in range(1,53,1):
        if i < 15:
            diamonds.append(i)
            whole.append(i)
        elif i > 14 and i <29:
            clubs.append(i)
            whole.append(i**2)
        elif i > 28 and i <43:
            hearts.append(i)
            whole.append(i**3)
        else:
            spades.append(i)
            whole.append(i**4)
    return diamonds, clubs, hearts, spades, whole