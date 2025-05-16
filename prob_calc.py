import random
prob = 0
for i in range (1_000_000):
    arr = []
    match = False
    for j in range (19):
        a = random.randint(0, 1000)
        for k in arr:
            if a == k:
                match = True
        arr.append(a)
    if match:
        prob += 1
    print('run: ' + str(i))
print (prob/10000)