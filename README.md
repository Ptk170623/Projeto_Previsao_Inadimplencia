# Projeto_Previsao_Inadimplencia

Neste projeto, usei Machine Learning para prever a inadimplência em empréstimos de uma empresa, contribuindo para a tomada de decisão. Os insights deste projeto e uma explicação não técnica estão disponível no meu blog técnico: https://medium.com/@patricksilvalessa5

## **Processo do Projeto:**
### Análise Exploratória:

A análise exploratória de dados (EDA) foi realizada para conhecermos melhor os dados e identificando padrões, valores ausentes, outliers e selecionando e criando variáveis que poderiam ser relevantes para o modelo.

### Técnicas Estatísticas:

Utilizei técnicas estatísticas para entender a relação das variáveis numéricas e categóricas com a variável alvo e para descobrir multicolinearidade e variáveis com poder preditivo.

### Modelos de Classificação:

Diversos modelos de classificação foram testados, incluindo algoritmos de ensemble models, como AdaBoost e GradienteBoost. Todos os modelos foram avaliados e comparados usando métricas como precisão, recall, F1-score e a média das AUC-ROC.

Diversos modelos de classificação foram testados e validados com as principais métricas, incluindo validação cruzada e a matriz de confusão.

### Validação:

Utilizei validação cruzada para garantir que a robustez e generalização do modelo, minimizando o risco de overfitting.

A matriz de confusão foi usada para analisar o desempenho dos modelos e identificar possíveis áreas de melhoria, como falsos positivos e falsos negativos.

### Escolha do Modelo Final:

Após a comparação de todos os modelos e a análise de suas métricas de desempenho, foi escolhido o modelo mais eficaz para a previsão de inadimplência.

### Implementação:

O modelo foi implementado em uma API que recebe um arquivo com as informações dos clientes e retorna o arquivo com uma nova coluna "Risco" que indica se o cliente possui baixo, médio, alto ou muito alto risco de inadimplência. Para usar a API leia o README da pasta notebooks/API

### Conclusão

Com essa informação preditiva, diversas abordagens podem ser seguidas para a tomada de decisão. Por exemplo, a empresa pode criar estratégias de cobrança antecipada para clientes com alto risco de inadimplência, ajustar as condições de empréstimo e também diminuir o limite de crédito desses clientes.

Com a aplicação deste projeto, um problema que gera grandes prejuízos para as empresas da área financeira é resolvido por meio da implementação de um modelo de classificação, capaz de prever o risco de inadimplência de um cliente, permitindo que a empresa tome decisões informadas e use estratégias eficazes para redução de riscos, maior segurança e rentabilidade.
