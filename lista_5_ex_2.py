clientes_A = {"Alice", "Bob", "Charlie", "David"}
clientes_B = {"Charlie", "David", "Eve", "Frank"}

print("Clientes em ambos os conjuntos: ", clientes_A & clientes_B)
print("Clientes apenas em clientes_A: ", clientes_A - clientes_B)
print("Clientes em apenas um dos conjuntos:", clientes_A ^ clientes_B)
todos_clientes = clientes_A | clientes_B
print("Porcentagem de clientes únicos: ", (len(todos_clientes) / (len(clientes_A) + len(clientes_B))) * 100, '%')



# Identificar os clientes que estão em ambos os conjuntos.
# Identificar os clientes que estão apenas em clientes_A.
# Identificar os clientes que estão em apenas um dos conjuntos.
# Calcular a porcentagem de clientes únicos.
