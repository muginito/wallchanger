#!usr/bin/env python3

import ctypes
import os
import sys

def set_wallpaper(wallpaper_path):
    # Change wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

def add_wallpaper(wallpaper_paths: dict, wallpaper_path: str, wallpaper_label: str):
    # Add wallpaper to path
    wallpaper_paths[wallpaper_label] = wallpaper_path

def main():
    # Define paths to wallpapers
    wallpaper_paths = {
        "wallpaper-1": r"C:\Users\mig\Pictures\Wallpapers\david by ai.png",
        "wallpaper-2": r"C:\Users\mig\Pictures\Wallpapers\Deserted.png"
    }

    # Check for valid wallpaper
    if len(sys.argv) != 2 or sys.argv[1] not in wallpaper_paths:
        print("Invalid usage. Please provide a valid wallpaper option.")
        sys.exit(1)

    # Set wallpaper
    wallpaper_option = sys.argv[1]
    wallpaper_path = wallpaper_paths[wallpaper_option]
    set_wallpaper(wallpaper_path)
    print(f"Wallpaper changed to {wallpaper_option}")

if __name__ == "__main__":
    main()
