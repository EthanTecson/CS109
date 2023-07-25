def power(base, exponent):
    new_base = 0
    variable = 0
    for i in range(exponent):
        answer = base + variable
        variable = base * base
        #base = base * i
    print(answer)

power(2, 4)