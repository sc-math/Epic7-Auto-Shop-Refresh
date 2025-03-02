import time
import pyautogui
import keyboard

# Tamanho da Tela
screen_width, screen_height = pyautogui.size()

# Variáveis Gerais
refresh = 0
skystone = 0
gold = 0
bookmark = 0
mystic = 0
wait_time = 0.65
confidence_rate = .95
stop = False
opcao = 0
number_bm_want = 0

# Cores
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[0;33m"
BOLD = "\033[;1m"
WARNING = '\033[93m'
RESET = "\033[0;0m"


def Resultado():
    global refresh, bookmark, mystic, skystone, gold
    skystone = refresh * 3
    gold = (bookmark * 184000) + (mystic * 280000)
    print(f'========================================================\n'
          f'As {refresh} atualizações na loja terminaram e foram gastas {skystone} Skystones.\n'
          f'==={BOLD}Total{RESET}===\n'
          f'{BOLD}{CYAN}Bookmark{RESET}: {bookmark}\n'
          f'{BOLD}{RED}Mystic{RESET}: {mystic}')

    if gold > 1000000:
        print(f'{BOLD}{YELLOW}Ouro Gasto{RESET}: {gold / 1000000}M')
    else:
        print(f'{BOLD}{YELLOW}Ouro Gasto{RESET}: {gold / 1000}K')


def AtualizaLoja():
    global refresh, skystone

    try:
        # Procurar na tela o Botão de Refresh
        location = pyautogui.locateOnScreen('refresh.png', confidence=confidence_rate)
        center = pyautogui.center(location)

        # Clicar no Botão de Refresh
        pyautogui.click(x=center.x, y=center.y, clicks=2, interval=0.2)
        time.sleep(wait_time)

        # Clicar no Botão de Confirmar Refresh
        pyautogui.click(screen_width * 0.578, screen_height * 0.611, clicks=2, interval=0.2)

        time.sleep(2 * wait_time)
        refresh += 1

    except:
        #print("erro no atualizar Loja")
        return


def ArrastarLoja():
    pyautogui.moveTo(screen_width * 0.677, screen_height * 0.74)
    pyautogui.dragTo(screen_width * 0.677, screen_height * 0.185, duration=.3)
    time.sleep(wait_time)


def comprar(location, bmType):
    global bookmark, mystic

    # Clicar no botão de Comprar
    pyautogui.click(x=screen_width * 0.901, y=location.top + location.height, clicks=2, interval=0.1)
    pyautogui.click(screen_width * 0.901, location.top + location.height)

    time.sleep(wait_time)

    # Confirmar a Compra
    pyautogui.click(screen_width * 0.557, screen_height * 0.703)
    pyautogui.click(screen_width * 0.557, screen_height * 0.703)

    if bmType == 1:
        bookmark += 1
        print(f'Yeaaaah! Encontrei 1 {BOLD}{CYAN}Bookmark{RESET} perdido!', end="")
        print("" if opcao == 1 else f' (Faltam {number_bm_want - bookmark})')
    elif bmType == 2:
        mystic += 1
        print(f'Woohoo! 1 {BOLD}{RED}Mystic{RESET} apareceu no meu caminho!')

    time.sleep(wait_time + .5)


def VerificaBookmark(turn):
    global bookmark
    try:
        if turn == 0:
            location = pyautogui.locateOnScreen('bm.png', confidence=confidence_rate)
        else:
            location = pyautogui.locateOnScreen('bm.png', confidence=confidence_rate, region=(810, 670, 170, 370))

        comprar(location, 1)

    except:
        #print("erro no Verifica Bookmark")
        return


def VerificaMystic(turn):
    global mystic
    try:
        if turn == 0:
            location = pyautogui.locateOnScreen('mystic.png', confidence=confidence_rate)
        else:
            location = pyautogui.locateOnScreen('mystic.png', confidence=confidence_rate, region=(810, 670, 170, 370))
        comprar(location, 2)

    except:
        #print("erro no Verifica Mystic")
        return


def Stop():
    global stop
    stop = True


def main():
    global opcao, number_bm_want
    opcao = int(input("1 - Valor de Sky\n2 - Quantidade de BMs\nInforma qual modo você quer:"))

    if opcao == 1:
        number_skystone_spend = int(input("Informe quantas Skys deseja roletar: "))
        number_skystone_spend = number_skystone_spend // 3

        print(
            f'\n{BOLD}{WARNING}*{RESET} As {number_skystone_spend} atualizações na loja começarão em 5 Segundos.\n'
            f'{BOLD}{WARNING}*{RESET} Pressione F1 caso queira encerrar o programa.\n')
        time.sleep(2)

        keyboard.add_hotkey('F1', Stop)

        for i in range(number_skystone_spend):
            if stop:
                break

            AtualizaLoja()
            VerificaBookmark(0)
            VerificaMystic(0)
            ArrastarLoja()
            VerificaBookmark(1)
            VerificaMystic(1)

    elif opcao == 2:
        number_bm_want = int(input("Informe quantos deseja comprar: "))

        print(
            f'\n{BOLD}{WARNING}*{RESET} A compra dos {number_bm_want} BMs na loja começarão em 5 Segundos.\n'
            f'{BOLD}{WARNING}*{RESET} Pressione F1 caso queira encerrar o programa.\n')
        time.sleep(2)

        keyboard.add_hotkey('F1', Stop)

        while bookmark < number_bm_want:
            if stop:
                break

            AtualizaLoja()
            VerificaBookmark(0)
            VerificaMystic(0)
            ArrastarLoja()
            VerificaBookmark(1)
            VerificaMystic(1)

    Resultado()


if __name__ == '__main__':
    main()
