import sys
import os

# Додаємо шлях до config.py (на один рівень вище кореня проєкту)
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, root)
