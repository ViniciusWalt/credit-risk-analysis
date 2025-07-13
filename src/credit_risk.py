import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho robusto para o arquivo CSV
file_path = os.path.join('data', 'credit_data.csv')

# Carregar dados
data = pd.read_csv(file_path)
X = data.drop('default', axis=1)
y = data['default']

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modelo com ajuste de classes desbalanceadas
model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Previsão
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Relatório
print("Relatório de Classificação:")
relatorio = classification_report(y_test, y_pred, zero_division=1)
print(relatorio)

# Salvar relatório em TXT
with open('classification_report.txt', 'w') as f:
    f.write(relatorio)

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Não Inadimplente', 'Inadimplente'],
            yticklabels=['Não Inadimplente', 'Inadimplente'])
plt.title('Matriz de Confusão')
plt.ylabel('Verdadeiro')
plt.xlabel('Previsto')
plt.savefig('confusion_matrix.png')
plt.close()

# Distribuição de probabilidade
plt.figure(figsize=(8, 6))
sns.histplot(y_prob, bins=30, kde=True)
plt.title('Distribuição de Probabilidades de Risco')
plt.xlabel('Probabilidade de Inadimplência')
plt.ylabel('Contagem')
plt.savefig('risk_distribution.png')
plt.close()

print("Relatório salvo como 'classification_report.txt'.")
print("Imagens 'confusion_matrix.png' e 'risk_distribution.png' geradas com sucesso!")
