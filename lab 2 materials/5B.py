print('this program calculates times table')
tablenum = input('\nWhich multiplication table shall i generate for you?')
tablenum = int(tablenum)
print("\nHere is your",tablenum,"times table:\n")
for i in range(1,13):
    print(i, "times", tablenum, "is",i*tablenum)
    print("-------------------")