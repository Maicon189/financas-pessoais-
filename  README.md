# App de Finanças Pessoais

[O programa recebe valores dos usuários e suas descrições e guarda essas informações. Então o programa mostra o saldo total, total de receitas, total de despesas e total por categoria. O usuário tem a opção de ver esse relatório na tela do terminal ou em txt]

## Como rodar
Certifique-se de ter o **Python 3** instalado em sua máquina. Você pode verificar digitando o comando abaixo no terminal:
```bash
python financas.py
```

## Funcionalidades

- [O menu conta com 5 opções
1- Opção de registrar receita e despesas
2- Lista todos lançamentos com o tipo, categoria e breve descrição
3- Saldo total, total de receitas, total de despesas e total por categoria
4- Gera um arquivo com os lançamentos em relatorio.txt
5- Sair do programa ]

## Funções implementadas

| Função | Responsabilidade |
|--------|-----------------|
| carregar() | [Verifica a existência do arquivo JSON, trata dados corrompidos e carrega o histórico financeiro.] |
| salvar() | [Escreve e atualiza a lista de transações de forma estruturada no armazenamento local.] |
| registrar_lancamento() | [Captura e valida as entradas do usuário, impedindo valores negativos ou tipos inválidos.] |
| exibir_extrato() | [ Imprime o histórico detalhado de movimentações com identificação visual de ganhos e gastos] |
| calcular_saldo() | [ Executa os cálculos matemáticos de receitas, despesas, saldo final e agrupamento por categoria.] |
| gerar_relatorio() | [Une os dados calculados em um texto legível e carimba o momento exato da geração] |
| exportar_relatorio() | [Controla o loop do menu e direciona o fluxo de execução conforme a escolha do usuário (relatorio.txt).] |

## Tecnologias usadas

Python 3 · json · os · datetime

## O que aprendi

[Foi mais dificil para mim iniciar o código sem utilizar 'IA', tentando usar a lógica e os conhecimentos adquiridos até agora. Mas conforme fui olhando para o projeto da calculadora fui vendo semelhanças que poderia usar para poder desenvolver esse projeto de finanças. Ficou claro para mim o menu e as interações com o usuários os demaias códigos tive que pesquisar e aprender a usar. Se eu começasse de de novo o projeto, me atentaria em pegar bem o processo de git e github com commits, e buscaria deixar o meu código mais "limpo" utilizando outros comandos que podem ser explorados.]