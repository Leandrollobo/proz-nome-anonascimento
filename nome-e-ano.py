nomeArmazenado = ''


def nome():
    global nomeArmazenado
    novoNome = False
    while (novoNome == False):
        try:
            nome = input("Digite seu nome completo:")

            if nome == '':
                print(
                    "Este campo não pode ser vazio, por favor digite seu nome completo")
            else:
                print("Obrigado", nome)
                nomeArmazenado = nome
                novoNome = True
                anoNascimento()

        except:
            print("Except")


def anoNascimento():
    novoAno = False

    while (novoAno == False):
        try:
            anoMinimo = 1922
            anoMaximo = 2021
            idade = 0
            anoNasc = int(
                input("Digite o ano do seu nascimento com 4 digitos: "))

            if anoNasc == '':
                print(
                    "Este campo não pode ser vazio, por favor digite o ano de nascimento com 4 digitos.")

            elif anoNasc < anoMinimo:
                print("Para este calculo o ano de nascimento deve ser maior que 1921")

            elif anoNasc > anoMaximo:
                print("Para este calculo o ano de nascimento deve ser menor que 2021")

            else:
                idade = 2023 - anoNasc
                print(nomeArmazenado, "Sua idade é:", idade)
                novoAno = True

        except:
            print("Letras e simbolos não permitidos, por favor digite apenas seu ano de nascimento no formato: AAAA")


nome()
