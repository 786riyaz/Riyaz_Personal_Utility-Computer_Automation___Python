import time
import pyautogui


# ============================================================
# CONFIG
# ============================================================

PORT = "3000"

# VS Code start hone ke baad wait
VS_CODE_WAIT = 5


# ============================================================
# SAFETY
# ============================================================

# Mouse ko screen ke top-left corner me le jaoge
# to PyAutoGUI automation stop kar dega.
pyautogui.FAILSAFE = True


# ============================================================
# HELPER
# ============================================================

def command_palette(command, wait=1):
    """
    VS Code Command Palette open karke command run karta hai.
    """

    print(f"   Command: {command}")

    pyautogui.hotkey("ctrl", "shift", "p")
    time.sleep(0.7)

    # Existing search text clear
    pyautogui.hotkey("ctrl", "a")

    pyautogui.write(command, interval=0.02)

    time.sleep(0.8)

    pyautogui.press("enter")

    time.sleep(wait)


# ============================================================
# 1. START MENU
# ============================================================

print()
print("==============================================")
print("       VS CODE PORT AUTOMATION")
print("==============================================")
print()

print("[1] Opening Start Menu...")

pyautogui.press("win")

time.sleep(1)


# ============================================================
# 2. SEARCH VS CODE
# ============================================================

print("[2] Searching Visual Studio Code...")

pyautogui.write(
    "Visual Studio Code",
    interval=0.03
)

time.sleep(1)

pyautogui.press("enter")


# ============================================================
# 3. WAIT FOR VS CODE
# ============================================================

print(f"[3] Waiting {VS_CODE_WAIT} seconds for VS Code...")

time.sleep(VS_CODE_WAIT)


# ============================================================
# 4. OPEN TERMINAL
# ============================================================

print("[4] Opening VS Code Terminal...")

pyautogui.hotkey("ctrl", "`")

time.sleep(2)

print("[OK] Terminal opened.")


# ============================================================
# 5. OPEN PORTS VIEW
# ============================================================

print("[5] Opening Ports View...")

command_palette(
    # "Forward a Port",
    "Ports: Focus on Ports View",
    wait=2
)

print("[OK] Ports View command executed.")


# ============================================================
# 6. FORWARD PORT
# ============================================================

print("[6] Opening Forward a Port...")

command_palette(
    "Forward a Port",
    wait=1.5
)


# ============================================================
# 7. ENTER PORT 3000
# ============================================================

print(f"[7] Entering port {PORT}...")

pyautogui.write(PORT, interval=0.1)

time.sleep(0.5)

pyautogui.press("enter")

time.sleep(3)

print(f"[OK] Port {PORT} forwarded.")


# ============================================================
# 8. MAKE PORT PUBLIC
# ============================================================

print("[8] Opening Port Visibility menu...")

# IMPORTANT:
#
# After Forward a Port finishes, VS Code normally puts
# focus back on the newly forwarded port.
#
# Shift + F10 = context menu
#
pyautogui.hotkey("shift", "f10")

time.sleep(1)


# ============================================================
# 9. NAVIGATE TO "PORT VISIBILITY"
# ============================================================

print("[9] Selecting Port Visibility...")

# Context menu order in VS Code is approximately:
#
# Open in Browser
# Preview in Editor
# Set Port Label
# Copy Local Address
# Port Visibility
# Change Port Protocol
# Stop Forwarding Port
# Forward a Port
#
# Port Visibility is therefore 4 DOWN from the first item.

for _ in range(4):
    pyautogui.press("down")
    time.sleep(0.15)

pyautogui.press("right")

time.sleep(0.7)


# ============================================================
# 10. SELECT PUBLIC
# ============================================================

print("[10] Selecting Public...")

# Submenu:
#
# Private
# Public
#
# Move down once.
pyautogui.press("down")

time.sleep(0.3)

pyautogui.press("enter")

time.sleep(2)


# ============================================================
# 11. CONTINUE SECURITY WARNING
# ============================================================

print("[11] Waiting for security confirmation...")

time.sleep(1)

# Continue is the default action in the warning dialog.
# Enter activates it without using coordinates.

pyautogui.press("enter")

time.sleep(3)

# ============================================================
# DONE
# ============================================================

print()
print("==============================================")
print("              AUTOMATION DONE")
print("==============================================")
print()
print(f"Port       : {PORT}")
print("Visibility : PUBLIC")
print()
print("No pixel coordinates were used.")
print("==============================================")