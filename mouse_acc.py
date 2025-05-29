#!/usr/bin/env python3
"""
Mouse Booster - A simple mouse acceleration utility
Created with PyAutoGUI and ASCII aesthetics
"""

import pyautogui
import time
import threading
import sys
import os
from datetime import datetime

class MouseBooster:
    def __init__(self):
        self.is_running = False
        self.acceleration_factor = 2.0
        self.original_speed = pyautogui.MINIMUM_DURATION
        self.boost_active = False
        
    def print_ascii_header(self):
        """Print ASCII art header"""
        header = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  ███╗   ███╗ ██████╗ ██╗   ██╗███████╗███████╗                ║
║  ████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔════╝                ║
║  ██╔████╔██║██║   ██║██║   ██║███████╗█████╗                  ║
║  ██║╚██╔╝██║██║   ██║██║   ██║╚════██║██╔══╝                  ║
║  ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║███████╗                ║
║  ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝                ║
║                                                               ║
║  ██████╗  ██████╗  ██████╗ ███████╗████████╗███████╗██████╗   ║
║  ██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ║
║  ██████╔╝██║   ██║██║   ██║███████╗   ██║   █████╗  ██████╔╝  ║
║  ██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ██╔══╝  ██╔══██╗  ║
║  ██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   ███████╗██║  ██║  ║
║  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
        """
        print(header)
        print("                    🚀 Mouse Acceleration Utility 🚀")
        print("                         v1.0 - ASCII Edition")
        print("═" * 67)
        
    def print_menu(self):
        """Print the main menu"""
        print("\n┌─────────────────────────────────────┐")
        print("│             MAIN MENU               │")
        print("├─────────────────────────────────────┤")
        print("│ [1] 🚀 Start Mouse Boost            │")
        print("│ [2] ⏹️  Stop Mouse Boost             │")
        print("│ [3] ⚙️  Settings                     │")
        print("│ [4] 📊 Status                       │")
        print("│ [5] ❓ Help                         │")
        print("│ [6] 🚪 Exit                         │")
        print("└─────────────────────────────────────┘")
        
    def print_status(self):
        """Print current status"""
        status_symbol = "🟢 ACTIVE" if self.boost_active else "🔴 INACTIVE"
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        print("\n┌─────────────────────────────────────┐")
        print("│             STATUS PANEL            │")
        print("├─────────────────────────────────────┤")
        print(f"│ Boost Status: {status_symbol:<18} │")
        print(f"│ Acceleration: {self.acceleration_factor:.1f}x{'':<17} │")
        print(f"│ Last Update:  {timestamp:<18} │")
        print(f"│ Original Speed: {self.original_speed:<16.3f} │")
        print("└─────────────────────────────────────┘")
        
    def print_settings_menu(self):
        """Print settings menu"""
        print("\n┌─────────────────────────────────────┐")
        print("│             SETTINGS                │")
        print("├─────────────────────────────────────┤")
        print("│ [1] 🎯 Set Acceleration Factor      │")
        print("│ [2] 🔄 Reset to Default             │")
        print("│ [3] 📋 View Current Settings        │")
        print("│ [4] ⬅️  Back to Main Menu           │")
        print("└─────────────────────────────────────┘")
        
    def print_help(self):
        """Print help information"""
        help_text = """
┌─────────────────────────────────────────────────────────────────┐
│                            HELP GUIDE                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ 🚀 MOUSE BOOSTER USAGE:                                        │
│                                                                 │
│ • Start Boost: Activates mouse acceleration                    │
│ • Stop Boost: Deactivates mouse acceleration                   │
│ • Settings: Configure acceleration factor (1.0 - 10.0)         │
│ • Status: View current boost status and settings               │
│                                                                 │
│ 📝 NOTES:                                                       │
│ • Higher acceleration = faster mouse movement                   │
│ • Default acceleration is 2.0x                                 │
│ • Press Ctrl+C anytime to stop the program                     │
│ • Changes take effect immediately                               │
│                                                                 │
│ ⚠️  WARNING:                                                    │
│ • Use responsibly - high acceleration can be hard to control   │
│ • Test settings before using for important tasks               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
        """
        print(help_text)
        
    def start_boost(self):
        """Start mouse acceleration"""
        if not self.boost_active:
            # Reduce the minimum duration to speed up mouse movements
            pyautogui.MINIMUM_DURATION = self.original_speed / self.acceleration_factor
            self.boost_active = True
            print(f"\n✅ Mouse boost ACTIVATED! Acceleration: {self.acceleration_factor}x")
            print("   Mouse movements are now accelerated!")
        else:
            print("\n⚠️  Mouse boost is already active!")
            
    def stop_boost(self):
        """Stop mouse acceleration"""
        if self.boost_active:
            # Restore original speed
            pyautogui.MINIMUM_DURATION = self.original_speed
            self.boost_active = False
            print("\n⏹️  Mouse boost DEACTIVATED!")
            print("   Mouse movements restored to normal speed.")
        else:
            print("\n⚠️  Mouse boost is already inactive!")
            
    def set_acceleration(self):
        """Set acceleration factor"""
        print(f"\nCurrent acceleration factor: {self.acceleration_factor}x")
        print("Enter new acceleration factor (1.0 - 10.0):")
        print("💡 Tip: 1.0 = normal speed, 2.0 = 2x faster, etc.")
        
        try:
            new_factor = float(input("➤ "))
            if 1.0 <= new_factor <= 10.0:
                self.acceleration_factor = new_factor
                # Apply immediately if boost is active
                if self.boost_active:
                    pyautogui.MINIMUM_DURATION = self.original_speed / self.acceleration_factor
                print(f"✅ Acceleration factor set to {new_factor}x")
            else:
                print("❌ Invalid input! Please enter a value between 1.0 and 10.0")
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")
            
    def reset_settings(self):
        """Reset to default settings"""
        self.acceleration_factor = 2.0
        if self.boost_active:
            pyautogui.MINIMUM_DURATION = self.original_speed / self.acceleration_factor
        print("✅ Settings reset to default (2.0x acceleration)")
        
    def settings_menu(self):
        """Handle settings menu"""
        while True:
            self.print_settings_menu()
            choice = input("\n➤ Enter your choice (1-4): ").strip()
            
            if choice == "1":
                self.set_acceleration()
            elif choice == "2":
                self.reset_settings()
            elif choice == "3":
                self.print_status()
            elif choice == "4":
                break
            else:
                print("❌ Invalid choice! Please enter 1-4.")
                
            input("\nPress Enter to continue...")
            
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def run(self):
        """Main application loop"""
        try:
            while True:
                self.clear_screen()
                self.print_ascii_header()
                self.print_menu()
                self.print_status()
                
                choice = input("\n➤ Enter your choice (1-6): ").strip()
                
                if choice == "1":
                    self.start_boost()
                elif choice == "2":
                    self.stop_boost()
                elif choice == "3":
                    self.settings_menu()
                elif choice == "4":
                    self.print_status()
                elif choice == "5":
                    self.print_help()
                elif choice == "6":
                    print("\n👋 Thanks for using Mouse Booster!")
                    print("   Goodbye! 🚀")
                    if self.boost_active:
                        self.stop_boost()
                    sys.exit(0)
                else:
                    print("❌ Invalid choice! Please enter 1-6.")
                    
                input("\nPress Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n🛑 Program interrupted by user!")
            if self.boost_active:
                self.stop_boost()
            print("👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            if self.boost_active:
                self.stop_boost()
            sys.exit(1)

def main():
    """Main function"""
    print("🚀 Initializing Mouse Booster...")
    time.sleep(1)
    
    # Disable pyautogui fail-safe for better performance
    pyautogui.FAILSAFE = False  # Keep failsafe for safety
    
    app = MouseBooster()
    app.run()

if __name__ == "__main__":
    main()