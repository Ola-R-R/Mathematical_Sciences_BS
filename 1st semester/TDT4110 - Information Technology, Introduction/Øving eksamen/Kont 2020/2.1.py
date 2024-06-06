def home_draw_away(matches):
    h = 0
    u = 0
    b = 0
    liste = []
    for i in range(0, len(matches)):
        if matches[i].lower() == "h":
            h += 1
        elif matches[i].lower() == "u":
            u += 1
        elif matches[i].lower() == "b":
            b += 1
    liste.append(h)
    liste.append(u)
    liste.append(b)
    return liste

print(home_draw_away(("h","u","B", "h")))