"""
Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%.
"""




CAMISAS = 1000

total_camisas = input("Ingresá la cantidad de camisas: ")

if total_camisas.isdigit():
    total_pagar_camisas = CAMISAS * int(total_camisas)
    if int(total_camisas) >= 3:
        calculo_porcentaje = 20 / 100
        operacion = int(total_pagar_camisas) * float(calculo_porcentaje) 
        total_pagar = int(total_pagar_camisas) - int(operacion)
        print(f"El total a pagar con el 20% de descuento es de {total_pagar}")
    else:
        total_pagar_camisas = CAMISAS * int(total_camisas)
        calculo_porcentaje = 10 / 100
        operacion = int(total_pagar_camisas) * float(calculo_porcentaje) 
        total_pagar = int(total_pagar_camisas) - int(operacion)
        print(f"El total a pagar con el 10% de descuento es de {total_pagar}")
else:
    print("Ingresá un número válido.")