from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync, StealthConfig
import time
import random
import json
from utils.auth import get_credentials, login
from utils.cookies import load_cookies
from config import COOKIES_FILE, TIKTOK_USERNAMES, WAIT_TIME

def main():
    with sync_playwright() as p:
        # Simulate a browser to not being detected as a bot
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            viewport={"width": 1280, "height": 720},
            permissions=["geolocation"],
            geolocation={"latitude": 48.8566, "longitude": 2.3522},  # (Paris)
            locale="fr-FR"
        )
        page = context.new_page()
        config = StealthConfig(navigator_languages=False, navigator_vendor=False, navigator_user_agent=False)
        stealth_sync(page, config)
        
        # Try to load cookies
        cookies_loaded = load_cookies(page)
        print("Cookies loaded" if cookies_loaded else "No cookie found")
        # If no cookies or expired load it again
        if not cookies_loaded:
            print("Connection required (no cookies)...")
            login(page)
            load_cookies(page)
        
        page.goto("https://www.tiktok.com/foryou", wait_until="load")	
        print("Tiktok opened")
        
        for username in TIKTOK_USERNAMES:
            share_button = page.locator('[data-e2e="share-btn"]').nth(0)
            share_button.click()
            
            share_message_button = page.locator('[data-e2e="share-message"]')
            share_message_button.click()
            
            search_input = page.get_by_role("textbox", name="Rechercher").nth(1)
            search_input.click()
            search_input.fill(username)         
                
        input("Press Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    main()