import pytest
from calculadora_independencia_financeira import CalculadoraIndependenciaFinanceira
from utils import calcular_anos_meses


@pytest.fixture
def investimento_1_ano():
    investimento = CalculadoraIndependenciaFinanceira()
    investimento.configurar_investimento(0, 1000, 8)
    investimento.configurar_alvos(1, 0, 0)
    investimento.calcular_investimento()
    return investimento


@pytest.fixture
def investimento_salario_alvo_5000():
    investimento = CalculadoraIndependenciaFinanceira()
    investimento.configurar_investimento(0, 1000, 8)
    investimento.configurar_alvos(0, 5000, 0)
    investimento.calcular_investimento()
    return investimento


@pytest.fixture
def investiomento_valor_alvo_1000000():
    investimento = CalculadoraIndependenciaFinanceira()
    investimento.configurar_investimento(0, 1000, 8)
    investimento.configurar_alvos(0, 0, 1000000)
    investimento.calcular_investimento()
    return investimento


def test_calculo_anos_meses():
    assert calcular_anos_meses(0) == ''
    assert calcular_anos_meses(1) == '1 mês'
    assert calcular_anos_meses(2) == '2 meses'
    assert calcular_anos_meses(12) == '1 ano'
    assert calcular_anos_meses(13) == '1 ano e 1 mês'
    assert calcular_anos_meses(14) == '1 ano e 2 meses'
    assert calcular_anos_meses(25) == '2 anos e 1 mês'
    assert calcular_anos_meses(26) == '2 anos e 2 meses'
    assert calcular_anos_meses(37) == '3 anos e 1 mês'
    assert calcular_anos_meses(38) == '3 anos e 2 meses'
    assert calcular_anos_meses(24) == '2 anos'
    assert calcular_anos_meses(36) == '3 anos'


def test_calculo_investimento_1_ano(investimento_1_ano):
    # Adicione aqui os testes específicos para verificar se os cálculos estão corretos
    # Por exemplo, você pode verificar se o total_acumulado está aumentando corretamente a cada mês
    expected_total_investido = 11000
    expected_total_acumulado = 11358.85
    expected_juros = 65.88
    expected_total_juros = 358.85

    assert investimento_1_ano.historico[-1]['total_investido'] == expected_total_investido
    assert investimento_1_ano.historico[-1]['total_acumulado'] == expected_total_acumulado
    assert investimento_1_ano.historico[-1]['juros'] == expected_juros
    assert investimento_1_ano.historico[-1]['total_juros'] == expected_total_juros

    assert round(investimento_1_ano.total_investido, 2) == expected_total_investido
    assert round(investimento_1_ano.total_acumulado, 2) == expected_total_acumulado
    assert round(investimento_1_ano.juros, 2) == expected_juros
    assert round(investimento_1_ano.total_juros, 2) == expected_total_juros

    # Verifique se os alvos foram atingidos corretamente
    assert investimento_1_ano.alvo_atingido['periodo']['atingido'] is True


def test_calculo_investimento_salario_alvo_5000(investimento_salario_alvo_5000):
    # Adicione aqui os testes específicos para verificar se os cálculos estão corretos
    # Por exemplo, você pode verificar se o total_acumulado está aumentando corretamente a cada mês
    expected_total_investido = 282000
    expected_total_acumulado = 788109.06
    expected_juros = 5005.46
    expected_total_juros = 506109.06

    assert investimento_salario_alvo_5000.historico[-1]['total_investido'] == expected_total_investido
    assert investimento_salario_alvo_5000.historico[-1]['total_acumulado'] == expected_total_acumulado
    assert investimento_salario_alvo_5000.historico[-1]['juros'] == expected_juros
    assert investimento_salario_alvo_5000.historico[-1]['total_juros'] == expected_total_juros

    assert round(investimento_salario_alvo_5000.total_investido, 2) == expected_total_investido
    assert round(investimento_salario_alvo_5000.total_acumulado, 2) == expected_total_acumulado
    assert round(investimento_salario_alvo_5000.juros, 2) == expected_juros
    assert round(investimento_salario_alvo_5000.total_juros, 2) == expected_total_juros

    # Verifique se os alvos foram atingidos corretamente
    assert investimento_salario_alvo_5000.alvo_atingido['salario']['atingido'] is True
    assert investimento_salario_alvo_5000.alvo_atingido['salario']['info'] == ('Salário alvo atingido em 23 anos e 7 '
                                                                               'meses')
    # testa se o período investido bate com o informado no alvo
    assert investimento_salario_alvo_5000.historico[-1]['mes'] == 283
    assert calcular_anos_meses(investimento_salario_alvo_5000.historico[-1]['mes']) == '23 anos e 7 meses'


def test_calculo_investimento_valor_alvo_1000000(investiomento_valor_alvo_1000000):
    # Adicione aqui os testes específicos para verificar se os cálculos estão corretos
    # Por exemplo, você pode verificar se o total_acumulado está aumentando corretamente a cada mês
    expected_total_investido = 314000
    expected_total_acumulado = 1001986.51
    expected_juros = 6365.57
    expected_total_juros = 687986.51

    assert investiomento_valor_alvo_1000000.historico[-1]['total_investido'] == expected_total_investido
    assert investiomento_valor_alvo_1000000.historico[-1]['total_acumulado'] == expected_total_acumulado
    assert investiomento_valor_alvo_1000000.historico[-1]['juros'] == expected_juros
    assert investiomento_valor_alvo_1000000.historico[-1]['total_juros'] == expected_total_juros

    assert round(investiomento_valor_alvo_1000000.total_investido, 2) == expected_total_investido
    assert round(investiomento_valor_alvo_1000000.total_acumulado, 2) == expected_total_acumulado
    assert round(investiomento_valor_alvo_1000000.juros, 2) == expected_juros
    assert round(investiomento_valor_alvo_1000000.total_juros, 2) == expected_total_juros

    # Verifique se os alvos foram atingidos corretamente
    assert investiomento_valor_alvo_1000000.alvo_atingido['total']['atingido'] is True
    assert investiomento_valor_alvo_1000000.alvo_atingido['total']['info'] == ('Valor total alvo atingido em 26 anos e '
                                                                               '3 meses')
    # testa se o período investido bate com o informado no alvo
    assert investiomento_valor_alvo_1000000.historico[-1]['mes'] == 315
    assert calcular_anos_meses(investiomento_valor_alvo_1000000.historico[-1]['mes']) == '26 anos e 3 meses'


def test_imprimir_configuracao(capsys, investiomento_valor_alvo_1000000):
    investiomento_valor_alvo_1000000.imprimir_configuracoes()
    captured = capsys.readouterr()
    expected_output = ('Configurações:\n'
                       '+----------------------+-------------+\n'
                       '|    Valor Inicial     |   R$ 0,00   |\n'
                       '|    Aporte Mensal     | R$ 1.000,00 |\n'
                       '| Taxa de Juros Anual  |     8%      |\n'
                       '| Taxa de Juros Mensal |    0.64%    |\n'
                       '+----------------------+-------------+\n'
                       '\n')

    assert captured.out == expected_output


def test_imprimir_resultado(capsys, investiomento_valor_alvo_1000000):
    investiomento_valor_alvo_1000000.imprimir_resultados_finais(investiomento_valor_alvo_1000000.periodo_alvo_meses)
    captured = capsys.readouterr()
    expected_output = ('\n'
                       'Resultados Finais:\n'
                       '+---------------------+---------------------+\n'
                       '|  Capital Investido  |    R$ 314.000,00    |\n'
                       '|   Juros Recebidos   |    R$ 687.986,51    |\n'
                       '| - - - - - - - - - - | - - - - - - - - - - |\n'
                       '|   Total Acumulado   |   R$ 1.001.986,51   |\n'
                       '|    Renda Mensal     |     R$ 6.365,57     |\n'
                       '+---------------------+---------------------+\n')

    assert captured.out == expected_output


def test_imprimir_alvo_atingido(capsys, investiomento_valor_alvo_1000000):
    investiomento_valor_alvo_1000000.imprimir_alvos()
    captured = capsys.readouterr()
    expected_output = ('Alvos:\n'
                       '+------------------+------------------+\n'
                       '|   Período Alvo   | 0 anos (0 meses) |\n'
                       '|   Salário Alvo   |     R$ 0,00      |\n'
                       '| Valor Total Alvo | R$ 1.000.000,00  |\n'
                       '+------------------+------------------+\n'
                       'Valor total alvo atingido em 26 anos e 3 meses\n')

    assert captured.out == expected_output


def test_imprimir_imprimir_progressao_milhoes(capsys, investiomento_valor_alvo_1000000):
    investiomento_valor_alvo_1000000.imprimir_progressao_milhoes()
    captured = capsys.readouterr()
    expected_output = ('\n'
                       'Progressão de Milhões Atingidos:\n'
                       '┏ R$ 0,00\n'
                       '┗ 1.0M atingido em 26 anos e 3 meses.\n'
                       '\n')

    assert captured.out == expected_output
