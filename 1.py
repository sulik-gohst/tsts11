god = i16nt(input())
if god % 4 != 0:
    print("Обычный")
elif god % 100 == 0:
    if god % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")