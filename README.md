# Santander Dev Week 2023 - Pipeline ETL com Python

Projeto prático de portfólio desenvolvido para demonstrar o fluxo **ETL**: Extração, Transformação e Carregamento.

A proposta original usava a API pública da Santander Dev Week. Como APIs públicas podem ficar indisponíveis, este projeto foi realizado com um arquivo CSV completo com dados fictícios de usuários.

## Objetivo

Criar um pipeline em Python que:

1. **Extrai** dados de usuários de um arquivo CSV.
2. **Transforma** esses dados, gerando uma mensagem personalizada para cada cliente.
3. **Carrega** o resultado final em novos arquivos de saída.

## Estrutura do projeto

```text
santander-dev-week-etl-portfolio/
├── data/
│   └── users.csv
├── output/
│   └── users_with_messages.csv
├── src/
│   └── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Dados de entrada

O arquivo `data/users.csv` contém dados fictícios:

```csv
id,nome,conta,cartao
1,Ana Souza,0001-9,**** **** **** 1234
2,Carlos Lima,0002-7,**** **** **** 5678
```

## Como executar

Clone o repositório, acesse a pasta do projeto e execute:

```bash
python src/main.py
```

O resultado será salvo em:

```text
output/users_with_messages.csv
output/users_with_messages.json
```

## Exemplo de saída

```csv
id,nome,conta,cartao,mensagem
1,Ana Souza,0001-9,**** **** **** 1234,Ana Souza, organize sua vida financeira...
```

## Conceitos aplicados

- Python
- ETL
- Leitura e escrita de CSV
- Manipulação de dados
- Geração de mensagens personalizadas
- Organização de projeto para GitHub
- Boas práticas de documentação

## Sobre a transformação

A etapa de transformação simula a geração de uma mensagem de educação financeira para cada usuário.  
Em um cenário real, essa etapa poderia ser integrada a uma API de IA generativa.

## Autor

Enzo Zapparolli
Linkedin: https://www.linkedin.com/in/enzo-zapparolli-5b4420348/
