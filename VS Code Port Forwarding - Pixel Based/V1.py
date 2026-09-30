import pyautogui
import time

# Mouse ko screen ke corner me le jaane par script stop ho jayegi
pyautogui.FAILSAFE = True

# ----------------------------------------
# Helper function
# ----------------------------------------

def click(x, y, delay=1):
    pyautogui.click(x, y)
    time.sleep(delay)


# ----------------------------------------
# 1. Start Menu open karo
# ----------------------------------------

print("Opening Start Menu...")

pyautogui.press("win")
time.sleep(1)

# VS Code search karo
pyautogui.write("Visual Studio Code", interval=0.03)
time.sleep(1)

# Enter -> VS Code open
pyautogui.press("enter")

print("VS Code opening...")

# ----------------------------------------
# 2. VS Code ko 5 seconds wait karo
# ----------------------------------------

time.sleep(5)

print("VS Code opened.")


# ----------------------------------------
# 3. Ports tab par click
# ----------------------------------------

# Aapke screenshot ke according
# Ports tab approximately y = 612
# x = 1005

print("Opening Ports tab...")

click(1005, 612, 2)


# ----------------------------------------
# 4. Forward a Port button
# ----------------------------------------

print("Clicking Forward a Port...")

# Screenshot ke according
# Forward a Port button approximately:
# x = 750
# y = 720

click(750, 720, 1)


# ----------------------------------------
# 5. Port 3000 enter karo
# ----------------------------------------

print("Entering port 3000...")

pyautogui.write("3000")
pyautogui.press("enter")

time.sleep(2)


# ----------------------------------------
# 6. Port ko Public karo
# ----------------------------------------

print("Opening Port Visibility menu...")

# 3000 wali row ke upar right-click
# Screenshot ke according approximately:
# x = 150
# y = 135

pyautogui.rightClick(150, 135)

time.sleep(1)


# Port Visibility menu item
# Screenshot ke according approximately:
# x = 760
# y = 340

click(760, 340, 1)


# ----------------------------------------
# 7. Public select karo
# ----------------------------------------

print("Selecting Public...")

# Screenshot ke according Public option
# approximately:
# x = 1100
# y = 377

click(1100, 377, 1)


# ----------------------------------------
# 8. Security warning -> Continue
# ----------------------------------------

print("Waiting for confirmation dialog...")

time.sleep(1)

# Continue button
# Screenshot ke according:
# x = 460
# y = 225

click(460, 225, 2)


print()
print("====================================")
print("Port 3000 should now be PUBLIC.")
print("====================================")