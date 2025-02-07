def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens  
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits  
    return "No solution"


num_heads = int(input("number of heads: "))
num_legs = int(input(" number of legs: "))

result = solve(num_heads, num_legs)


if isinstance(result, tuple):
    chickens, rabbits = result
    print("Chickens:", chickens)
    print("Rabbits:", rabbits)
else:
    print(result)
