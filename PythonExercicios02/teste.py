import os
import time

def linha_completa(msg, cor_fundo='\033[44m'):
    """
    Imprime uma linha com cor de fundo que ocupa a largura total do terminal.
    :param msg: A mensagem a ser exibida.
    :param cor_fundo: Código de escape ANSI para a cor de fundo.
    """
    # 1. Obtém a largura do terminal
    largura = os.get_terminal_size().columns
    reset = '\033[0m'

    # 2. Cria uma linha com cor de fundo
    #    e centraliza a mensagem dentro dela.
    linha = f'{cor_fundo}{msg:^{largura}}{reset}'

    # 3. Imprime a linha
    print(linha)


# --- Exemplo de uso ---
linha_completa('Este é um título!')
time.sleep(1) # pausa para ver o efeito
linha_completa('Vamos falar sobre Python.', '\033[42m') # Fundo verde