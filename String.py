name = str(input("Имя "))
age = int(input("Возраст "))
Gender = str(input("Пол "))
company = str (input("Компания, в которой работаете "))
family = str(input("Семейное положение "))
adress = str (input("Адрес проживания "))
print(len(name))

a = company
if a in company:
    print("Yes")

print(adress[2])
print(name[1:])
print(company[::-1])
print(" Имя :{0}\n Возраст:{1}\n Пол:{2}\n Компания, в которой работаете:{3}\n Семейное положение:{4}\n Адрес проживания:{5}".format(name, age, Gender, company, family, adress))
print(f" Имя: {name}\n Возраст: {age}\n Пол: {Gender}\n Компания,в которой работаете: {company}\n Семейное положение: {family}\n Адрес проживания: {adress}")

print("""
Белеет парус одинокой
В тумане моря голубом!..
Что ищет он в стране далекой?
Что кинул он в краю родном?..

Играют волны — ветер свищет,
И мачта гнется и скрыпит...
Увы! он счастия не ищет
И не от счастия бежит!
""")