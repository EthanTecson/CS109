
def hailstone(start):
    count = 1
    print(start)
    if start > 0:
        while start != 1:
            if start % 2 == 0:
                start = start // 2
                print(start)
                count = count + 1
            else:
                start = (start * 3) + 1
                print(start)
                count = count + 1
        else: print('Number of Integers: ', count)
    else:
        print('Please Enter Positive Number')

def main():
    number = int(input("Enter Positive Integer: "))
    hailstone(number)
main()


