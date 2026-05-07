"""
Pipeline ETL - Santander Dev Week

Este script demonstra um fluxo ETL completo usando dados fictícios em CSV.

Etapas:
1. Extract: lê usuários de data/users.csv
2. Transform: gera mensagens personalizadas de educação financeira
3. Load: salva os dados enriquecidos em CSV e JSON
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, List


ROOT_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT_DIR / "data" / "users.csv"
OUTPUT_CSV = ROOT_DIR / "output" / "users_with_messages.csv"
OUTPUT_JSON = ROOT_DIR / "output" / "users_with_messages.json"


User = Dict[str, str]


def extract_users(file_path: Path) -> List[User]:
    """Lê os dados de usuários a partir de um arquivo CSV."""
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    with file_path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        users = list(reader)

    required_columns = {"id", "nome", "conta", "cartao"}
    missing_columns = required_columns - set(reader.fieldnames or [])

    if missing_columns:
        raise ValueError(
            f"O CSV está sem as colunas obrigatórias: {', '.join(missing_columns)}"
        )

    return users


def generate_financial_message(user: User) -> str:
    """
    Gera uma mensagem personalizada para o usuário.

    Esta função simula uma etapa de IA generativa.
    Em um projeto real, você poderia substituir esta lógica por uma chamada
    a uma API de IA.
    """
    nome = user["nome"].strip()

    return (
        f"{nome}, acompanhe seus gastos, defina metas mensais e use seu cartão "
        "com consciência para fortalecer sua saúde financeira."
    )


def transform_users(users: List[User]) -> List[User]:
    """Adiciona uma mensagem personalizada para cada usuário."""
    transformed_users = []

    for user in users:
        enriched_user = user.copy()
        enriched_user["mensagem"] = generate_financial_message(user)
        transformed_users.append(enriched_user)

    return transformed_users


def load_to_csv(users: List[User], file_path: Path) -> None:
    """Salva os usuários transformados em um arquivo CSV."""
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not users:
        raise ValueError("Não há usuários para salvar.")

    fieldnames = list(users[0].keys())

    with file_path.open(mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)


def load_to_json(users: List[User], file_path: Path) -> None:
    """Salva os usuários transformados em um arquivo JSON."""
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open(mode="w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=2)


def main() -> None:
    """Executa o pipeline ETL completo."""
    print("Iniciando pipeline ETL...")

    users = extract_users(INPUT_FILE)
    print(f"Extração concluída: {len(users)} usuários encontrados.")

    transformed_users = transform_users(users)
    print("Transformação concluída: mensagens personalizadas geradas.")

    load_to_csv(transformed_users, OUTPUT_CSV)
    load_to_json(transformed_users, OUTPUT_JSON)

    print("Carregamento concluído.")
    print(f"Arquivo CSV gerado em: {OUTPUT_CSV}")
    print(f"Arquivo JSON gerado em: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
