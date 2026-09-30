import pyautogui
import time

pyautogui.FAILSAFE = True


def click(x, y, delay=1):
    pyautogui.click(x, y)
    time.sleep(delay)


# ========================================
# 1. Start Menu open karo
# ========================================

print("Opening Start Menu...")

pyautogui.press("win")
time.sleep(1)

pyautogui.write("Visual Studio Code", interval=0.03)
time.sleep(1)

pyautogui.press("enter")

print("VS Code opening...")


# ========================================
# 2. VS Code ko 5 seconds wait karo
# ========================================

time.sleep(5)

print("VS Code opened.")


# ========================================
# 3. Terminal open karo
# ========================================

print("Opening VS Code Terminal...")

pyautogui.hotkey("ctrl", "`")

time.sleep(2)


# ========================================
# 4. Ports tab par click
# ========================================

print("Opening Ports tab...")

click(675, 735, 2)


# ========================================
# 5. Forward a Port
# ========================================

print("Clicking Forward a Port...")

click(750, 720, 1)


# ========================================
# 6. Port 3000
# ========================================

print("Entering port 3000...")

pyautogui.write("3000")
pyautogui.press("enter")

time.sleep(2)


# ========================================
# 7. Port Visibility -> Public
# ========================================

print("Opening Port Visibility...")

pyautogui.rightClick(150, 135)

time.sleep(1)

click(760, 340, 1)


# ========================================
# 8. Select Public
# ========================================

print("Selecting Public...")

click(1100, 377, 1)


# ========================================
# 9. Continue
# ========================================

print("Waiting for confirmation...")

time.sleep(1)

click(460, 225, 2)


print()
print("======================================")
print("Port 3000 is now PUBLIC.")
print("======================================")