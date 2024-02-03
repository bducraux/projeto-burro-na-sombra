from utils import taxa_anual_para_mensal, calcular_anos_meses, formatar_valor


class CalculadoraIndependenciaFinanceira:
    def __init__(self):
        # Valores padrão
        self.valor_aporte_inicial = 0
        self.valor_aporte_mensal = 1000
        self.taxa_juros_anual = 6
        self.taxa_juros_mensal = 0.49
        self.periodo_alvo_anos = 1
        self.periodo_alvo_meses = 12
        self.salario_alvo = 0
        self.valor_total_alvo = 0

        # Variáveis adicionais
        self.juros = 0
        self.total_juros = 0
        self.total_investido = 0
        self.total_acumulado = 0
        self.historico = []
        self.ultimo_milhao_atingido = 0
        self.milhoes_atingidos_historico = []

        # Informações sobre os alvos atingidos
        self.alvo_atingido = {}

        # Informação sobre se configurações iniciais e os limites foram definidos
        self.alvo_definido = False
        self.configuracao_inicial_definida = False

    def configurar_investimento(self, _valor_inicial, _valor_aporte_mensal, _taxa_juros_anual):
        self.valor_aporte_inicial = _valor_inicial
        self.valor_aporte_mensal = _valor_aporte_mensal
        self.taxa_juros_anual = _taxa_juros_anual
        self.taxa_juros_mensal = taxa_anual_para_mensal(_taxa_juros_anual)

        self.configuracao_inicial_definida = True

    def configurar_alvos(self, _periodo_alvo_anos, _salario_alvo, _valor_total_alvo):
        self.periodo_alvo_anos = _periodo_alvo_anos
        self.periodo_alvo_meses = _periodo_alvo_anos * 12 if _periodo_alvo_anos else 0
        self.salario_alvo = _salario_alvo
        self.valor_total_alvo = _valor_total_alvo

        # Configurar alvos atingidos
        if self.periodo_alvo_anos:
            self.alvo_atingido['periodo'] = {'atingido': False, 'info': ''}
        if self.salario_alvo:
            self.alvo_atingido['salario'] = {'atingido': False, 'info': 'Alvo de salário não atingido!'}
        if self.valor_total_alvo:
            self.alvo_atingido['total'] = {'atingido': False, 'info': 'Alvo de valor total não atingido!'}

        # Verificar limites após configurar os alvos
        self.alvo_definido = any([self.periodo_alvo_anos, self.salario_alvo, self.valor_total_alvo])

    def calcular_investimento(self):
        """
        Calcula o crescimento do investimento ao longo do tempo e verifica se os alvos foram atingidos.

        Para cada mês, o método calcula o valor do investimento, juros recebidos e verifica se os alvos foram atingidos,
        os resultados são armazenados em um histórico que será utilizado para gerar um relatório final.

        :return: None
        """

        # Período de investimento em meses (padrão: 50 anos caso o período alvo não seja definido)
        periodo_investimento = 12 * 50 if not self.periodo_alvo_meses else self.periodo_alvo_meses
        for mes in range(1, periodo_investimento + 1):
            self.historico.append({"mes": mes,
                                   "total_investido": round(self.total_investido, 2),
                                   "total_acumulado": round(self.total_acumulado, 2),
                                   "juros": round(self.juros, 2),
                                   "total_juros": round(self.total_juros, 2)
                                   })

            milhoes_atingidos = self.total_acumulado // 1000000
            tempo_para_atingir = calcular_anos_meses(mes)

            # Adiciona ao histórico de milhões atingidos
            if milhoes_atingidos > self.ultimo_milhao_atingido:
                milhoes_atingidos_info = {"milhao": milhoes_atingidos,
                                          "tempo": tempo_para_atingir,
                                          "mes": mes}
                self.ultimo_milhao_atingido = milhoes_atingidos
                self.milhoes_atingidos_historico.append(milhoes_atingidos_info)

            if 0 < self.salario_alvo <= self.juros:
                self.alvo_atingido['salario']['atingido'] = True
                self.alvo_atingido['salario']['info'] = f'Salário alvo atingido em {calcular_anos_meses(mes)}'
                break

            if 0 < self.valor_total_alvo <= self.total_acumulado:
                self.alvo_atingido['total']['atingido'] = True
                self.alvo_atingido['total']['info'] = f'Valor total alvo atingido em {calcular_anos_meses(mes)}'
                break

            if self.periodo_alvo_anos and mes == self.periodo_alvo_meses:
                self.alvo_atingido['periodo']['atingido'] = True
                self.alvo_atingido['periodo']['info'] = 'Período alvo atingido!'
                break

            # Calcula o valor do investimento e juros recebidos para o próximo mês
            self.juros = self.total_acumulado * self.taxa_juros_mensal / 100
            self.total_juros += self.juros
            self.total_investido += self.valor_aporte_mensal
            self.total_acumulado += self.valor_aporte_mensal + self.juros

    def imprimir_configuracoes(self):
        print('Configurações:')
        if not self.configuracao_inicial_definida:
            print("AVISO: Nenhuma configuração inicial foi definida! Configuração padrão foi utilizada.")

        table_data = [
            ['Valor Inicial', formatar_valor(self.valor_aporte_inicial)],
            ['Aporte Mensal', formatar_valor(self.valor_aporte_mensal)],
            ['Taxa de Juros Anual', f'{self.taxa_juros_anual}%'],
            ['Taxa de Juros Mensal', f'{self.taxa_juros_mensal}%'],
        ]
        self.imprimir_tabela(table_data)
        print()

    def imprimir_alvos(self):
        print('Alvos:')
        if not self.alvo_definido:
            print("AVISO: Nenhum alvo foi definido! Período alvo padrão de 1 ano foi utilizado.")

        table_data = [
            ['Período Alvo', f'{self.periodo_alvo_anos} anos ({self.periodo_alvo_meses} meses)'],
            ['Salário Alvo', formatar_valor(self.salario_alvo)],
            ['Valor Total Alvo', formatar_valor(self.valor_total_alvo)],
        ]

        self.imprimir_tabela(table_data)

        for alvo, info in self.alvo_atingido.items():
            print(f'{info["info"]}')

    def imprimir_resultados_finais(self, mes_atual):
        print('\nResultados Finais:')
        table_data = [
            ['Capital Investido', formatar_valor(self.total_investido)],
            ['Juros Recebidos', formatar_valor(self.total_juros)],
            ['- ' * 10, '- ' * 10],
            ['Total Acumulado', formatar_valor(self.total_acumulado)],
            ['Renda Mensal', formatar_valor(self.juros)],
        ]
        self.imprimir_tabela(table_data)

    def imprimir_progressao_milhoes(self):
        print('\nProgressão de Milhões Atingidos:')
        print(f"┏ {formatar_valor(self.valor_aporte_inicial)}")

        # checa se o histórico de milhões atingidos está vazio
        if not self.milhoes_atingidos_historico:
            print(f"┗ {formatar_valor(self.total_acumulado)}")
            print("Você ainda não atingiu 1M. Continue investindo!")
            return

        for i in range(1, len(self.milhoes_atingidos_historico)):
            milhao_anterior = self.milhoes_atingidos_historico[i - 1]
            milhao_atual = self.milhoes_atingidos_historico[i]
            meses_entre_milhoes = calcular_anos_meses(milhao_atual["mes"] - milhao_anterior["mes"])

            print(f"┣ {milhao_anterior['milhao']}M atingido em {milhao_anterior['tempo']}.")
            print(f"┠ {meses_entre_milhoes} meses")

        print(f"┗ {self.milhoes_atingidos_historico[-1]['milhao']}M atingido em "
              f"{self.milhoes_atingidos_historico[-1]['tempo']}.")

        print()

    @staticmethod
    def imprimir_tabela(table_data: list):
        try:
            from tabulate import tabulate
            print(tabulate(table_data, tablefmt="pretty"))
        except ImportError:
            for row in table_data:
                # check if row is a separator
                if row[0].startswith('-'):
                    print(''.join(['-' * len(cell) for cell in row]))
                    continue
                print(': '.join(map(str, row)))

    def plotar_grafico(self):
        try:
            import matplotlib.pyplot as plt

            if not self.historico:
                print('Nenhum dado para plotar o gráfico.')
                return

            # Extrair dados do histórico
            meses = [entry['mes'] for entry in self.historico]
            _total_acumulado = [entry['total_acumulado'] for entry in self.historico]
            _total_investido = [entry['total_investido'] for entry in self.historico]

            # Plotar o gráfico
            plt.figure(figsize=(12, 8))

            # Linhas principais
            plt.plot(meses, _total_acumulado, label='Total Acumulado', color='b', linewidth=2)
            plt.plot(meses, _total_investido, label='Total Investido', color='green', linestyle='--', linewidth=2)

            # Destacar pontos onde milhões foram atingidos
            num_milhoes_atingidos = [entry['total_acumulado'] // 1000000 for entry in self.historico]

            # Ajustar a escala do eixo y começando do VALOR_INICIAL
            valor_inicial_ajustado = self.valor_aporte_inicial - (self.valor_aporte_inicial % 50000)
            plt.yticks(
                range(valor_inicial_ajustado, int(max(max(_total_acumulado), max(_total_investido))) + 50000, 50000))

            # Ajustar o eixo x para mostrar meses em intervalos de 6 meses
            plt.xticks(range(0, max(meses) + 1, 6))

            # Adicionar rótulos e título
            plt.title('Crescimento dos Investimentos ao Longo do Tempo', fontsize=16)
            plt.xlabel('Meses', fontsize=12)
            plt.ylabel('Valores em Milhões', fontsize=12)

            # Adicionar grade e legenda
            plt.grid(True)
            plt.legend(loc='upper left')

            # Adicionar quadro informativo para tempo de atingir cada marco de milhão
            legendas_adicionadas = set()

            for mes_atual, milhao in zip(meses, num_milhoes_atingidos):
                if milhao > 0 and milhao not in legendas_adicionadas:
                    plt.scatter(mes_atual, milhao * 1000000, color='red', marker='o')

                    tempo_para_atingir = calcular_anos_meses(mes_atual)
                    plt.annotate(f'{milhao}M em {tempo_para_atingir}', xy=(mes_atual, milhao * 1000000),
                                 xytext=(mes_atual + 15, milhao * 1000000 + 500000), fontsize=8,
                                 arrowprops=dict(facecolor='black', arrowstyle='->'))

                    legendas_adicionadas.add(milhao)

            # Mostrar o gráfico
            plt.tight_layout()
            plt.show()
        except ImportError:
            print('Para plotar o gráfico, instale a biblioteca matplotlib.')

    def imprimir_relatorio_final(self):
        self.imprimir_configuracoes()
        self.imprimir_alvos()
        self.imprimir_progressao_milhoes()
        self.imprimir_resultados_finais(self.periodo_alvo_meses)

        self.plotar_grafico()


if __name__ == '__main__':
    # CONFIGURAÇÕES INICIAIS
    valor_inicial = 100000  # Valor inicial investido
    valor_aporte_mensal = 5000  # Valor a ser investido mensalmente
    taxa_juros_anual = 6  # Taxa de juros anual

    # CONFIGURAÇÕES DE ALVOS
    periodo_alvo_anos = 10  # Alvo de período de investimento em anos
    salario_alvo = 0  # Alvo de renda mensal
    valor_total_alvo = 0  # Alvo de valor total acumulado

    investimento = CalculadoraIndependenciaFinanceira()
    investimento.configurar_investimento(valor_inicial, valor_aporte_mensal, taxa_juros_anual)
    investimento.configurar_alvos(periodo_alvo_anos, salario_alvo, valor_total_alvo)

    investimento.calcular_investimento()
    investimento.imprimir_relatorio_final()
