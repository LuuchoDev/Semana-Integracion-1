print("\nTabla de verdad para NAND")
print("A\tB\tA NAND B")
for p in [True, False]:
    for q in [False, True]:
        resultado = not (p and q)
        print(f"{p}\t{q}\t{resultado}")