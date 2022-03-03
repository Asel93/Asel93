a = str(input("Введите ваше имя: "))
counter = 1
while counter <= 20:
    print(f'{a}')
    counter += 1

print("\n")


counter = 1
while counter <= 25:
    print(counter*5, end=" ")
    counter = counter + 3

counter = 1
for counter in range(1, 26, 3):
    print(counter*5, end = " ")

print('\n')

a = int(input("Введите число: "))
while a > 0:
    print("Результат числа после добавления 10-ти:", a+10)
    break
if a == 0:
    print("Выход из вычисления!")


print('\n')


a = str(input("Введите слово или фразу: "))
for i in a:
    print(2 * i, end='')
