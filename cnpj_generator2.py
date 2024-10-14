#CNPJ FRESH - SEGMENTO AUTORIZADO
import random
 
def calcular_dv_cnpj(digitos, pesos):
    soma = sum(d * p for d, p in zip(digitos, pesos))
    resto = soma % 11
    dv = 11 - resto
    return dv if dv < 10 else 0
 
def gerar_cnpj2():
    while True:
        # Gera os primeiros 12 dígitos do CNPJ
        cnpj = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]  # Os 4 últimos dígitos fixos (0001)
 
        # Pesos para o cálculo dos dígitos verificadores
        pesos_primeiro_dv = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos_segundo_dv = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
 
        # Calcula o primeiro dígito verificador
        primeiro_dv = calcular_dv_cnpj(cnpj, pesos_primeiro_dv)
 
        # Ajusta o primeiro dígito verificador para ser par, se necessário
        if primeiro_dv % 2 != 0:
            continue  # Gera um novo CNPJ se o primeiro dígito verificador não for par
 
        cnpj.append(primeiro_dv)
 
        # Calcula o segundo dígito verificador
        segundo_dv = calcular_dv_cnpj(cnpj, pesos_segundo_dv)
 
        # Ajusta o segundo dígito verificador para ser par, se necessário
        if segundo_dv % 2 != 0:
            continue  # Gera um novo CNPJ se o segundo dígito verificador não for par
 
        cnpj.append(segundo_dv)
 
        # Formata o CNPJ em uma string
        cnpj_str = ''.join(map(str, cnpj))
        return cnpj_str