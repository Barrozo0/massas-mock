#CPF NÃO EXISTE SFA - NÃO AUTORIZADO
import random
 
def calcular_dv(digitos):
    peso = len(digitos) + 1
    soma = sum(d * (peso - i) for i, d in enumerate(digitos))
    resto = soma % 11
    dv = 11 - resto
    return dv if dv < 10 else 0
 
def gerar_cpf5():
    while True:
        # Gera os primeiros 9 dígitos do CPF
        cpf = [random.randint(0, 9) for _ in range(9)]
 
        # Calcula o primeiro dígito verificador
        primeiro_dv = calcular_dv(cpf)
 
        # Verifica se o primeiro dígito verificador é exatamente 7
        if primeiro_dv != 7:
            continue  # Gera um novo CPF se o primeiro dígito verificador não for 7
 
        cpf.append(primeiro_dv)
 
        # Calcula o segundo dígito verificador
        segundo_dv = calcular_dv(cpf)
 
        # Verifica se o segundo dígito verificador é ímpar
        if segundo_dv % 2 == 0:
            continue  # Gera um novo CPF se o segundo dígito verificador não for ímpar
 
        cpf.append(segundo_dv)
 
        # Formata o CPF em uma string
        cpf_str = ''.join(map(str, cpf))
        return cpf_str