nota = float(input("Digite sua nota: "))

if nota >= 9:
    print("Desempenho: Excelente (A)")
elif nota >= 8:
    print("Desempenho: Muito Bom (B)")
elif nota >= 7:
    print("Desempenho: Bom (C)")
elif nota >= 6:
    print("Desempenho: Regular (D)")
elif nota >= 5:
    print("Desempenho: Insuficiente (E)")
else:
    print("Desempenho: Reprovado (F)")
