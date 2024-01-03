import random
for i in range(1,7):
    f="1";
    for j in range(1,11):
        f+=str(random.randint(0,9))
    print(f)