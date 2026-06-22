import requests
import pandas as pd
import sqlalchemy

url_dict = {
    "dolar": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=01/01/2020&dataFinal=31/12/2024",
    "ipca": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2020&dataFinal=31/12/2024",
    "selic": "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2020&dataFinal=31/12/2024"
}

def extrair_series(urls):
    """Processo que aplica as mesmas alterações em todos os dados coletados
    Converte campos, valida quantidade de dados por cada URL e transforma tudo em um DataFrame"""
    success = []
    errors = []

    for serie, url in urls.items():

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(data)

            df["data"] = pd.to_datetime(
                df["data"],
                format="%d/%m/%Y"
            )

            df["valor"] = df["valor"].astype(float).round(2)
            df["serie"] = serie
            success.append(df)
            print(f'[OK] {serie} - {df.shape[0]} registros coletados')

        else:
            print(f'[ERRO] {serie} - {response.status_code}')
            errors.append(
                {
                    "serie": serie,
                    "url": url,
                    "status_code": response.status_code
                }
            )

    return success, errors

dfs, errors = extrair_series(url_dict)

all_dfs = pd.concat(dfs).reset_index(drop=True)

engine = sqlalchemy.create_engine("sqlite:///economico.db")
all_dfs.to_sql('indicadores_economicos', engine, index=False, if_exists='replace')

media_anual = (all_dfs.groupby([all_dfs['data'].dt.year, 'serie'])['valor']
    .mean()
    .reset_index()
)
media_anual = media_anual.rename(columns={'data': 'ano'})
media_anual.to_csv('media_anual.csv', index=False)
