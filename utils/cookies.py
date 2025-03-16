"""
Cookie management for TikTok
"""
import json
import os

def load_cookies(page):
    """Load cookies from file"""
    from config import COOKIES_FILE
    
    try:
        if not os.path.exists(COOKIES_FILE):
            print(f"Cookies file not found: {COOKIES_FILE}")
            return False
        print("Loading cookies...")
        with open(COOKIES_FILE, "r") as file:
            cookies = json.load(file)
        
        page.context.add_cookies(cookies)
        print("Cookies loaded successfully")
        return True
    except Exception as e:
        print(f"Error loading cookies: {e}")
        return False
