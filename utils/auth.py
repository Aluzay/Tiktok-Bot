"""
Authentification to TikTok
"""
import json
import time
import os
import random
from pathlib import Path

def get_credentials():
    """Get the email and password from the credentials file"""
    try:
        from credentials import EMAIL, PASSWORD
        return EMAIL, PASSWORD
    except ImportError:
        print("Error: credentials.py file not found")
        print("Please create a credentials.py file based on credentials_example.py")
        exit(1)

def login(page):
    """Logs into TikTok and saves the cookies"""
    from config import COOKIES_FILE
    EMAIL, PASSWORD = get_credentials()
    
    # Create the data folder if it doesn't exist
    Path(os.path.dirname(COOKIES_FILE)).mkdir(parents=True, exist_ok=True)
    
    try:
        page.goto("https://www.tiktok.com/login/phone-or-email/email")
        
        time.sleep(5)
        username_input = page.locator("input[name='username']")
        username_input.click()
        
        for char in EMAIL:
            username_input.type(char, delay=random.uniform(50, 150))
            
        password_input = page.locator("input[type='password']")
        password_input.click()
        
        for char in PASSWORD:
            password_input.type(char, delay=random.uniform(50, 150))

        time.sleep(2)        
        page.click("button[type='submit']")
                
        # Wait for captcha if necessary
        input("Press Enter to continue...")
        
        # Save the cookies
        cookies = page.context.cookies()
        with open(COOKIES_FILE, "w") as file:
            json.dump(cookies, file)
        print("Cookies sauvegardés avec succès")
        
        return True
    except Exception as e:
        print(f"Erreur lors de la connexion: {e}")
        return False