import pandas as pd

def classificar_risco(dados, modelo):
    features = modelo.feature_names_in_
    dados_modelo = dados[features]
    probs = modelo.predict_proba(dados_modelo)[:, 1]

    def classificar_risco_individual(prob):
        if prob < 0.3:
            return 'Baixo'
        elif prob < 0.5:
            return 'Médio'
        elif prob < 0.7:
            return 'Alto'
        else:
            return 'Muito Alto'

    resultado = pd.DataFrame({'Risco': [classificar_risco_individual(p) for p in probs]})
    return resultado

def preprocessar_dados(dados, modelo, top_features):
    dados_originais = dados.copy()

    if 'Idade' in dados.columns:
        bins = [0, 29, 45, 59, 100]
        labels = ['Menos de 30', '30 a 45', '46 a 60', 'Mais de 60']
        dados['Faixa_etaria'] = pd.cut(dados['Idade'], bins=bins, labels=labels)

    if 'Renda' in dados.columns:
        bins = [0, 25000, 50000, 75000, 100000, 1000000]
        labels = ['Até 25K', 'De 25K a 50K', 'De 50K a 75K', 'De 75K a 100K', 'Mais de 100K']
        dados['Faixa_salarial'] = pd.cut(dados['Renda'], bins=bins, labels=labels)

    dados = dados.dropna()

    colunas_categoricas = dados.select_dtypes(include=['object', 'category']).columns
    colunas_categoricas_com_mais_de_30_valores = [col for col in colunas_categoricas if dados[col].nunique() > 30]
    dados = dados.drop(columns=colunas_categoricas_com_mais_de_30_valores)

    colunas_com_poucos_valores = [col for col in colunas_categoricas if col not in colunas_categoricas_com_mais_de_30_valores]
    dados = pd.get_dummies(dados, columns=colunas_com_poucos_valores, drop_first=True)

    colunas_relevantes = [col for col in top_features.index if col in dados.columns]
    dados_filtrados = dados[colunas_relevantes]

    dados_filtrados = dados_filtrados.copy()
    dados_filtrados.loc[:, 'Risco'] = classificar_risco(dados_filtrados, modelo)['Risco']
    dados_originais['Risco'] = dados_filtrados['Risco'].values

    return dados_originais
