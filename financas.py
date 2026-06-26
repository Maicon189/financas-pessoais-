import json
import os

ARQUIVO_JSON = "lancamentos.json"
ARQUIVO_TXT = "relatorio.txt"


def carregar_dados():
    """Verifica se existe lancamentos.json e carrega ou inicia lista vazia."""
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler arquivo corrompido. Iniciando lista vazia.")
            return []
    return []


def salvar_dados(lancamentos):
    """Salva a lista de lançamentos no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(lancamentos, f, indent=4, ensure_ascii=False)
ef registrar_lancamento(lancamentos):

    while True:
        tipo = input("Digite o tipo [R - Receita / D - Despesa]: ").upper().strip()
        if tipo in ["R", "D"]:
            break
        print("Tipo inválido! Escolha apenas R ou D.")

    while True:
        try:
            valor = float(input("Digite o valor (ex: 150.50): "))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")


    categoria = input("Digite a categoria (ex: Alimentação, Salário): ").strip()
    descricao = input("Digite uma breve descrição: ").strip()


    novo_lancamento = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
    }
    lancamentos.append(novo_lancamento)

    salvar_dados(lancamentos)
    print("Lançamento registrado e salvo com sucesso!")
