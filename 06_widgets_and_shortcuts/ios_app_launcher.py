#!/usr/bin/env python3
"""
📱 iOS App Launcher & Deep Link URL Schemes
Launches external iOS applications directly from Python using iOS URL Schemes and Deep Links.
Supports Camera, Settings, Maps, Safari, Messages, Mail, Music, Files, Shortcuts, and third-party apps.
"""

import sys
import os
import webbrowser
import time

# Catalog of standard iOS Deep Links & URL Schemes
APPS_CATALOG = [
    ("1", "Settings App (Pyto Permissions & Wi-Fi)", "app-settings:"),
    ("2", "Apple Maps (Current Location / Navigation)", "maps://"),
    ("3", "Safari Web Browser (Open Apple.com)", "https://www.apple.com"),
    ("4", "Apple Photos Library", "photos-redirect://"),
    ("5", "Apple Files App", "shareddocuments://"),
    ("6", "Apple Music", "music://"),
    ("7", "Apple Notes App", "mobilenotes://"),
    ("8", "Apple Reminders App", "x-apple-reminderkit://"),
    ("9", "Apple Calendar App", "calshow:"),
    ("10", "Apple App Store", "itms-apps://"),
    ("11", "Apple Shortcuts App", "shortcuts://"),
    ("12", "Messages App (SMS Compose)", "sms:"),
    ("13", "Mail App (Email Compose)", "mailto:"),
    ("14", "YouTube App", "youtube://"),
    ("15", "Spotify Music App", "spotify://"),
    ("16", "WhatsApp Messenger", "whatsapp://"),
    ("17", "Telegram Messenger", "tg://"),
    ("18", "X (formerly Twitter)", "twitter://"),
]

def open_app_url(url_scheme):
    """Opens an app using iOS URL Scheme via webbrowser or pyto_core"""
    print(f"🚀 Launching URL Scheme: {url_scheme} ...")
    try:
        # Try Pyto's core open_url if available
        import pyto_core
        if hasattr(pyto_core, 'open_url'):
            pyto_core.open_url(url_scheme)
            print("✅ URL dispatched via pyto_core.open_url")
            return True
    except Exception:
        pass

    try:
        # Fallback to standard Python webbrowser on iOS
        success = webbrowser.open(url_scheme)
        if success:
            print("✅ URL dispatched via webbrowser.open")
            return True
    except Exception as e:
        print(f"⚠️ Error launching scheme: {e}")

    return False

def show_graphical_app_launcher():
    """Builds a native UIKit Grid UI to launch apps with one tap"""
    try:
        import pyto_ui as ui
    except ImportError:
        return

    def get_system_color(name, legacy_name=None):
        if hasattr(ui, 'SystemColors') and hasattr(ui.SystemColors, name):
            return getattr(ui.SystemColors, name)
        if legacy_name and hasattr(ui, legacy_name):
            return getattr(ui, legacy_name)
        if hasattr(ui, f"COLOR_{name}"):
            return getattr(ui, f"COLOR_{name}")
        return None

    view = ui.View()
    bg_col = get_system_color('SYSTEM_BACKGROUND', 'COLOR_SYSTEM_BACKGROUND')
    if bg_col is not None:
        view.background_color = bg_col
    view.title = "📱 iOS App Launcher"

    title_label = ui.Label()
    title_label.text = "Tap any app icon to launch from Python"
    try:
        title_label.font = ui.Font.bold_system_font_of_size(17)
        if hasattr(ui, 'TextAlignment'):
            title_label.text_alignment = ui.TextAlignment.CENTER
        elif hasattr(ui, 'TEXT_ALIGNMENT_CENTER'):
            title_label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
    except Exception:
        pass
    title_label.size = (340, 30)
    title_label.center = (view.width / 2, 35)

    # Top App Buttons
    quick_apps = [
        ("⚙️ Settings", "app-settings:", get_system_color('SYSTEM_GRAY', 'COLOR_SYSTEM_GRAY')),
        ("🗺️ Maps", "maps://", get_system_color('SYSTEM_GREEN', 'COLOR_SYSTEM_GREEN')),
        ("🌐 Safari", "https://www.apple.com", get_system_color('SYSTEM_BLUE', 'COLOR_SYSTEM_BLUE')),
        ("📸 Photos", "photos-redirect://", get_system_color('SYSTEM_ORANGE', 'COLOR_SYSTEM_ORANGE')),
        ("📁 Files", "shareddocuments://", get_system_color('SYSTEM_BLUE', 'COLOR_SYSTEM_BLUE')),
        ("🎵 Music", "music://", get_system_color('SYSTEM_RED', 'COLOR_SYSTEM_RED')),
        ("⚡ Shortcuts", "shortcuts://", get_system_color('SYSTEM_PURPLE', 'COLOR_SYSTEM_PURPLE')),
        ("📝 Notes", "mobilenotes://", get_system_color('SYSTEM_YELLOW', 'COLOR_SYSTEM_YELLOW')),
    ]

    button_container = ui.View()
    button_container.size = (340, 320)
    button_container.center = (view.width / 2, 220)

    btn_w = 155
    btn_h = 60
    gap = 12

    for i, (name, scheme, col) in enumerate(quick_apps):
        row = i // 2
        col_idx = i % 2
        x = col_idx * (btn_w + gap)
        y = row * (btn_h + gap)

        btn = ui.Button()
        btn.title = name
        if col is not None:
            btn.background_color = col
        white_col = get_system_color('WHITE', 'COLOR_WHITE')
        if white_col is not None:
            btn.title_color = white_col
        btn.corner_radius = 14
        btn.size = (btn_w, btn_h)
        btn.frame = (x, y, btn_w, btn_h)

        def make_action(target_scheme):
            def action_handler(sender):
                open_app_url(target_scheme)
                try:
                    ui.HapticFeedback(ui.HapticFeedback.IMPACT_MEDIUM).generate()
                except Exception:
                    pass
            return action_handler

        btn.action = make_action(scheme)
        button_container.add_subview(btn)

    view.add_subview(title_label)
    view.add_subview(button_container)

    mode = getattr(ui.PresentationMode, 'SHEET', None) if hasattr(ui, 'PresentationMode') else getattr(ui, 'PRESENTATION_MODE_SHEET', 0)
    if mode is not None:
        ui.show_view(view, mode=mode)
    else:
        ui.show_view(view)

def main():
    print("=" * 60)
    print("  📱 iOS App Launcher & Deep Link Manager")
    print("=" * 60)
    print("Select an app to open on your iPhone:")
    print("-" * 60)

    for num, name, scheme in APPS_CATALOG:
        print(f"   [{num:>2}] {name:<42} ({scheme})")

    print("\n   [ G] 🎨 Open Graphical UIKit Launcher")
    print("   [ C] ✏️ Enter Custom URL Scheme")
    print("   [ 0] 🚪 Cancel / Exit")
    print("=" * 60)

    choice = input("👉 Enter choice and press Enter: ").strip()

    if choice == "0" or choice.lower() == "exit" or choice.lower() == "q":
        return
    elif choice.lower() == "g":
        show_graphical_app_launcher()
        return
    elif choice.lower() == "c":
        custom_scheme = input("👉 Enter custom URL scheme (e.g. twitter:// or https://google.com): ").strip()
        if custom_scheme:
            open_app_url(custom_scheme)
        return

    selected_scheme = None
    for num, name, scheme in APPS_CATALOG:
        if choice == num:
            selected_scheme = scheme
            break

    if selected_scheme:
        open_app_url(selected_scheme)
    else:
        print("⚠️ Invalid selection.")

if __name__ == "__main__":
    main()
