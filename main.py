import statistics


def welcome():
    print('Welcome Developer :)\n')
    questions = [
        "1. Elabore um algoritmo que imprima na tela lado a lado o texto 'Hello World!' 10 vezes.",
        "2. Elabore um algoritmo que imprima na tela o texto 'Hello World!' 10 vezes, um por linha.",
        "3. Elabore um algoritmo que imprima todos os números inteiros de 1 até 100 inclusive.",
        "4. Elabore um algoritmo que imprima 100 vezes o texto '1- Hello World!' com o número.",
        "5. Elabore um algoritmo que imprima todos os números decrescentes de 100 até 0 inclusive.",
        "6. Elabore um algoritmo que imprima todos os números pares inteiros de 1 até 1000.",
        "7. Elabore um algoritmo que imprima todos os números ímpares de 1000 até 0.",
        "8. Elabore um algoritmo que imprima a soma dos 100 primeiros números inteiros positivos.",
        "9. Elabore um algoritmo que solicite ao usuário um número inteiro que indicará a quantidade de vezes que o "
        "texto 'Hello World!' será impresso na tela, um em cada linha.",
        "10. Elabore um algoritmo que solicite ao usuário uma palavra e um número inteiro que indicará a quantidade "
        "de vezes que a palavra digitada será impressa na tela, um em cada linha.",
        "11. Elabore um algoritmo que leia um número de entrada que indicará a quantidade de números a serem lidos. "
        "Em seguida, leia n números (conforme o valor informado anteriormente) e imprima a soma e a média aritmética "
        "dos números informados.",
        "12. Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos "
        "(N). Em seguida algoritmo deve solicitar o nome e idade de N pessoas e ao final apresentar o nome da pessoa "
        "mais velha.",
        "13. Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos "
        "(N). Em seguida algoritmo deve solicitar o sexo (M/F) e idade de N pessoas e ao final apresentar a média de "
        "idade de ambos os gêneros catalogados.",
        "14. Elabore um algoritmo que solicite ao usuário 10 números reais e ao final apresente o maior e o menor "
        "deles.",
        "15. Elabore um algoritmo que solicite N números reais e quando o usuário informar o valor nulo 0 (zero) o "
        "programa ordene e mostre todos os números informados de forma crescente.",
        "16. Escreva um programa que vá solicitando as idades dos alunos da sala até que todos sejam informados ("
        "perguntar ao usuário se deseja informar a idade do próximo aluno). Ao final apresentar a idade do mais novo, "
        "a idade do mais velho, Quantos alunos têm mais de 18 anos, quantos alunos têm até 18 anos, "
        "a média aritmética e a mediana. "
    ]

    for q in questions:
        print(q)

    item = int(input('\nDigite o número da Questão para acessa-lá: '))
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
