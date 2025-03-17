print(r"""
      
 ______     ______     __    __     ______   ______     ______     ______     ______     ______     ______    
/\  ___\   /\  __ \   /\ "-./  \   /\  == \ /\  __ \   /\  == \   /\  __ \   /\  ___\   /\  __ \   /\  __ \   
\ \ \____  \ \ \/\ \  \ \ \-./\ \  \ \  _-/ \ \  __ \  \ \  __<   \ \  __ \  \ \ \____  \ \  __ \  \ \ \/\ \  
 \ \_____\  \ \_____\  \ \_\ \ \_\  \ \_\    \ \_\ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_____/   \/_/  \/_/   \/_/     \/_/\/_/   \/_/ /_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/ 
                                                                                                              

      """)

def consolidar_tarefas(equipe_a, equipe_b, tarefa_remover):
    # Unir as listas de tarefas
    tarefas_consolidadas = equipe_a.union(equipe_b)
    
    # Remover a tarefa especificada, se estiver presente
    tarefas_consolidadas.discard(tarefa_remover)
    
    return tarefas_consolidadas

# Listas de tarefas das equipes
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

# Solicitar a tarefa a ser removida
tarefa_remover = input("Digite a tarefa que deseja remover: ")

# Consolidar as tarefas
tarefas_finais = consolidar_tarefas(equipe_a, equipe_b, tarefa_remover)

# Exibir as tarefas finais
print("Tarefas finais:", tarefas_finais)