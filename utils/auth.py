"""
Authentification to TikTok
"""
import json
import time
import os
import random
import math
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
    from tiktok_captcha_solver import PlaywrightSolver
    from credentials import API_KEY
    EMAIL, PASSWORD = get_credentials()
    
    # Create the data folder if it doesn't exist
    Path(os.path.dirname(COOKIES_FILE)).mkdir(parents=True, exist_ok=True)
    
    try:
        page.goto("https://www.tiktok.com/login/phone-or-email/email", wait_until="load")
        print("Tiktok login page opened")
                
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
        
        # Solve captcha if present
        captcha_solver = PlaywrightSolver(
            page,
            API_KEY,
            headers={"User-Agent": "Chrome"},
            mouse_step_delay_ms=math.floor(random.uniform(10, 20)),
            mouse_step_size=math.floor(random.uniform(10, 20)),
        )
        time.sleep(2)
        captcha_solver.solve_captcha_if_present()
        time.sleep(2)
        
        # Save the cookies
        cookies = page.context.cookies()
        with open(COOKIES_FILE, "w") as file:
            json.dump(cookies, file)
        print("Cookies saved")
        
        return True
    except Exception as e:
        print(f"Error while connecting: {e}")
        return False