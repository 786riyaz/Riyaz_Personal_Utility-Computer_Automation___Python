import time
import subprocess

from pywinauto import Desktop
from pywinauto.keyboard import send_keys


# ============================================================
# CONFIG
# ============================================================

PORT = "3000"
VS_CODE_WAIT = 5


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def find_element(parent, title=None, control_type=None, timeout=10):
    """
    UI Automation element ko title/control_type ke basis par find karta hai.
    Pixel coordinates ka use nahi karta.
    """

    end_time = time.time() + timeout

    while time.time() < end_time:

        try:
            kwargs = {}

            if title is not None:
                kwargs["title"] = title

            if control_type is not None:
                kwargs["control_type"] = control_type

            element = parent.child_window(**kwargs)

            if element.exists(timeout=0.5):
                return element

        except Exception:
            pass

        time.sleep(0.3)

    return None


def find_descendant(parent, title=None, control_type=None, timeout=10):
    """
    Deep UI hierarchy mein element search karta hai.
    """

    end_time = time.time() + timeout

    while time.time() < end_time:

        try:
            kwargs = {}

            if title is not None:
                kwargs["title"] = title

            if control_type is not None:
                kwargs["control_type"] = control_type

            element = parent.child_window(**kwargs)

            if element.exists(timeout=0.5):
                return element

        except Exception:
            pass

        time.sleep(0.3)

    return None


def get_vscode():
    """
    Running VS Code window ko UI Automation ke through find karta hai.
    """

    desktop = Desktop(backend="uia")

    end_time = time.time() + 15

    while time.time() < end_time:

        try:
            windows = desktop.windows()

            for window in windows:

                try:
                    title = window.window_text()

                    if "Visual Studio Code" in title:
                        return window

                except Exception:
                    continue

        except Exception:
            pass

        time.sleep(0.5)

    return None


# ============================================================
# 1. START MENU -> VS CODE
# ============================================================

print()
print("============================================")
print(" VS Code Port Automation")
print("============================================")
print()

print("[1] Opening Start Menu...")

send_keys("{VK_LWIN}")

time.sleep(1)

print("[2] Searching Visual Studio Code...")

# send_keys("Visual Studio Code")
send_keys("VS Code")

time.sleep(1)

send_keys("{ENTER}")

print("[3] VS Code starting...")

time.sleep(VS_CODE_WAIT)


# ============================================================
# 2. CONNECT TO VS CODE
# ============================================================

print("[4] Finding VS Code window...")

vscode = get_vscode()

if vscode is None:
    print()
    print("ERROR: VS Code window could not be found.")
    print("Make sure Visual Studio Code is installed and opened.")
    exit(1)

print("[OK] VS Code found.")


# ============================================================
# 3. OPEN TERMINAL
# ============================================================

print("[5] Opening VS Code Terminal...")

vscode.set_focus()

send_keys("^`")

time.sleep(2)

print("[OK] Terminal opened.")


# ============================================================
# 4. FIND PORTS TAB
# ============================================================

print("[6] Finding Ports tab...")

ports_tab = find_descendant(
    vscode,
    title="Ports",
    control_type="TabItem",
    timeout=10
)

if ports_tab is None:

    # Some VS Code versions expose it differently.
    # Try without specifying control type.
    ports_tab = find_descendant(
        vscode,
        title="Ports",
        timeout=5
    )


if ports_tab is None:
    print()
    print("ERROR: Ports tab could not be found.")
    print()
    print("Available UI elements:")
    print("--------------------------------------------")

    try:
        for element in vscode.descendants():
            try:
                name = element.window_text()
                control = element.element_info.control_type

                if name:
                    print(f"{control}: {name}")

            except Exception:
                pass
    except Exception:
        pass

    exit(1)


print("[OK] Ports tab found.")

ports_tab.click_input()

time.sleep(1)


# ============================================================
# 5. FORWARD A PORT
# ============================================================

print("[7] Finding 'Forward a Port' button...")

forward_button = find_descendant(
    vscode,
    title="Forward a Port",
    control_type="Button",
    timeout=5
)

if forward_button is None:

    forward_button = find_descendant(
        vscode,
        title="Forward a Port",
        timeout=5
    )


if forward_button is None:

    print()
    print("ERROR: 'Forward a Port' button was not found.")
    print()
    print("Available buttons:")
    print("--------------------------------------------")

    try:
        for element in vscode.descendants(control_type="Button"):
            try:
                name = element.window_text()

                if name:
                    print(name)

            except Exception:
                pass
    except Exception:
        pass

    exit(1)


print("[OK] Forward a Port button found.")

forward_button.click_input()

time.sleep(1)


# ============================================================
# 6. ENTER PORT 3000
# ============================================================

print(f"[8] Entering port {PORT}...")

# VS Code's port picker is keyboard-friendly.
# Focus should already be in the port input.

send_keys(PORT)

time.sleep(0.5)

send_keys("{ENTER}")

time.sleep(2)

print(f"[OK] Port {PORT} submitted.")


# ============================================================
# 7. FIND PORT ROW
# ============================================================

print("[9] Finding port 3000 row...")

port_row = None

end_time = time.time() + 10

while time.time() < end_time:

    try:

        # Search for any UI element containing 3000
        elements = vscode.descendants()

        for element in elements:

            try:
                text = element.window_text()

                if text and "3000" in text:
                    port_row = element
                    break

            except Exception:
                continue

        if port_row is not None:
            break

    except Exception:
        pass

    time.sleep(0.5)


if port_row is None:
    print()
    print("ERROR: Port 3000 row could not be found.")
    exit(1)


print("[OK] Port 3000 found.")


# ============================================================
# 8. OPEN PORT CONTEXT MENU
# ============================================================

print("[10] Opening port context menu...")

port_row.click_input(button="right")

time.sleep(1)


# ============================================================
# 9. FIND PORT VISIBILITY
# ============================================================

print("[11] Finding 'Port Visibility'...")

# Context menu normally belongs to Desktop,
# not directly to VS Code's normal child hierarchy.

desktop = Desktop(backend="uia")

visibility = None

end_time = time.time() + 5

while time.time() < end_time:

    try:

        visibility = desktop.window(
            title="Port Visibility",
            control_type="MenuItem"
        )

        if visibility.exists(timeout=0.5):
            break

    except Exception:
        pass

    time.sleep(0.3)


if visibility is None or not visibility.exists():

    # Try searching all visible MenuItems
    try:

        for element in desktop.descendants(control_type="MenuItem"):

            try:
                name = element.window_text()

                if name and "Port Visibility" in name:
                    visibility = element
                    break

            except Exception:
                pass

    except Exception:
        pass


if visibility is None:

    print()
    print("ERROR: Port Visibility menu was not found.")
    exit(1)


print("[OK] Port Visibility found.")

visibility.click_input()

time.sleep(0.8)


# ============================================================
# 10. SELECT PUBLIC
# ============================================================

print("[12] Selecting Public...")

public_item = None

end_time = time.time() + 5

while time.time() < end_time:

    try:

        public_item = desktop.window(
            title="Public",
            control_type="MenuItem"
        )

        if public_item.exists(timeout=0.5):
            break

    except Exception:
        pass

    time.sleep(0.3)


if public_item is None or not public_item.exists():

    try:

        for element in desktop.descendants(control_type="MenuItem"):

            try:
                name = element.window_text()

                if name and name.strip() == "Public":
                    public_item = element
                    break

            except Exception:
                pass

    except Exception:
        pass


if public_item is None:

    print()
    print("ERROR: Public option was not found.")
    exit(1)


print("[OK] Public option found.")

public_item.click_input()

time.sleep(1)


# ============================================================
# 11. CONTINUE SECURITY WARNING
# ============================================================

print("[13] Waiting for security confirmation...")

continue_button = None

end_time = time.time() + 5

while time.time() < end_time:

    try:

        continue_button = desktop.window(
            title="Visual Studio Code"
        ).child_window(
            title="Continue",
            control_type="Button"
        )

        if continue_button.exists(timeout=0.5):
            break

    except Exception:
        pass

    time.sleep(0.3)


if continue_button is None or not continue_button.exists():

    # Search globally
    try:

        for window in desktop.windows():

            try:

                button = window.child_window(
                    title="Continue",
                    control_type="Button"
                )

                if button.exists(timeout=0.5):
                    continue_button = button
                    break

            except Exception:
                pass

    except Exception:
        pass


if continue_button is None or not continue_button.exists():

    print()
    print("ERROR: Continue button was not found.")
    exit(1)


print("[OK] Continue button found.")

continue_button.click_input()

time.sleep(2)


# ============================================================
# DONE
# ============================================================

print()
print("============================================")
print(" SUCCESS")
print("============================================")
print()
print(f"Port {PORT} has been forwarded.")
print("Port visibility: PUBLIC")
print()
print("Automation completed.")
print()