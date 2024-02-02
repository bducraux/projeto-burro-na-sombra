import locale

# Set the locale to the user's default setting to format the number correctly
locale.setlocale(locale.LC_ALL, '')


def taxa_anual_para_mensal(taxa_anual: int, round_digits: int = 2) -> float:
    taxa_mensal = (1 + taxa_anual / 100) ** (1 / 12) - 1

    return round(taxa_mensal * 100, round_digits)


def taxa_mensal_para_anual(taxa_mensal: float, round_digits: int = 2) -> float:
    taxa_anual = (1 + taxa_mensal / 100) ** 12 - 1
    return round(taxa_anual * 100, round_digits)


def calcular_anos_meses(total_meses: int) -> str:
    anos, meses_sobra = divmod(total_meses, 12)

    anos_str = f'{anos} ano{"s" if anos != 1 else ""}' if anos > 0 else ''
    meses_str = f'{meses_sobra} m{"eses" if meses_sobra != 1 else "ês"}' if meses_sobra > 0 else ''

    if anos_str and meses_str:
        return f'{anos_str} e {meses_str}'
    else:
        return anos_str + meses_str


def formatar_valor(valor: float) -> str:
    return f'R$ {locale.format_string("%1.2f", valor, grouping=True)}'
