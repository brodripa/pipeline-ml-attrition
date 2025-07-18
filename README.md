
# 🔍 IBM HR Analytics Attrition Prediction Pipeline

## 🧠 Contexto do Problema

🔍 TechCorp Attrition Prediction Pipeline

🧠 Contexto do Problema

A IBM HR Analytics, uma das maiores empresas de tecnologia do país, com mais de 50.000 funcionários, enfrenta uma crise de rotatividade. Em apenas um ano, a taxa de attrition aumentou 35%, gerando prejuízos superiores a R$ 45 milhões.

Além dos custos diretos de demissão e contratação, a empresa sofre com:

- Perda de conhecimento institucional
- Redução da produtividade
- Baixa na moral das equipes
- Atrasos em projetos estratégicos

A empresa contratou um Cientista de Dados para desenvolver um sistema preditivo de alta performance que ajude o RH a identificar funcionários com alto risco de desligamento, permitindo ações preventivas eficazes.

---

## 🎯 Objetivo

Desenvolver um pipeline completo de Machine Learning para prever a rotatividade de funcionários, utilizando boas práticas de engenharia de atributos, tratamento de dados desbalanceados e avaliação robusta de modelos preditivos.

---

## 📁 Estrutura do Projeto

Todos os arquivos estão organizados no mesmo diretório:

- `base\base.csv`: base de dados original
- `1_hr_analise_estatistica.ipynb`: análise exploratória inicial
- `2_hr_analise_attrition.ipynb`: investigação detalhada da rotatividade
- `3_hr_feature_engineering.ipynb`: criação de novas features
- `4_hr_modelagem_hr_attrition.ipynb`: treinamento e comparação de modelos
- `5_hr_valiacao_attrition.ipynb`: avaliação final dos modelos
- `main_pipeline.py`: execução completa do pipeline
- `hr_attrition_pipeline.py`: classe modular reutilizável
- `README.md`: este documento

---

## ⚙️ Funcionalidades do Pipeline

- Análise estatística e exploração inicial dos dados
- Engenharia de atributos avançada e criação de variáveis compostas
- Balanceamento de classes com SMOTE, undersampling e técnicas híbridas
- Treinamento e comparação de múltiplos algoritmos:
  - Random Forest
  - Regressão Logística
  - LightGBM (com e sem GPU)
- Otimização de hiperparâmetros com Optuna
- Relatórios e visualizações:
  - ROC Curve, Precision-Recall
  - Feature Importance
  - Matriz de Confusão
- Geração de arquivos JSON com resultados e métricas

---

## 🔧 Instalação

### Clone o repositório:

```bash
git clone https://github.com/brodripa/pipeline-ml-attrition
cd techcorp-attrition-pipeline
```

### Crie o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# ou
source venv/bin/activate  # Linux/Mac

---

## 💻 Como Usar

### Cada notebook executa individualmente:

### Fazer predições com o modelo salvo:

```python
# O notebook 4_hr_modelagem_hr_attrition treina e gera os modelos
#  Logistic Regression, Random Forest, XGBoost e CatBoost
```

### Comparar diferentes estratégias de balanceamento:

```python
## 📊 Principais Resultados
# 🏆 Comparativo de desempenho dos modelos:
                     F1-score  Precision    Recall
Logistic Regression  0.478723   0.384615  0.633803
CatBoost             0.403846   0.636364  0.295775
XGBoost              0.385321   0.552632  0.295775
Random Forest        0.336449   0.500000  0.253521
```

### Usar o pipeline diretamente:

```python
=======
Perda de conhecimento institucional

Redução da produtividade

Baixa na moral das equipes

Atrasos em projetos estratégicos

A empresa MackScience desenvolveu um sistema preditivo de alta performance que ajude o RH a identificar funcionários com alto risco de desligamento, permitindo ações preventivas eficazes.

🎯 Objetivo
Um projeto em Machine Learning para prever a rotatividade de funcionários, utilizando boas práticas de engenharia de atributos, tratamento de dados desbalanceados, e avaliação robusta de modelos preditivos.

📁 Estrutura do Projeto

bash
Copiar
Editar

📦 techcorp-attrition-pipeline

├── base\base.csv

├── notebooks/

│   ├── 1_hr_analise_estatistica.ipynb

│   ├── 2_hr_analise_attrition.ipynb

│   ├── 3_hr_feature_engineering.ipynb

│   ├── 4_hr_modelagem_hr_attrition.ipynb

│   └── 5_hr_valiacao_attrition.ipynb

└── README.md

⚙️ Funcionalidades do Pipeline
Análise estatística e exploração inicial dos dados

Engenharia de atributos avançada e criação de variáveis compostas

Balanceamento de classes com SMOTE, undersampling e técnicas híbridas

Treinamento e comparação de múltiplos algoritmos:

Logistic Regression  
CatBoost            
XGBoost           
Random Forest    
 

Relatórios e visualizações:

Dentro de cada notebook geramos as visualizações graficas dos indicadores.
 - Frequência das categorias
 - Análise de Outliers com Boxplots
 - Mapa de Calor de Correlação
 - Gráficos de Boxplot e Barras
---

## 📈 Insights Estratégicos

4. Insight de Negócio
🔁 1. Funcionários que fazem horas extras (OverTime) têm risco significativamente maior de sair Observação: A maioria dos desligamentos ocorre entre funcionários que fazem horas extras regularmente.

Possível causa: Sobrecarga de trabalho, estresse ou insatisfação com o equilíbrio entre vida pessoal e profissional.

Ação recomendada: Monitorar e limitar carga de trabalho excessiva. Oferecer programas de bem-estar e pausas programadas para essas equipes.

💸 2. Funcionários com menor renda mensal (MonthlyIncome) apresentam maior attrition Observação: Os desligamentos são mais comuns em funcionários com renda abaixo da mediana.

Possível causa: Percepção de desvalorização, oportunidades melhores no mercado ou insatisfação financeira.

Ação recomendada: Avaliar políticas salariais para cargos críticos e oferecer bônus de retenção estratégicos para talentos com baixo salário.

🕒 3. Funcionários com pouco tempo de casa (YearsAtCompany < 3 anos) têm maior probabilidade de sair Observação: Muitos dos desligamentos ocorrem nos primeiros anos de empresa.

Possível causa: Falta de integração, treinamento inadequado ou desalinhamento de expectativas no onboarding.

Ação recomendada: Fortalecer o processo de integração e acompanhamento nos primeiros 12–24 meses de trabalho com mentoring, feedbacks e desenvolvimento individualizado.

👶 4. Funcionários mais jovens (Age < 30 anos) demonstram maior propensão ao desligamento Observação: A taxa de attrition é mais alta entre jovens profissionais.

Possível causa: Maior mobilidade de carreira, insatisfação com plano de crescimento ou incompatibilidade cultural.

Ação recomendada: Criar planos de carreira acelerados, envolver esse público com programas de inovação e desafios internos.

---

## 📌 Requisitos

- Python 3.8+
- 8GB RAM (mínimo), 16GB recomendado
- GPU (opcional) para acelerar o LightGBM

---

## 🤝 Contribuições

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do repositório
2. Crie uma branch:
   ```bash
   git checkout -b feature/SuaFeature
   ```
3. Commit:
   ```bash
   git commit -m 'Minha contribuição'
   ```
4. Push:
   ```bash
   git push origin feature/SuaFeature
   ```
5. Abra um Pull Request 🚀

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
=======

Requesitos e bibliotecas

pandas
numpy
matplotlib
seaborn
sklearn.model_selection
sklearn.preprocessing
sklearn.metrics
sklearn.linear_model
sklearn.ensemble
xgboost
catboost
imblearn.over_sampling


