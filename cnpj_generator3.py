#CNPJ NÃO EXISTE - SEGMENTO NÃO VALIDADO
import random
 
def calcular_dv_cnpj(digitos, pesos):
    soma = sum(d * p for d, p in zip(digitos, pesos))
    resto = soma % 11
    dv = 11 - resto
    return dv if dv < 10 else 0
 
def gerar_cnpj3():
    while True:
        # Gera os primeiros 12 dígitos do CNPJ
        cnpj = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]  # Os 4 últimos dígitos fixos (0001)
 
        # Pesos para o cálculo dos dígitos verificadores
        pesos_primeiro_dv = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos_segundo_dv = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
 
        # Calcula o primeiro dígito verificador
        primeiro_dv = calcular_dv_cnpj(cnpj, pesos_primeiro_dv)
 
        # Verifica se o primeiro dígito verificador é 9
        if primeiro_dv != 9:
            continue  # Gera um novo CNPJ se o primeiro dígito verificador não for 9
 
        cnpj.append(primeiro_dv)
 
        # Calcula o segundo dígito verificador
        segundo_dv = calcular_dv_cnpj(cnpj, pesos_segundo_dv)
 
        # Verifica se o segundo dígito verificador é 9
        if segundo_dv != 9:
            continue  # Gera um novo CNPJ se o segundo dígito verificador não for 9
 
        cnpj.append(segundo_dv)
 
        # Formata o CNPJ em uma string
        cnpj_str = ''.join(map(str, cnpj))
        return cnpj_str