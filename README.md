# Sistema de Histórico de Edição de Imagens

Este projeto implementa um sistema de histórico de edição de imagens utilizando uma lista duplamente encadeada. O sistema permite que usuários de um aplicativo de edição de imagens mantenham um registro de suas ações e possam desfazer/refazer operações de forma eficiente.

## Funcionalidades

- Adicionar novas ações ao histórico (com ID auto incrementado)
- Desfazer a última ação realizada (remove a ação do histórico)
- Refazer a última ação desfeita (restaura a ação removida)
- Listar todas as ações realizadas com indicação da ação atual

## Estrutura do Projeto

- `historico_edicao.py`: Implementação principal da lista duplamente encadeada
- `Fluxograma.md`: Documentação visual do fluxo do sistema
- `README.md`: Este arquivo de documentação

## Como Usar

Para executar o projeto, basta rodar o arquivo principal:

```bash
python historico_edicao.py
```

O programa oferece um menu interativo com as seguintes opções:
1. Adicionar nova ação (apenas descrição é necessária, ID é gerado automaticamente)
2. Desfazer última ação (remove a ação atual do histórico)
3. Refazer última ação desfeita (restaura a última ação removida)
4. Listar histórico (mostra todas as ações com indicação da ação atual)
5. Sair

## Implementação

O projeto foi implementado utilizando duas classes principais:

1. `No`: Representa um nó da lista duplamente encadeada, contendo:
   - Descrição da ação
   - ID da imagem (gerado automaticamente)
   - Referência para o nó anterior
   - Referência para o próximo nó

2. `HistoricoEdicao`: Gerencia o histórico de ações, implementando:
   - Contador de ID auto incrementado
   - Pilha de ações desfeitas
   - Adição de novas ações
   - Desfazer última ação (remove e armazena)
   - Refazer última ação desfeita (restaura da pilha)
   - Listagem do histórico

## Características Especiais

- IDs são gerados automaticamente (1, 2, 3, ...)
- Ações desfeitas são armazenadas em uma pilha
- Ao adicionar uma nova ação, todas as ações desfeitas são descartadas
- O histórico mostra um asterisco (*) indicando a ação atual
- Interface interativa para fácil manipulação do histórico

## Requisitos

- Python 3.4 +