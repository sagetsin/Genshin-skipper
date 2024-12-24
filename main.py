import pyautogui
import pyscreeze
import time

def print_pos():
    for i in range(20):
        print(pyautogui.position())
        time.sleep(0.5)

def move_mouse(x, y):
    pyautogui.moveTo(x,y)

def click_auto():
    pyautogui.click(x=33, y=32, button="left")

def forward_dialog():
    pyautogui.click(x=942, y=664, button="left", clicks=1, interval=0.25)
    print("click")

def choose_dialog():
    #im = pyautogui.screenshot("partial-screen.png", region=(905, 569, 1794, 943))
    try:
        x,y = pyautogui.locateCenterOnScreen("F.png")
        pyautogui.press('f')
    except:
        print("No dialog found")


def pause_game():
    pyautogui.press('esc')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time.sleep(5)
    #print_pos()
    click_auto()
    for i in range(10):
        forward_dialog()
        choose_dialog()
