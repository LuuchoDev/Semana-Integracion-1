
# Programa: Generador de Tablas de Verdad
# Descripción: Permite al usuario elegir entre distintas operaciones lógicas (AND, OR, XOR, NAND, NOR, IMPLICACION, BICONDICIONAL)
# y muestra la tabla de verdad correspondiente para cada operador lógico seleccionado.

## Menu de elección.
print("Tablas de verdad para operaciones lógicas!")
operador = input("Ingrese el operador lógico (AND, OR, NOT, XOR, NAND, NOR, IMPLICACION, BICONDICIONAL): ").strip().upper()

## Condicional en base al operador lógico elegido.
## Operador lógico AND
if operador == "AND":
    print("\nTabla de verdad para AND")
    print("P\tQ\tP AND Q")
    #Evaluación de todas las combinaciones posibles de P y Q
    for p in [True, False]:
        for q in [True, False]:
            resultado = p and q
            print(f"{int(p)}\t{int(q)}\t{int(resultado)}")
## Operador lógico OR
elif operador == "OR":
    print("\nTabla de verdad para OR")
    print("P\tQ\tP OR Q")
    for p in [True, False]:
        for q in [True, False]:
            resultado = p or q
            print(f"{int(p)}\t{int(q)}\t{int(resultado)}")
## Operador lógico NOT
elif operador == "NOT":
    print("\nTabla de verdad para NOT")
    print("P\tP NOT")
    for p in [True, False]:
        resultado = not p
        print(f"{int(p)}\t{int(resultado)}")
## Operador lógico XOR
elif operador == "XOR":
    print("\nTabla de verdad para XOR")
    print("P\tQ\tP XOR Q")
    for p in [True, False]:
        for q in [True, False]:
            resultado = p != q
            print(f"{int(p)}\t{int(q)}\t{int(resultado)}")
## Operador lógico NAND
elif operador == "NAND":
    print("\nTabla de verdad para NAND")
    print("P\tQ\tP NAND Q")
    for p in [True, False]:
        for q in [True, False]:
            resultado = not (p and q)
            print(f"{int(p)}\t{int(q)}\t{int(resultado)}")
## Operador lógico NOR
elif operador == "NOR":
    print("\nTabla de verdad para NOR")
    print("P\tQ\tP NOR Q")
    for p in [True, False]:
        for q in [True, False]:
            resultado = not (p or q)
            print(f"{int(p)}\t{int(q)}\t{int(resultado)}")
## Operador lógico IMPLICACION
elif operador == "IMPLICACION":
    print("\nTabla de verdad para IMPLICACION")
    print("P\tQ\tP IMPLICACION Q")
    for p in [True, False]:
        for q in [True, False]:
            resultado = (not p) or q
            print(f"{int(p)}\t{int(q)}\t{int(resultado)}")
## Operador lógico BICONDICIONAL
elif operador == "BICONDICIONAL":
    print("\nTabla de verdad para BICONDICIONAL")
    print("P\tQ\tP BICONDICIONAL Q")
    for p in [True, False]:
        for q in [True, False]:
            resultado = p == q
            print(f"{int(p)}\t{int(q)}\t{int(resultado)}")