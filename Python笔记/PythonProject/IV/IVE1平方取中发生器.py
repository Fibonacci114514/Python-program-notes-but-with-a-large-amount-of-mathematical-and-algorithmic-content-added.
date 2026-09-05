seed = 2333
def random4():
    global seed
    seed = seed ** 2
    return int(str(seed)[1:5])
for i in range(10):
    print(random4())