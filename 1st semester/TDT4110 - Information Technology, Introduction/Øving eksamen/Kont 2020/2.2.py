def pos_vocals(text):
    liste = []
    for i in range(len(text)):
        if (text[i].lower() == "a") or (text[i].lower() == "e") or (text[i].lower() == "i") or (text[i].lower() == "o") or (text[i].lower() == "u") or (text[i].lower() == "y") or (text[i].lower() == "æ") or (text[i].lower() == "ø") or (text[i].lower() == "å"):
            liste.append(i)
    return liste

print(pos_vocals("DettE er et eksempel pÅ lAng liste med vokaler"))