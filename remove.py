# Solicita os pedidos feitos
pedidos_input = input("Pedidos feitos (separados por vírgula): ")

# Converte a string de pedidos em uma lista
pedidos = [pedido.strip() for pedido in pedidos_input.split(',')]

# Exibe a lista de pedidos antes da remoção
print(f"Pedidos feitos: {pedidos}")

# Remove o último pedido
if pedidos:  # Verifica se a lista não está vazia
    pedidos.pop()

# Exibe a lista de pedidos finais
print(f"Pedidos finais: {pedidos}")