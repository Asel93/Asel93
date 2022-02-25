
a = str(input("Введите слово или текст: "))
print(a[::-1])

a = "Я обучаюсь курсу Python Django"
print("Название курса:" , a[17:])

b = "$$$Python@@@"
c = b.lstrip("$")
d = c.rstrip("@")
print(d)

w = "%%%Programming"
print(w.lstrip("%"))

z = "City&&&"
print(z.rstrip("&"))

m = "****Computer***"
print(m.strip("*"))

number = str(input("Любимое число: "))
color = str(input("Любимый цвет: "))
city = str(input("Любимый город: "))
food = str(input("Любимая еда: "))
print("Любимое число: {0}\nЛюбимый цвет: {1}\nЛюбимый город: {2}\nЛюбимая еда: {3}".format(number, color, city, food))
print(f"Любимое число: {number}\nЛюбимый цвет: {color}\nЛюбимый город: {city}\nЛюбимая еда: {food}")