# < Іваньо Іван >
# Лабораторна робота № 4.4
# Табуляція функції, заданої графіком.
# Варіант 0.6

R = int(input("R: "))
X_start = int(input("X_поч: "))
X_end = int(input("X_кін: "))
dX = int(input("dX: "))

print('---------------------------')
print('|   X   |   Y   |')
print('---------------------------')

x = X_start

while x <= X_end:
    if x <= -5:
        y = -3
    elif -5 < x <= -R:
        y = (3 * R + 3 * x) / (-R + 5)
    elif -R < x <= R:
        y = (R ** 2 - x ** 2) ** 0.5
    elif R < x <= 8:
        y = R * (x - R) / (8 - R)
    else:
        y = R

    print('|   ' + str(x) + '   |   ' + str(round(y, 3)) + '   |')
    x += dX

print('---------------------------')
