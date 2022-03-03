asd = int(input("Write a number then see if it is prime: "))
flag = True

for i in range(2,asd):
    if asd % i == 0:
        flag = False
        print(f"{asd} is NOT prime")
        break

if flag:
    print(f"{asd} is prime")
