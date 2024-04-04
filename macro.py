import time
import pyautogui
import keyboard

# Tamanho da Tela
screen_width = 0
screen_height = 0

# Variáveis Gerais
refresh = 0
skystone = 0
gold = 0
bookmark = 0
mystic = 0
wait_time = 0.8
confidence_rate = .95
stop = False

# Cores
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[0;33m"
BOLD = "\033[;1m"
WARNING = '\033[93m'
RESET = "\033[0;0m"


def InicializaVariaveis():
    global refresh, skystone, gold, bookmark, mystic, stop, screen_width, screen_height

    refresh = skystone = gold = bookmark = mystic = 0
    stop = False

    screen_width, screen_height = pyautogui.size()


def Resultado():
    global refresh, bookmark, mystic, skystone, gold
    skystone = refresh * 3
    gold = (bookmark * 184000) + (mystic * 280000)
    print(f'⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺⸺\n'
          f'As {refresh} atualizações na loja terminaram e foram gastas {skystone} Skystones.\n'
          f'⸺⸺⸺{BOLD}Total{RESET}⸺⸺⸺\n'
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
        location = pyautogui.locateOnScreen('img/refresh.png', confidence=confidence_rate)
        center = pyautogui.center(location)

        # Clicar no Botão de Refresh
        pyautogui.click(center.x, center.y)
        time.sleep(wait_time)

        # Clicar no Botão de Confirmar Refresh
        pyautogui.click(screen_width * 0.578, screen_height * 0.611)
        time.sleep(2 * wait_time)
        refresh += 1

    except:
        return


def ArrastarLoja():
    pyautogui.moveTo(screen_width * 0.677, screen_height * 0.74)
    pyautogui.dragTo(screen_width * 0.677, screen_height * 0.185, duration=.5)
    time.sleep(wait_time)


def VerificaBookmark1():
    global bookmark
    try:
        location = pyautogui.locateOnScreen('img/covenant.png', confidence=confidence_rate)

        # Clicar no botão de Comprar
        pyautogui.click(screen_width * 0.901, location.top + location.height)
        time.sleep(wait_time)

        # Confirmar a Compra
        pyautogui.click(screen_width * 0.557, screen_height * 0.703)
        time.sleep(wait_time)
        bookmark += 1
        print(f'Yeaaaah! Encontrei 1 {BOLD}{CYAN}Bookmark{RESET} perdido!')

    except:
        return


def VerificaBookmark2():
    global bookmark
    try:
        location = pyautogui.locateOnScreen('img/covenant.png', confidence=confidence_rate, region=(810, 670, 170, 370))

        # Clicar no botão de Comprar
        pyautogui.click(screen_width * 0.901, location.top + location.height)
        time.sleep(wait_time)

        # Confirmar a Compra
        pyautogui.click(screen_width * 0.557, screen_height * 0.703)
        time.sleep(wait_time)
        bookmark += 1
        print(f'Yeaaaah! Encontrei 1 {BOLD}{CYAN}Bookmark{RESET} perdido!')

    except:
        return


def VerificaMystic1():
    global mystic
    try:
        location = pyautogui.locateOnScreen('img/mystic.png', confidence=confidence_rate)

        # Clicar no botão de Comprar
        pyautogui.click(screen_width * 0.901, location.top + location.height)
        time.sleep(wait_time)

        # Confirmar a Compra
        pyautogui.click(screen_width * 0.557, screen_height * 0.703)
        time.sleep(wait_time)
        mystic += 1
        print(f'Woohoo! 1 {BOLD}{RED}Mystic{RESET} apareceu no meu caminho!')

    except:
        return


def VerificaMystic2():
    global mystic
    try:
        location = pyautogui.locateOnScreen('img/mystic.png', confidence=confidence_rate, region=(810, 670, 170, 370))

        # Clicar no botão de Comprar
        pyautogui.click(screen_width * 0.901, location.top + location.height)
        time.sleep(wait_time)

        # Confirmar a Compra
        pyautogui.click(screen_width * 0.557, screen_height * 0.703)
        time.sleep(wait_time)
        mystic += 1
        print(f'Woohoo! 1 {BOLD}{RED}Mystic{RESET} apareceu no meu caminho!')

    except:
        return


def Stop():
    global stop
    stop = True


def main():
    InicializaVariaveis()

    # print(screen_width, screen_height)

    number_skystone_spend = int(input("Informe quantas Skys deseja roletar: "))
    number_skystone_spend = number_skystone_spend // 3

    print(f'\n{BOLD}{WARNING}*{RESET} As {number_skystone_spend} atualizações na loja começarão em 5 Segundos.\n'
          f'{BOLD}{WARNING}*{RESET} Pressione F1 caso queira encerrar o programa.\n')
    time.sleep(5)

    keyboard.add_hotkey('F1', Stop)

    for i in range(number_skystone_spend):
        if stop:
            break

        AtualizaLoja()
        VerificaBookmark1()
        VerificaMystic1()
        ArrastarLoja()
        VerificaBookmark2()
        VerificaMystic2()

    Resultado()


if __name__ == '__main__':
    main()
