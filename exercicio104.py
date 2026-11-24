valores = {
    "PR": 0.0190, 
    "AC": 0.02, 
    "ES": 0.02, 
    "SC": 0.02, 
    "PE": 0.024, 
    "MA": 0.025,
    "PA": 0.025, 
    "PB": 0.025, 
    "SE": 0.025, 
    "AL": 0.03, 
    "AM": 0.03,
    "AP": 0.03, 
    "BA": 0.03, 
    "DF": 0.03,
    "MS": 0.03, 
    "MT": 0.03, 
    "PI": 0.03, 
    "RN": 0.03, 
    "RO": 0.03, 
    "RR": 0.03,
    "RS": 0.03, 
    "CE": 0.035, 
    "TO": 0.035, 
    "GO": 0.0375, 
    "MG": 0.04, 
    "RJ": 0.04, 
    "SP": 0.04, 
}

print("calculo do valor de cada estado")
print()

estado = input("digite a sigla do estado:").upper()
valor = float(input("digite o valor:"))

if estado in valores:
    percentual = valores[estado]
    valor_calculado = percentual * valor 

    print()
    print(f"o valor para cada estado {estado} é de R${valor_calculado:.2F}")

else:
    print(f"o estado{estado} é valido")