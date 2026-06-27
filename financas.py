from datetime import datetime
import json
import os

ARQUIVO_JSON = "lancamentos.json"
ARQUIVO_TXT = "relatorio.txt"


def carregar_dados():
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler arquivo. Iniciando lista vazia.")
            return []
    return []


def salvar_dados(lancamentos):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(lancamentos, f, indent=4, ensure_ascii=False)


def registrar_lancamento(lancamentos):
    while True:
        tipo = input("Digite o tipo [1 - Receita / 2 - Despesa]: ").upper().strip()
        if tipo in ["1", "2"]:
            break
        print("Tipo inválido! Escolha apenas 1 ou 2.")

    while True:
        try:
            valor = float(input("Digite o valor (ex: 500): "))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Opção inválida! Digite apenas números.")

    categoria = input("Digite a categoria (ex: Transporte, Salário): ").strip()
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


def exibir_extrato(lancamentos):
    if not lancamentos:
        print("\n[Aviso] Nenhum lançamento encontrado. O extrato está vazio.")
        return

    print("\n EXTRATO DE LANÇAMENTOS ")
    for i, lanc in enumerate(lancamentos, 1):
        sinal = "+" if lanc["tipo"] == "1" else "-"
        tipo_str = "Receita" if lanc["tipo"] == "1" else "Despesa"
        print(
            f"{i}. [{tipo_str}] {lanc['categoria']} ({lanc['descricao']}): {sinal}R$ {lanc['valor']:.2f}"
        )
    print("\n")


def processar_relatorio(lancamentos):
    total_receitas = sum(l["valor"] for l in lancamentos if l["tipo"] == "1")
    total_despesas = sum(l["valor"] for l in lancamentos if l["tipo"] == "2")
    saldo_final = total_receitas - total_despesas

    por_categoria = {}
    for l in lancamentos:
        cat = l["categoria"]
        sinal = 1 if l["tipo"] == "1" else -1
        por_categoria[cat] = por_categoria.get(cat, 0.0) + (l["valor"] * sinal)

    return total_receitas, total_despesas, saldo_final, por_categoria


def formatar_texto_relatorio(receitas, despesas, saldo, categorias):
    data_geracao = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    linhas = [
        " RELATÓRIO FINANCEIRO ",
        f"Gerado em: {data_geracao}",  # Inserido para aproveitar a variável
        "-----------------------------------",
        f"Total de Receitas: R$ {receitas:.2f}",
        f"Total de Despesas: R$ {despesas:.2f}",
        f"Saldo Final: R$ {saldo:.2f}",
        "-----------------------------------",
        "Resumo por Categoria (Saldo líquido):",
    ]
    for cat, valor_cat in categorias.items():
        linhas.append(f"  - {cat}: R$ {valor_cat:.2f}")
    linhas.append("")
    return "\n".join(linhas)


def principal():
    lancamentos = carregar_dados()
    while True:
        print("\n MENU PRINCIPAL:")
        print("[1] Registrar Lançamento")
        print("[2] Exibir Extrato")
        print("[3] Exibir Relatório na Tela")
        print("[4] Exportar Relatório para Arquivo TXT")
        print("[5] Sair")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            registrar_lancamento(lancamentos)
        elif opcao == "2":
            exibir_extrato(lancamentos)
        elif opcao == "3" or opcao == "4":
            if not lancamentos:
                print("\n[Aviso] Não há dados para gerar relatórios.")
                continue

            rec, desp, saldo, cats = processar_relatorio(lancamentos)
            texto_relatorio = formatar_texto_relatorio(rec, desp, saldo, cats)

            if opcao == "3":
                print("\n" + texto_relatorio + "\n")
            elif opcao == "4":
                with open(ARQUIVO_TXT, "w", encoding="utf-8") as f:
                    f.write(texto_relatorio)
                print(
                    f"\nRelatório exportado com sucesso para '{ARQUIVO_TXT}'!"
                )
        elif opcao == "5":
            print("\nSaindo do programa. Até logo!")
            break



if __name__ == "__main__":
    principal()
