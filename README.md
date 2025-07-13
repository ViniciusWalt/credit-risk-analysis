# Sistema de Análise de Risco de Crédito

## Descrição
Este projeto implementa um sistema básico de análise de risco de crédito usando aprendizado de máquina. Ele utiliza Python com bibliotecas como `scikit-learn` para prever a inadimplência de mutuários com base em dados como idade, renda e histórico de crédito, gerando relatórios e visualizações.

## Requisitos
- Python 3.11.13
- Dependências:
  - `pandas==1.5.3`
  - `scikit-learn==1.5.1`
  - `matplotlib==3.7.1`
  - `seaborn==0.12.2`
  - `numpy==1.24.3`

## Instalação
1. Instale Python 3.11.13 de [python.org](https://www.python.org/downloads/).
2. Clone o repositório:
   ```bash
   git clone <seu-repositorio>
   cd SARC
   ```
3. Crie e ative o ambiente virtual:
   ```powershell
   py -3.11 -m venv env
   .\env\Scripts\activate
   ```
4. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```

## Uso
1. Prepare um arquivo `credit_data.csv` com colunas: `idade`, `renda`, `historico_credito`, `divida`, `default` (0 ou 1).
2. Execute o script:
   ```powershell
   python src\credit_risk.py
   ```
3. Resultados:
   - Relatório de classificação no terminal e em `classification_report.txt`.
   - Imagens `confusion_matrix.png` e `risk_distribution.png` no diretório.

## Estrutura do Projeto
- `src/credit_risk.py`: Script principal para análise de risco.
- `credit_data.csv`: Dataset de entrada.
- `requirements.txt`: Lista de dependências.
- `env/`: Ambiente virtual (ignorado pelo Git).

## Contribuição
- Adicione mais dados ao `credit_data.csv` para melhorar a robustez do modelo.
- Sugira melhorias no código (ex.: outros algoritmos como RandomForest).

## Histórico
- **13/07/2025**: Projeto concluído com sucesso, utilizando Python 3.11.13 e dependências compatíveis.