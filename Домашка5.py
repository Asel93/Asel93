print(list(range(15, 100, 5)))

print("\n")

for i in range(15, 100, 5):
    print(i)

print("\n")


i = 15
while  i <=100:
    print(i)
    i+=5


print("\n")

a = ["Moscow", "Bishkek", "NY", "Tashkent", "Almaty","Talas", "NY", "Moscow"]
#a.remove('NY') - 1 вариант
del a[7] # - 2 вариант
#a.remove('Moscow') - 1 вариант
del a[6] # - 2 вариант
print(a)

print("\n")

list1 = [34, 31, 5, 53,1,34, 5]
sum1 = 0
avg = 0
a = len(list1)
for i in list1:
    sum1 +=i
avg = sum1/a
print("Среднеарифметическое значение внутри данного списка", list1, ":", avg)

print("\n")

list2 = ["Елена", "Степан", "Мурат", "Асан", "Айсулуу"]
print(f"{list2[0]} получает ЗП: 50 тыс.рублей \n{list2[1]} получает ЗП: 70 тыс.рублей \n{list2[2]} получает ЗП: 50 тыс.рублей \n{list2[3]} получает ЗП: 50 тыс.рублей \n{list2[4]} получает ЗП: 50 тыс.рублей \n" )

print("\n")


