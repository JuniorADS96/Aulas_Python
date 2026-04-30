# 1. ENTRADA DE DADOS
# O input() lê o que você digita como TEXTO. 
# Como idade é um número, usamos o int() para converter esse texto em um NÚMERO INTEIRO.
idade = int(input("Digite sua idade: "))

# 2. ESTRUTURA DE DECISÃO (O "Cérebro" do programa)

# O 'if' (significa "SE") testa a primeira condição: a idade é menor que 18?
if idade < 18:
    # Se for verdade, ele executa o bloco abaixo e ignora o restante.
    print("Voce é menor de idade.")

# O 'elif' (abreviação de ELSE IF - SENÃO SE) serve para testar uma segunda opção,
# caso a primeira lá em cima tenha sido falsa.
elif idade == 18:
    # Note que usamos '==' para comparar igualdade. Um '=' sozinho serve para guardar valor.
    print("Você tem exatamente 18 anos.")

# O 'else' (SENÃO) é o nosso "plano B". 
# Se não for menor que 18 e nem igual a 18, só sobrou ser maior.
else:
    print("Você é maior de idade.")

# Resumo: O programa segue um caminho por vez, dependendo do valor da variável 'idade'.
