# Calculadora de Investimento

Esta classe Python foi desenvolvida para simular o crescimento de um investimento ao longo do tempo, levando em consideração aportes mensais, taxas de juros e metas de atingir determinados valores acumulados.

## Como Usar

1. **Configurações Iniciais:**

    - `valor_inicial`: O valor inicial investido.
    - `valor_mensal`: O valor a ser investido mensalmente.
    - `taxa_juros_anual`: A taxa de juros anual.
    
2. **Configurações de Alvos:**
   - Defina pelo menos um alvo a ser atingido
   - Você pode definir mais de um alvo, mas o investimento será calculado até que o primeiro alvo seja atingido.
   - Defina um alvo como 0 para desativá-lo
   
3. **Execução e Impressão de Resultados:**
```bash
 python calculadora_independencia_financeira.py
```   

## Visualização de Gráficos e Tabelas

Certifique-se de ter a biblioteca `matplotlib` e `tabulate` instaladas para visualizar os gráficos e tabelas.

```bash
pip install matplotlib
pip install tabulate
```
Caso não tenha o resultado será impresso no terminal de forma mais simples.
