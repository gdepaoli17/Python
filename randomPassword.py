import random

import pyperclip
from win10toast import ToastNotifier


def copytext(password):
    pyperclip.copy(password)

letters = "abcdefghijklmnopqrstuvwxyz"
# upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
symbols = "!@#$%&*/\\?<>+-"
password_length = 10
password_combo = letters + letters.upper() + symbols + numbers

generate_password = "".join(random.sample(password_combo, password_length))

copytext(generate_password)
sys_tray_notifier = ToastNotifier()
sys_tray_notifier.show_toast(generate_password)
