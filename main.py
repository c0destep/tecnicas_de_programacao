import statistics


def welcome():
    print('Welcome Developer :)')
    item = int(input('Digite o número da Questão para acessa-lá: '))
    return item


question = welcome()

if question == 1:
    count = 0
    text = ""

    while count < 10:
        text += "Hello World"
        count = count + 1

    print(text)
elif question == 2:
    count = 0

    while count < 10:
        print("Hello World")
        count = count + 1

elif question == 3:
    count = 0

    while count < 100:
        if count % 2 == 0:
            print(count)

        count = count + 1

elif question == 4:
    count = 1

    while count <= 100:
        print(f"{count} - Hello World")
        count = count + 1

elif question == 5:
    count = 100

    while count > 0:
        print(count)
        count = count - 1

elif question == 6:
    count = 0

    while count < 1000:
        if count % 2 == 0:
            print(count)

        count = count + 1

elif question == 7:
    count = 1000

    while count > 0:
        if count % 2 == 1:
            print(count)

        count = count - 1

elif question == 8:
    count = 0
    total = 0

    while count <= 100:
        total += count
        count = count + 1

    print(total)

elif question == 9:
    n = int(input('Digite a quantidade de vezes que repetirá: '))
    count = 0

    while count < n:
        print("Hello World")
        count = count + 1

elif question == 10:
    text = str(input('Digite uma palavra: '))
    n = int(input('Digite a quantidade de vezes que repetirá essa palavra: '))
    count = 0

    while count < n:
        print(text)
        count = count + 1

elif question == 11:
    n = int(input('Informe a quantidade de número que irá digitar: '))
    count = 0
    soma = 0

    while count < n:
        number = int(input('Digite o número: '))
        soma += number
        count = count + 1

    print(f'A soma deu {soma} é a média foi {soma / n}')

elif question == 12:
    x = int(input('Informe a quantidade de pessoas que irá digitar: '))
    count = 1
    items = []
    ages = []


    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age


    while count <= x:
        y = str(input(f'Informe o nome da {count}° pessoa: '))
        z = int(input(f'Informe a idade da {count}° pessoa: '))

        items.append(Person(y, z))
        count = count + 1

    for k in items:
        ages.append(k.age)

    old = max(ages)

    for p in items:
        if p.age == old:
            print(f'{p.name} é o(a) mais velho(a) entre os {x}')

elif question == 13:
    r = int(input('Informe a quantidade de pessoas que irá digitar: '))
    count = 1
    male = []
    female = []

    while count <= r:
        y = str(input(f'Informe o sexo da {count}° pessoa: '))
        z = int(input(f'Informe a idade da {count}° pessoa: '))

        if y == 'M':
            male.append(z)
        else:
            female.append(z)

        count = count + 1

    print(f'Média de idade do Sexo Masculino {sum(male) / len(male)}')
    print(f'Média de idade do Sexo Feminino {sum(female) / len(female)}')

elif question == 14:
    count = 0
    numbers = []

    while count < 10:
        numbers.append(float(input('Digite os números: ')))
        count = count + 1

    print(f'{max(numbers)} é o maior')
    print(f'{min(numbers)} é o menor')

elif question == 15:
    count = 1
    nums = []

    while count > 0:
        num = float(input(f'Informe o {count}° número: '))

        if num != 0:
            nums.append(num)
        else:
            print(sorted(nums, key=None, reverse=True))
            break

        count = count + 1

else:
    count = 1
    students = []
    students_olds = 0
    students_kids = 0

    while count > 0:
        z = int(input(f'Informe a idade do {count}° aluno: '))
        students.append(z)

        print('----Responda com "Sim" ou "Não"---- \n')
        res = str(input(f'Deseja informa a idade do proximo aluno: '))

        if res == 'Sim':
            count = count + 1
        else:
            print(f'O mais velho tem {max(students)} anos')
            print(f'O mais novo tem {min(students)} anos')

            for student in students:
                if student > 18:
                    students_olds = students_olds + 1
                else:
                    students_kids = students_kids + 1

            med = sum(students) / len(students)
            print(f'{students_olds} com mais de 18')
            print(f'{students_kids} com menos de 18')
            print(f'A média de idade é {med:.1f} anos')
            print(f'Mediana das idades é {statistics.median(students)} anos')
            break
