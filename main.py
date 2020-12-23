
def result(game, table):
    points = {"win": 3, "draw": 1, "loss": 0}
    for i in game:
        g = i.split(';')
        if g[2] == "win":
            table[g[0]][0] += 1
            table[g[0]][1] += 1
            table[g[0]][4] += points["win"]
            table[g[1]][0] += 1
            table[g[1]][3] += 1
        elif g[2] == "loss":
            table[g[0]][0] += 1
            table[g[0]][3] += 1
            table[g[1]][0] += 1
            table[g[1]][1] += 1
            table[g[1]][4] += points["win"]
        elif g[2] == "draw":
            table[g[0]][0] += 1
            table[g[0]][2] += 1
            table[g[0]][4] += points["draw"]
            table[g[1]][0] += 1
            table[g[1]][2] += 1
            table[g[1]][4] += points["draw"]

    list_d = list(table.items())
    list_d.sort(key=lambda k: k[1][4], reverse=True)

    return list_d


def table(liga):
    table_liga = dict()
    for i in liga:
        table_liga[i] = [0, 0, 0, 0, 0]
    return table_liga


def print_table(table):
    print("Team\t\t\t\t\t\t\t| MP | W | D | L | P")
    for i in table:
        print("{}\t\t\t\t| {}  | {} | {} | {} | {}".format(i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4]))


la_liga = ["Allegoric Alaskans", "Blithering Badgers", "Devastating Donkeys", "Courageous Californians"]

first_game = [
    "Courageous Californians;Devastating Donkeys;win",
    "Allegoric Alaskans;Blithering Badgers;win",
    "Devastating Donkeys;Allegoric Alaskans;loss",
    "Courageous Californians;Blithering Badgers;win",
    "Blithering Badgers;Devastating Donkeys;draw",
    "Allegoric Alaskans;Courageous Californians;draw"
    ]

table_l = table(la_liga)
list_res = result(first_game, table_l)

print_table(list_res)
