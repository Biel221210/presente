import subprocess
import sys
import datetime
import time
import os

# Cor roxa 💜
PURPLE = "\033[0;35m"
RESET = "\033[0m"

# Limpar terminal (Windows / Linux)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()


print(PURPLE + """
Depois de pensar um pouco, decidi te dar esse arquivo especial 💜
Ele tem um menu com algumas coisinhas que eu implementei só pra você.
Espero muito que você goste!
""" + RESET)

time.sleep(2)

limpar_tela()
if os.path.exists("art_ascii"):
    with open("art_ascii", "r", encoding="utf-8") as f:
        print(PURPLE + f.read() + RESET)

while True:
    opcao = input(PURPLE + """
========================
Menu 💜
[1] Ver quanto tempo faz que eu te conheço
[2] Executar o código
[3] Iniciar site
[4] Mostrar o quanto eu te considero
[0] Sair
========================
Escolha uma opção: """ + RESET)

    if opcao == '1':
        data_conhecimento = datetime.datetime(2020, 1, 26)
        data_atual = datetime.datetime.now()
        tempo_juntos = data_atual - data_conhecimento
        print(PURPLE + f"\nTe conheço há {tempo_juntos.days} dias\n" + RESET)
        time.sleep(2)

    elif opcao == '2':
        print(PURPLE + "\nExecutando seu código especial...\n" + RESET)
        subprocess.run(['python3', 'we_LOVE_samy_LOVE_SO_MUCH.py'])

    elif opcao == '3':
        print(PURPLE + "\nIniciando seu site de presente...\n" + RESET)
        subprocess.run(['python3', 'site.py'])

    elif opcao == '4':
        print(PURPLE + "\nPreparando a declaração...\n" + RESET)
        time.sleep(2)
        print('É nois (vc realmente achou que fosse algo a mais?)')
        input(PURPLE + "\nPressione Enter para voltar ao menu..." + RESET)

    elif opcao == '0':
        print(PURPLE + "\nRala veinho" + RESET)
        time.sleep(1)
        sys.exit()

    else:
        print(PURPLE + "\nOpção inválida 😅 tenta de novo!\n" + RESET)
        time.sleep(1)


