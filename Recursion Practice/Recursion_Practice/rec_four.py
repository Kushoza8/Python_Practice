#direct return statement with a value terminates the function
def num(n):
    for i in range(n):
        if i==4:
            return 1
        print(i)
num(5)