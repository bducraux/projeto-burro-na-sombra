# Calculadora para Independência Financeira

Esta classe Python foi desenvolvida para simular o crescimento de um investimento ao longo do tempo, levando em consideração aportes mensais, taxas de juros e metas de atingir determinados valores acumulados.

## Como Usar

### Configurações Iniciais:

- `valor_inicial`: Valor inicial investido.
- `valor_mensal`: Valor a ser investido mensalmente.
- `taxa_juros_anual`: Taxa de juros anual.

### Configurações de Alvos:
- Defina pelo menos um alvo a ser atingido
- Você pode definir mais de um alvo, mas o investimento será calculado até que o primeiro alvo seja atingido.
- Defina um alvo como 0 para desativá-lo

**Possíveis alvos:**

| Alvo               |                       Descrição                        |
|--------------------|:------------------------------------------------------:|
| periodo_alvo_anos  |        Alvo de período de investimento em anos         |
| salario_alvo       |                  Alvo de renda mensal                  |
| valor_total_alvo   |             Alvo de valor total acumulado              |



### Execução e Impressão de Resultados:
```bash
 python calculadora_independencia_financeira.py
```   

### Instalação de Dependências:
```bash
 pip install -r requirements.txt
```

### Testes:
```bash
 pytest -v
```