sexo = input("Informe o sexo (F/M): ")
altura = float(input("Informe a altura em metros"))

if ( sexo == "F"):
	print("Peso Ideal = ", 62.1 * altura - 44.7)
else:
	print("Peso Ideal Masculino = ", 72.7 * altura - 58)