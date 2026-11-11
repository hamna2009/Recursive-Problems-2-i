def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    if stairs == 1:
        return 1
    if stairs >= 2:
        return ways(stairs - 1) + ways(stairs - 2)

print(ways(5))
print(ways(67))

num_stairs = int(input("Enter the number of stairs: "))
guess = int(input("Guess the number of ways to climb the stairs: "))
print(f"Number of ways to climb {num_stairs} stairs are {ways(num_stairs)} but your guess was {guess}.")
