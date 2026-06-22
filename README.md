#Portugues (linha 78)

# BCB Economic Pipeline

A data engineering pipeline that collects real economic data from the Brazilian Central Bank (BCB) public API, transforms it with pandas, loads it into a local database, and exports an annual summary report.

## What it does:
- Fetches historical data for 3 economic indicators (USD exchange rate, SELIC, IPCA) from the BCB public API
- Transforms and standardizes the data using pandas
- Loads the consolidated dataset into a SQLite database
- Exports a CSV report with the annual average per indicator

## Tech Stack

- **Python** — core language
- **requests** — API consumption
- **pandas** — data transformation
- **SQLAlchemy** — database loading
- **SQLite** — local storage

## Project Structure

```
bcb-economic-pipeline/
│
├── data/
│   └── media_anual.csv       # Annual average report
│
├── src/
│   └── pipeline.py           # Main pipeline script
│
├── economico.db              # SQLite database
├── requirements.txt
└── README.md
```

## How to run

1. Clone the repository
```bash
git clone https://github.com/WesleySr21/bcb-economic-pipeline.git
cd bcb-economic-pipeline
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the pipeline
```bash
python src/pipeline.py
```

## Output example

**Console log:**
```
[OK] dolar - 1252 registros coletados
[OK] selic - 1252 registros coletados
[OK] ipca - 60 registros coletados
```

**media_anual.csv:**
| ano | serie | valor |
|-----|-------|-------|
| 2020 | dolar | 5.39 |
| 2020 | ipca | 0.29 |
| 2020 | selic | 4.40 |

## Data Source

[Banco Central do Brasil — Séries Temporais](https://www.bcb.gov.br/estatisticas/tabelaespecial)

---

# Pipeline de Dados Econômicos — BCB

Pipeline de engenharia de dados que coleta indicadores econômicos reais da API pública do Banco Central do Brasil, transforma com pandas, carrega em banco de dados local e exporta um relatório de médias anuais.

## O que faz

- Consome dados históricos de 3 indicadores (Dólar PTAX, SELIC, IPCA) via API pública do BCB
- Transforma e padroniza os dados com pandas
- Carrega o dataset consolidado em banco SQLite
- Exporta CSV com a média anual por indicador

## Tecnologias

- **Python** — linguagem principal
- **requests** — consumo de API
- **pandas** — transformação dos dados
- **SQLAlchemy** — carga no banco
- **SQLite** — armazenamento local

## Estrutura do projeto

```
bcb-economic-pipeline/
│
├── data/
│   └── media_anual.csv       # Relatório de médias anuais
│
├── src/
│   └── pipeline.py           # Script principal do pipeline
│
├── economico.db              # Banco de dados SQLite
├── requirements.txt
└── README.md
```

## Como rodar

1. Clone o repositório
```bash
git clone https://github.com/WesleySr21/bcb-economic-pipeline.git
cd bcb-economic-pipeline
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Execute o pipeline
```bash
python src/pipeline.py
```

## Exemplo de saída

**Log no console:**
```
[OK] dolar - 1252 registros coletados
[OK] selic - 1252 registros coletados
[OK] ipca - 60 registros coletados
```

**media_anual.csv:**
| ano | serie | valor |
|-----|-------|-------|
| 2020 | dolar | 5.39 |
| 2020 | ipca | 0.29 |
| 2020 | selic | 4.40 |
## 📡 Fonte dos dados

[Banco Central do Brasil — Séries Temporais](https://www.bcb.gov.br/estatisticas/tabelaespecial)
