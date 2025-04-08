Esta aplicação fornece uma API construída com FastAPI para prever o risco de inadimplência de clientes com base em uma planilha de dados dos clientes. O modelo de Machine Learning utilizado pode ser o padrão ou customizado, assim como o conjunto de variáveis (features).

## Estrutura do arquivo:
API/ 
- app.py # Arquivo com os códigos utilizando a biblioteca FastAPI
- funcoes.py # Funções de pré-processamento e predição criadas para implementar o modelo
- modelo_inadimplencia.pkl # Modelo de ML padrão (XGBoost)
- top_features.pkl # Lista das variáveis mais relevantes utilizadas no modelo padrão 
- requirements.txt # Dependências do projeto
- README.md # Este arquivo

## Usar a API de forma remota
É possível usar a API apenas acessando o link disponibilizado pelo Ngrok, porém esse link precisa ser reativado a cada 8 horas, então entre em contado e irei reativá-lo.

## Como Rodar a API Localmente
1. Clone o repositório e entre na pasta da API:
git clone https://github.com/Ptk170623/Projeto_Previsao_Inadimplencia.git
cd Projeto_Previsao_Inadimplencia/notebooks/API

2. (Recomendado) Crie e ative um ambiente virtual:
python -m venv venv
venv\Scripts\activate   # No Windows
# ou
source venv/bin/activate  # No Linux/macOS

3. Instale as dependências:
pip install -r requirements.txt

4. Execute a API com o Uvicorn:
uvicorn app:app --reload

5. Acesse a documentação interativa no navegador:
http://127.0.0.1:8000/docs

Na interface da API haverá uma descrição mostrando como usa-la e dentro da pasta API há uma amostra de novos dados que podem ser usados para testar a API.