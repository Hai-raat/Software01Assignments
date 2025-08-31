import random

N = int(input("Please enter a random number to generate: "))

inside_circle = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_circle += 1

pi_approx = 4 * inside_circle / N
print(f"Approximation of pi with {N} points: {pi_approx}")