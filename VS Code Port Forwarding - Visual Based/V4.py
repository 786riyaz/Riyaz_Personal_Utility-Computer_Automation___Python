import pyautogui
import time

pyautogui.FAILSAFE = True


# ======================================
# 1. OPEN VS CODE
# ======================================

print("Opening Start Menu...")
pyautogui.press("win")
time.sleep(1)

print("Searching VS Code...")
pyautogui.write(
    "Visual Studio Code",
    interval=0.03
)

time.sleep(1)
pyautogui.press("enter")

print("Waiting for VS Code...")
time.sleep(5)


# ======================================
# 2. OPEN TERMINAL
# ======================================

print("Opening Terminal...")
pyautogui.hotkey("ctrl", "`")
time.sleep(2)


# ======================================
# 3. FORWARD PORT
# ======================================

print("Opening Port Forwarding...")
pyautogui.hotkey("ctrl", "shift", "3")
time.sleep(1)

print("Entering port 3000...")
pyautogui.write(
    "3000",
    interval=0.1
)

time.sleep(0.5)
pyautogui.press("enter")

time.sleep(3)

print("Port 3000 forwarded.")


# ======================================
# 4. OPEN PORT CONTEXT MENU
# ======================================

print("Opening port context menu...")

pyautogui.hotkey("shift", "f10")

time.sleep(1)


# ======================================
# 5. MOVE TO PORT VISIBILITY
# ======================================

print("Selecting Port Visibility...")

# Force keyboard navigation to start
pyautogui.press("home")
time.sleep(0.3)

# Menu:
#
# 1. Open in Browser
# 2. Preview in Editor
# 3. Set Port Label
# 4. Copy Local Address
# 5. Port Visibility
#
# Move 4 times down
for _ in range(4):
    pyautogui.press("down")
    time.sleep(0.3)


# ======================================
# 6. OPEN PORT VISIBILITY SUBMENU
# ======================================

print("Opening Port Visibility submenu...")

pyautogui.press("right")
time.sleep(1)


# ======================================
# 7. SELECT PUBLIC
# ======================================

print("Selecting Public...")

# Submenu:
#
# Private
# Public
#
# Private is first, Public is second

pyautogui.press("down")
time.sleep(0.5)

pyautogui.press("enter")

time.sleep(2)


# ======================================
# 8. CONFIRM SECURITY WARNING
# ======================================

print("Waiting for public port confirmation...")

time.sleep(1)

# Continue is the default button
pyautogui.press("enter")

time.sleep(3)


# ======================================
# DONE
# ======================================

print()
print("======================================")
print("           AUTOMATION DONE")
print("======================================")
print()
print("Port       : 3000")
print("Visibility : PUBLIC")
print()
print("======================================")