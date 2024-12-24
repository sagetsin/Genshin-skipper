import pyautogui
import time

def print_pos():
    for i in range(20):
        print(pyautogui.position())
        time.sleep(0.5)

def move_mouse(x, y):
    pyautogui.moveTo(x,y)

def click_auto():
    pyautogui.click(x=33, y=32, buttom="left")

def forward_dialog():
    for i in range(10):
        pyautogui.click(x=942, y=664, button="left", clicks=1, interval=0.25)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_pos()
    #move_mouse(33,32)
    click_auto()
    forward_dialog()
