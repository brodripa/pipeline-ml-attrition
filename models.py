import os

os.makedirs('models', exist_ok=True)
os.makedirs('results', exist_ok=True)

import joblib

# Após treinar seu modelo
joblib.dump(model, f'models/{model_name}_model.joblib')

import json
from datetime import datetime

# Exemplo de dicionário de resultados (como no seu prompt)
model_results = {
    "model_name": "LightGBM",
    "metrics": {...},
    "best_params": {...},
    "feature_names": [...],
    "training_date": datetime.now().isoformat()
}

# Salvar resultados do modelo
with open(f'results/{model_results["model_name"]}_results.json', 'w', encoding='utf-8') as f:
    json.dump(model_results, f, ensure_ascii=False, indent=2)

all_results = {
    "metadata": {...},
    "results": {...}
}

with open('results/summary_results.json', 'w', encoding='utf-8') as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)