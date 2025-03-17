# TikTok Bot

## About This Project

This bot was created for a friend who was traveling for a month and didn’t want to lose his TikTok streaks. He asked me to build a bot that automatically shares one TikTok per day to a list of users.  

Since this was a quick project made to solve a specific need, it might not be perfect, but it gets the job done!  

## Configuration

To use this bot, follow these steps to configure your credentials:

1. Copy the file `credentials_example.py` and rename it to `credentials.py`.
2. Edit `credentials.py` with your personal credentials.
3. Copy the file `config_exemple.py` and rename it to `config.py`
4. Edit `config.py` with the your config
5. Obtain an API key to solve captchas from: [SadCaptcha](https://www.sadcaptcha.com/).

## Important Notes

- If you encounter a captcha-related error, you may have run out of credits. Check your balance here: [SadCaptcha API](https://www.sadcaptcha.com/api/v1/swagger-ui/index.html).
- The files `credentials.py` and `tiktok_cookies.json` are ignored by Git and will not be shared.  
- `tiktok_cookies.json` contain authentication data, so keep it secure.