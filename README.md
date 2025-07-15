
# 🔍 TechCorp Attrition Prediction Pipeline

## 🧠 Contexto do Problema

A TechCorp Brasil, uma das maiores empresas de tecnologia do país, com mais de 50.000 funcionários, enfrenta uma crise de rotatividade. Em apenas um ano, a taxa de attrition aumentou 35%, gerando prejuízos superiores a R$ 45 milhões.

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

- `dados.csv`: base de dados original
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
```

### Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 💻 Como Usar

### Executar o pipeline completo:

```python
from main_pipeline import run_complete_pipeline
pipeline = run_complete_pipeline(n_samples=50000, balance_strategy='smote')
```

### Fazer predições com o modelo salvo:

```python
from main_pipeline import load_and_use_saved_model
load_and_use_saved_model()
```

### Comparar diferentes estratégias de balanceamento:

```python
from main_pipeline import compare_strategies
compare_strategies()
```

### Usar o pipeline diretamente:

```python
from hr_attrition_pipeline import HRAttritionPipeline
import pandas as pd

pipeline = HRAttritionPipeline(use_gpu=True, balance_strategy='smote')
df = pd.read_csv('seus_dados.csv')
X, y = pipeline.load_and_prepare_data(df)
X_eng = pipeline.create_features(X)
# Seguir com split, treino e avaliação
```

---

## 📊 Principais Resultados

| Modelo              | Precision | Recall | F1-Score | AUC-ROC |
|---------------------|-----------|--------|----------|---------|
| Random Forest        | 0.267     | 0.574  | 0.364    | 0.659   |
| Logistic Regression  | 0.248     | 0.629  | 0.356    | 0.645   |
| LightGBM             | 0.271     | 0.624  | 0.378    | 0.673   |

---

## 📈 Insights Estratégicos

- Funcionários com horas extras recorrentes têm o dobro de chance de sair
- Baixa satisfação no trabalho é o segundo maior fator de risco
- Profissionais sem promoção por 5+ anos estão em grupo de risco
- Funcionários jovens em vendas têm alta probabilidade de attrition

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
