print("Bienvenido")
nombre = input("Ingresá tu nombre: ")
if nombre.isalpha():
    print(f"Hola, {nombre.capitalize()}. Cómo estás?")
else:
    print("No")