from rich.console import Console
from time import sleep

import pyautogui
import keyboard


console = Console()
console.show_cursor(False)


def test(e):
    console.print(pyautogui.position())


keyboard.on_press_key("p", test)


while True:
    input()
