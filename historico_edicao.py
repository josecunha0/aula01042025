class No:
    def __init__(self, descricao, imagem_id):
        self.descricao = descricao
        self.imagem_id = imagem_id
        self.anterior = None
        self.proximo = None

class HistoricoEdicao:
    def __init__(self):
        self.inicio = None
        self.atual = None
        self.proximo_id = 1  # Contador para auto incremento do ID
        self.acoes_desfeitas = []  # Pilha para armazenar ações desfeitas
    
    def adicionar_acao(self, descricao):
        novo_no = No(descricao, self.proximo_id)
        self.proximo_id += 1
        
        if self.inicio is None:
            self.inicio = novo_no
            self.atual = novo_no
        else:
            novo_no.anterior = self.atual
            self.atual.proximo = novo_no
            self.atual = novo_no
        
        # Limpa a pilha de ações desfeitas quando uma nova ação é adicionada
        self.acoes_desfeitas = []
    
    def desfazer(self):
        if self.atual and self.atual.anterior:
            # Remove a ação atual do histórico
            acao_atual = self.atual
            self.atual = self.atual.anterior
            self.atual.proximo = None
            
            # Armazena a ação removida na pilha de ações desfeitas
            self.acoes_desfeitas.append(acao_atual)
            return True
        return False
    
    def refazer(self):
        if self.acoes_desfeitas:
            # Recupera a última ação desfeita
            acao_refeita = self.acoes_desfeitas.pop()
            
            # Reconecta a ação ao histórico
            acao_refeita.anterior = self.atual
            self.atual.proximo = acao_refeita
            self.atual = acao_refeita
            return True
        return False
    
    def listar_acoes(self):
        if not self.inicio:
            print("Nenhuma ação no histórico")
            return
        
        no_atual = self.inicio
        print("\nHistórico de ações:")
        print("-" * 30)
        
        while no_atual:
            # Marca a ação atual com um asterisco
            if no_atual == self.atual:
                print("*", end=" ")
            else:
                print(" ", end=" ")
            print(f"Descrição: {no_atual.descricao}")
            print(f"ID da Imagem: {no_atual.imagem_id}")
            print("-" * 30)
            no_atual = no_atual.proximo

def menu():
    print("\n=== Sistema de Histórico de Edição de Imagens ===")
    print("1. Adicionar nova ação")
    print("2. Desfazer última ação")
    print("3. Refazer última ação desfeita")
    print("4. Listar histórico")
    print("5. Sair")
    return input("\nEscolha uma opção (1-5): ")

def main():
    historico = HistoricoEdicao()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            descricao = input("Digite a descrição da ação: ")
            historico.adicionar_acao(descricao)
            print("Ação adicionada com sucesso!")
        
        elif opcao == "2":
            if historico.desfazer():
                print("Ação desfeita com sucesso!")
            else:
                print("Não há ações para desfazer!")
        
        elif opcao == "3":
            if historico.refazer():
                print("Ação refeita com sucesso!")
            else:
                print("Não há ações para refazer!")
        
        elif opcao == "4":
            historico.listar_acoes()
        
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main() 