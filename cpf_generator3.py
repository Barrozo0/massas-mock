#CPF BASE - NÃO AUTORIZADO
import random

# Função para calcular o dígito verificador
def calcular_dv_cpf(digitos, pesos):
    soma = sum(d * p for d, p in zip(digitos, pesos))
    resto = soma % 11
    dv = 11 - resto
    return dv if dv < 10 else 0

# Função para garantir que o primeiro dígito seja ímpar (diferente de 7 ou 9)
def ajustar_primeiro_dv(dv):
    if dv % 2 == 0:  # Se for par, soma 1 para torná-lo ímpar
        dv += 1
    if dv == 7 or dv == 9:  # Se for 7 ou 9, ajusta para outro ímpar (ex: 5 ou 3)
        dv = 5 if dv == 7 else 3
    return dv

# Função para garantir que o segundo dígito seja ímpar (não pode ser 9)
def ajustar_segundo_dv(dv):
    if dv % 2 == 0:  # Se for par, soma 1 para torná-lo ímpar
        dv += 1
    if dv == 9:  # Se for 9, ajusta para 7
        dv = 7
    return dv

# Função para gerar CPF válido com as restrições dos dígitos verificadores
def gerar_cpf3():
    cpf = [random.randint(0, 9) for _ in range(9)]  # Base do CPF

    pesos_primeiro_dv = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo_dv = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # Calcular o primeiro dígito verificador
    primeiro_dv = calcular_dv_cpf(cpf, pesos_primeiro_dv)
    primeiro_dv = ajustar_primeiro_dv(primeiro_dv)  # Ajustar para ser ímpar (diferente de 7 ou 9)
    cpf.append(primeiro_dv)

    # Calcular o segundo dígito verificador
    segundo_dv = calcular_dv_cpf(cpf, pesos_segundo_dv)
    segundo_dv = ajustar_segundo_dv(segundo_dv)  # Ajustar para ser ímpar
    cpf.append(segundo_dv)

    # Verificar se o CPF gerado é válido
    if validar_cpf(cpf):
        # Transformar o CPF em string e retornar
        cpf_str = ''.join(map(str, cpf))
        return cpf_str
    else:
        # Tentar novamente até gerar um CPF válido
        return gerar_cpf3()

# Função para validar um CPF gerado
def validar_cpf(cpf):
    pesos_primeiro_dv = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo_dv = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # Verificar primeiro dígito verificador
    primeiro_dv = calcular_dv_cpf(cpf[:9], pesos_primeiro_dv)
    if primeiro_dv != cpf[9]:
        return False

    # Verificar segundo dígito verificador
    segundo_dv = calcular_dv_cpf(cpf[:10], pesos_segundo_dv)
    if segundo_dv != cpf[10]:
        return False

    return True
