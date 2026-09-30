import pyautogui
import time

pyautogui.FAILSAFE = True


# ============================================================
# 1. OPEN START MENU
# ============================================================

print("Opening Start Menu...")

pyautogui.press("win")

time.sleep(1)


# ============================================================
# 2. SEARCH VS CODE
# ============================================================

print("Searching VS Code...")

pyautogui.write(
    "Visual Studio Code",
    interval=0.03
)

time.sleep(1)

pyautogui.press("enter")


# ============================================================
# 3. WAIT FOR VS CODE
# ============================================================

print("Waiting for VS Code...")

time.sleep(5)


# ============================================================
# 4. OPEN TERMINAL
# ============================================================

print("Opening Terminal...")

pyautogui.hotkey("ctrl", "`")

time.sleep(2)


# ============================================================
# 5. OPEN PORT FORWARDING
# ============================================================

print("Opening Port Forwarding...")

pyautogui.hotkey("ctrl", "shift", "3")

time.sleep(1)


# ============================================================
# 6. ENTER PORT 3000
# ============================================================

print("Entering port 3000...")

pyautogui.write(
    "3000",
    interval=0.1
)

time.sleep(0.5)

pyautogui.press("enter")

# Wait for port to be created
time.sleep(3)

print("Port 3000 forwarded.")


# ============================================================
# 7. OPEN CONTEXT MENU FOR PORT 3000
# ============================================================

print("Opening port context menu...")

# Shift + F10 = keyboard right-click
pyautogui.hotkey("shift", "f10")

time.sleep(1)


# ============================================================
# 8. PORT VISIBILITY
# ============================================================

print("Opening Port Visibility...")

# Context menu:
#
# 1. Open in Browser
# 2. Preview in Editor
# 3. Set Port Label
# 4. Copy Local Address
# 5. Port Visibility
#
# First item is selected.
# Move down 4 times to Port Visibility.

for i in range(4):
    pyautogui.press("down")
    time.sleep(0.2)


# Open Port Visibility submenu
pyautogui.press("right")

time.sleep(1)


# ============================================================
# 9. SELECT PUBLIC
# ============================================================

print("Selecting Public...")

# Submenu:
#
# Private
# Public
#
# Private is selected initially.
# Move down once to Public.

pyautogui.press("down")

time.sleep(0.3)

pyautogui.press("enter")

time.sleep(2)


# ============================================================
# 10. CONFIRM PUBLIC PORT
# ============================================================

print("Waiting for confirmation...")

time.sleep(1)

# VS Code warning dialog:
#
# You're about to create a publicly forwarded port...
#
# Continue button is the default action.
# Enter = Continue

pyautogui.press("enter")

time.sleep(3)


# ============================================================
# DONE
# ============================================================

print()
print("======================================")
print("           AUTOMATION DONE")
print("======================================")
print()
print("Port       : 3000")
print("Visibility : PUBLIC")
print()
print("======================================")