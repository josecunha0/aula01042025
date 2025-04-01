# Fluxograma do Sistema de Histórico de Edição de Imagens

## Estrutura de Dados
```mermaid
classDiagram
    class No {
        +String descricao
        +int imagemId
        +No anterior
        +No proximo
        +__init__(descricao, imagemId)
    }
    
    class Historico {
        +No inicio
        +No atual
        +int proximoId
        +List acoesDesfeitas
        +adicionarAcao(descricao)
        +desfazer()
        +refazer()
        +listarAcoes()
    }
```

## Fluxograma de Operações

### Adicionar Ação
```mermaid
flowchart TD
    A[Início] --> B[Receber descrição]
    B --> C[Criar novo nó com ID auto incrementado]
    C --> D{Lista vazia?}
    D -->|Sim| E[Definir como início]
    D -->|Não| F[Conectar com nó atual]
    E --> G[Limpar pilha de ações desfeitas]
    F --> G
    G --> H[Fim]
```

### Desfazer Ação
```mermaid
flowchart TD
    A[Início] --> B{Existe ação anterior?}
    B -->|Sim| C[Remover ação atual do histórico]
    B -->|Não| D[Retornar erro]
    C --> E[Armazenar ação na pilha de desfeitas]
    E --> F[Fim]
    D --> F
```

### Refazer Ação
```mermaid
flowchart TD
    A[Início] --> B{Pilha de desfeitas vazia?}
    B -->|Não| C[Recuperar última ação desfeita]
    B -->|Sim| D[Retornar erro]
    C --> E[Reconectar ação ao histórico]
    E --> F[Fim]
    D --> F
```

### Listar Ações
```mermaid
flowchart TD
    A[Início] --> B{Lista vazia?}
    B -->|Sim| C[Retornar mensagem]
    B -->|Não| D[Iniciar do primeiro nó]
    D --> E{Existe próximo?}
    E -->|Sim| F[Imprimir nó atual]
    F --> G[Mover para próximo]
    G --> E
    E -->|Não| H[Imprimir último nó]
    H --> I[Fim]
    C --> I
```

## Pseudocódigo das Operações Principais

### Adicionar Ação
```
PROCEDIMENTO adicionarAcao(descricao)
    novoNo <- CRIAR No(descricao, proximoId)
    proximoId <- proximoId + 1
    
    SE inicio = NULO ENTÃO
        inicio <- novoNo
        atual <- novoNo
    SENÃO
        novoNo.anterior <- atual
        atual.proximo <- novoNo
        atual <- novoNo
    FIM SE
    
    acoesDesfeitas <- []  // Limpa pilha de ações desfeitas
FIM PROCEDIMENTO
```

### Desfazer Ação
```
PROCEDIMENTO desfazer()
    SE atual.anterior ≠ NULO ENTÃO
        acaoAtual <- atual
        atual <- atual.anterior
        atual.proximo <- NULO
        acoesDesfeitas.ADICIONAR(acaoAtual)
        RETORNAR VERDADEIRO
    SENÃO
        RETORNAR FALSO
    FIM SE
FIM PROCEDIMENTO
```

### Refazer Ação
```
PROCEDIMENTO refazer()
    SE acoesDesfeitas.NÃO_ESTÁ_VAZIA() ENTÃO
        acaoRefeita <- acoesDesfeitas.REMOVER_ÚLTIMO()
        acaoRefeita.anterior <- atual
        atual.proximo <- acaoRefeita
        atual <- acaoRefeita
        RETORNAR VERDADEIRO
    SENÃO
        RETORNAR FALSO
    FIM SE
FIM PROCEDIMENTO
```

### Listar Ações
```
PROCEDIMENTO listarAcoes()
    SE inicio = NULO ENTÃO
        IMPRIMIR "Nenhuma ação no histórico"
        RETORNAR
    FIM SE
    
    noAtual <- inicio
    IMPRIMIR "Histórico de ações:"
    IMPRIMIR "------------------------------"
    
    ENQUANTO noAtual ≠ NULO FAÇA
        SE noAtual = atual ENTÃO
            IMPRIMIR "*", end=" "
        SENÃO
            IMPRIMIR " ", end=" "
        FIM SE
        IMPRIMIR "Descrição:", noAtual.descricao
        IMPRIMIR "ID da Imagem:", noAtual.imagemId
        IMPRIMIR "------------------------------"
        noAtual <- noAtual.proximo
    FIM ENQUANTO
FIM PROCEDIMENTO 