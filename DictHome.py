dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

print("\n")




print("\n")

votersDict = {"Denis":32, "Sergei":21, "Elena":18, "Timur":17, "Oleg": 27}
for voter, numb in votersDict.items():
    if numb > 18:
        print(f'Вас зовут: {voter} , вам {numb} лет и вы можете голосовать')
    if numb < 18:
        print((f'Вас зовут: {voter} , вам {numb} лет и вы НЕ можете голосовать, потому что вы слишком молоды!'))

print("\n")

studentList = {"Oleg":"Moscow", "Stepan": "Novosibirsk", "Olga": "Ekaterenburg", "Murat":"Bishkek", "David":"New York"}
name = input("Введите имя человека, который вы хотите удалить: ")
del studentList[name]
print(studentList)

print("\n")
sampleDict = {"class":
                  { "student":
                        { "name":"Mike","marks":
                            { "physics":70, "history" :80}
                          }
                    }
              }
print(sampleDict['class']["student"]["marks"]["history"])

