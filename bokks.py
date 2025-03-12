livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

livro_procurado = "O Hobbit"

# Função para buscar o livro
def buscar_livro(livros, livro_procurado):
    for livro in livros:
        if livro == livro_procurado:
            print(f"Livro encontrado: {livro}")
            break 

buscar_livro(livros, livro_procurado)