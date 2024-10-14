#CNPJ BASE SEGMENTO AUTORIZADO
import random

# Função para calcular o dígito verificador
def calcular_dv_cnpj(digitos, pesos):
    soma = sum(d * p for d, p in zip(digitos, pesos))
    resto = soma % 11
    dv = 11 - resto
    return dv if dv < 10 else 0

# Função para garantir que o primeiro dígito seja ímpar (diferente de 9)
def ajustar_primeiro_dv(dv):
    if dv % 2 == 0:  # Se for par, soma 1 para torná-lo ímpar
        dv += 1
    if dv == 9:  # Se for 9, reduz para 7 (para não permitir 9)
        dv = 7
    return dv

# Função para garantir que o segundo dígito seja par
def ajustar_segundo_dv(dv):
    if dv % 2 != 0:  # Se for ímpar, soma 1 para torná-lo par
        dv += 1
    return dv

# Função para gerar CNPJ válido com as restrições dos dígitos verificadores
def gerar_cnpj():
    cnpj = [random.randint(0, 9) for _ in range(8)] + [0, 0, 0, 1]  # Base do CNPJ

    pesos_primeiro_dv = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo_dv = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # Calcular o primeiro dígito verificador
    primeiro_dv = calcular_dv_cnpj(cnpj, pesos_primeiro_dv)
    primeiro_dv = ajustar_primeiro_dv(primeiro_dv)  # Ajustar para ser ímpar (diferente de 9)
    cnpj.append(primeiro_dv)

    # Calcular o segundo dígito verificador
    segundo_dv = calcular_dv_cnpj(cnpj, pesos_segundo_dv)
    segundo_dv = ajustar_segundo_dv(segundo_dv)  # Ajustar para ser par
    cnpj.append(segundo_dv)

    # Verificar se o CNPJ gerado é válido
    if validar_cnpj(cnpj):
        # Transformar o CNPJ em string e retornar
        cnpj_str = ''.join(map(str, cnpj))
        return cnpj_str
    else:
        # Tentar novamente até gerar um CNPJ válido
        return gerar_cnpj()

# Função para validar um CNPJ gerado
def validar_cnpj(cnpj):
    pesos_primeiro_dv = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo_dv = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # Verificar primeiro dígito verificador
    primeiro_dv = calcular_dv_cnpj(cnpj[:12], pesos_primeiro_dv)
    if primeiro_dv != cnpj[12]:
        return False

    # Verificar segundo dígito verificador
    segundo_dv = calcular_dv_cnpj(cnpj[:13], pesos_segundo_dv)
    if segundo_dv != cnpj[13]:
        return False

    return True