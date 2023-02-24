print("----------------------------")
print("   CADASTRO FUNCIONARIO     ")
print("----------------------------")
codigo = int(input("Digite o código do funcionário: "))
nome = input("Digite o nome do funcionário: ")
salario = float(input("Informe o salario: "))
ativo = True
idade = int(input("Digite a idade: "))

print("----------------------------")
print("   RESUMO FUNCIONARIO     ")
print("----------------------------")
print("Código: %d "%codigo)
print("Nome: %s"%nome)
print("Salário: %.2f " % salario)
if idade >= 18:
    print("Idade: Maior Idade")
else:
    print("Idade: Menor idade")
print("Ativo: %r "% ativo)
print("----------------------------")