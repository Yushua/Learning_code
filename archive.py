# i = "hello "
# i += "hello"
# print(i)

# enemy = []

# enemy.append("yusha")
# enemy.append("yusha2")
# enemy.append("yusha3")
# enemy.append("yusha4")
# enemy.append("yusha5")
# lenght = len(enemy)

# x = 0;
# while x < lenght:
#     print(enemy[x])
#     x += 1
# print("\nCollections")
# actions = {"a": 1, "b": 2}
# actions["c"] = 3
# actions["\n"] = 3
# actions.get("d")
# del(actions["c"])
# print(actions.keys())
# print(actions.values())
# print(actions.items())
# print("\n")

# x = 2

# while x <= 20:
#     if x == 2:
#         print(x)
#     elif x % 2 != 0 or x % 3 != 0 or x % 4 != 0 or x % 5 != 0 or x % 6 != 0 or x % 7 != 0 or x % 8 != 0 or x % 9 != 0:
#         print(x)
#     x += 1

x = 0;
y = 0;
string = "hello"
def     increase_mov(xi, yi):
    global x
    global y
    x += xi
    y += yi
def     ftstrjoin(string, tmp):
    string += tmp
    return string
string = ftstrjoin(string, "hello")
increase_mov(2, 2)
print(x, y)
print(string)
