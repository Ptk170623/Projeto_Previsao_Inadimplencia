from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
import io

from funcoes import preprocessar_dados

# Inicializa a aplicação com título, descrição e versão
app = FastAPI(
    title="API de Risco de Inadimplência",
    description=(
        "Envie uma planilha de dados no formato `.xlsx` (Excel) e receba de volta o arquivo com uma nova coluna indicando o risco de inadimplência do cliente.\n\n"
        "**Instruções de uso:**\n"
        "- Vá até `POST /prever-risco/ Prever Risco`\n"
        "- Clique em `Try it out`\n"
        "- Em `file`, clique em `Escolher arquivo` e envie a planilha Excel\n"
        "- Se quiser usar o modelo padrão e as variáveis padrão, **desmarque** as opções `Send empty value` de `modelo_file` e `features_file`\n"
        "- Abaixo haverá **\"Download file\"** destacado em azul. Clique para fazer o download da nova planilha com a coluna risco de inadimplência.\n"
        "- Caso deseje, você pode também enviar:\n"
        "   - Um modelo `.pkl` no campo `modelo_file`\n"
        "   - Um arquivo `.pkl` com a lista de variáveis (features) no campo `features_file`"
    ),
    version="1.0.0"
)

# Habilita CORS (ideal para testes e para uso com ngrok)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega arquivos padrão
modelo_padrao = joblib.load("modelo_inadimplencia.pkl")
top_features_padrao = pd.read_pickle("top_features.pkl")

@app.post("/prever-risco/")
async def prever_risco(
    file: UploadFile = File(...),
    modelo_file: UploadFile = File(None),
    features_file: UploadFile = File(None)
):
    try:
        # Lê a planilha enviada
        contents = await file.read()
        dados = pd.read_excel(io.BytesIO(contents))

        # Verifica se o modelo customizado foi enviado
        if modelo_file is not None and modelo_file.filename != "":
            modelo_bytes = await modelo_file.read()
            modelo = joblib.load(io.BytesIO(modelo_bytes))
        else:
            modelo = modelo_padrao

        # Verifica se o arquivo de features customizadas foi enviado
        if features_file is not None and features_file.filename != "":
            features_bytes = await features_file.read()
            top_features = pd.read_pickle(io.BytesIO(features_bytes))
        else:
            top_features = top_features_padrao

        # Processa e prevê
        dados_com_risco = preprocessar_dados(dados, modelo, top_features)

        # Cria arquivo de resposta
        output = io.BytesIO()
        dados_com_risco.to_excel(output, index=False)
        output.seek(0)

        return StreamingResponse(
            output,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={'Content-Disposition': 'attachment; filename=resultado_risco.xlsx'}
        )

    except Exception as e:
        return {"erro": str(e)}
