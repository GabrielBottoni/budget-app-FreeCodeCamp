# 💰 Budget App

Um aplicativo de orçamento desenvolvido em **Python** como parte dos estudos de Programação Orientada a Objetos (POO) no [freeCodeCamp](https://www.freecodecamp.org/).

O projeto permite criar categorias de orçamento, registrar depósitos e saques, realizar transferências entre categorias e visualizar um gráfico com a porcentagem dos gastos de cada categoria.

## 📌 Sobre o projeto

A proposta deste exercício foi colocar em prática conceitos fundamentais de **Programação Orientada a Objetos em Python**, utilizando uma classe `Category` para representar diferentes categorias de orçamento.

Cada categoria possui seu próprio livro-caixa (`ledger`), onde são armazenadas as transações realizadas.

Além do controle das transações, o projeto também possui uma função responsável por gerar um gráfico de barras mostrando a distribuição percentual dos gastos entre as categorias.

## 🚀 Funcionalidades

* Criar categorias de orçamento
* Registrar depósitos
* Registrar saques
* Consultar o saldo atual
* Verificar disponibilidade de fundos
* Transferir valores entre categorias
* Exibir o histórico de transações
* Gerar um gráfico percentual dos gastos
* Formatar os valores e descrições conforme os requisitos do projeto

## 🧠 Conceitos praticados

Durante o desenvolvimento, foram praticados principalmente:

* Classes e objetos
* Atributos de instância
* Métodos
* `self`
* `__init__`
* `__str__`
* Listas
* Dicionários
* Estruturas condicionais
* Loops
* Funções
* F-strings
* Formatação de strings
* Manipulação de valores numéricos
* Programação Orientada a Objetos

## 🏗️ Estrutura principal

### `Category`

A classe `Category` representa uma categoria de orçamento.

```python
food = Category("Food")
```

Cada categoria possui um `ledger` próprio para armazenar suas transações:

```python
food.ledger
```

### Depósitos

Os depósitos são registrados como valores positivos:

```python
food.deposit(1000, "initial deposit")
```

### Saques

Os saques são registrados como valores negativos e só acontecem quando existe saldo suficiente:

```python
food.withdraw(50, "groceries")
```

### Transferências

Também é possível transferir dinheiro entre categorias:

```python
food.transfer(50, clothing)
```

A transferência registra automaticamente uma saída na categoria de origem e uma entrada na categoria de destino.

### Gráfico de gastos

A função:

```python
create_spend_chart(categories)
```

calcula a porcentagem dos gastos de cada categoria considerando apenas os valores retirados e gera um gráfico de barras em texto.

## 📊 Exemplo

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")

clothing = Category("Clothing")

food.transfer(50, clothing)

print(food)
```

Saída:

```text
*************Food*************
initial deposit        1000.00
groceries               -10.15
Transfer to Clothing    -50.00
Total: 939.85
```

## 📚 Principais aprendizados

Um dos principais aprendizados deste projeto foi entender melhor como uma classe pode representar uma entidade e manter seu próprio estado.

Também foi importante compreender na prática a diferença entre:

* **classe**
* **instância**
* **atributos**
* **métodos**
* **`self`**

Outro ponto interessante foi trabalhar com os testes do desafio. Pequenos detalhes, como formatação de strings, quantidade de espaços, valores negativos e quebras de linha, podem fazer um teste falhar mesmo quando a lógica principal está funcionando.

Isso reforçou a importância de não olhar apenas para o resultado final, mas também para os requisitos específicos que o código precisa cumprir.

## 🛠️ Tecnologias

* Python
* Programação Orientada a Objetos
* freeCodeCamp

## 🎯 Objetivo

Este projeto faz parte da minha jornada de fortalecimento dos fundamentos de **Python e Programação Orientada a Objetos**, servindo como mais um exercício prático para consolidar conceitos antes de avançar para projetos mais complexos.

---

**Desenvolvido por Gabriel Bottoni**
