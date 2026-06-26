import json
import os

# Nome dos arquivos de persistência
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

