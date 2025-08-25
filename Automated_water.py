#  python -m Automated_water
#  .\venv\Scripts\activate  

import telegram
import time
import random
import os
import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
print(API_TOKEN)
CHAT_ID = os.getenv('CHAT_ID')
print(CHAT_ID)

# --- SCRIPT LOGIC ---
# 2. Define the function as asynchronous with "async def"
async def send_random_voice_message(bot, chat_id):
    """Selects and sends a random voice message."""
    
    try:
        # --> ADDED: Get the current time and format it into a nice string
        now = datetime.now()
        hour_string = now.strftime("%I").lstrip('0')
        minute_string = now.strftime("%M")

        time_string = f"{hour_string}点{minute_string}分了哦~"
        
        message_text = f"Hi~ BB💗, 现在是{time_string}"
        
        print("Sending text message with the current time...")
        # --> ADDED: Send the text message
        await bot.send_message(chat_id=chat_id, text=message_text)
        print("Text message sent successfully! ✅")

    except Exception as e:
        print(f"An error occurred while sending the text message: {e}")

    # --- Part 2: Send the random voice message ---
    voice_files = [f'Water {i}.ogg' for i in range(1, 9)]
    
    try:
        chosen_file = random.choice(voice_files)
        
        if os.path.exists(chosen_file):
            print(f"Sending {chosen_file}...")
            with open(chosen_file, 'rb') as voice_note:
                # 3. "await" the function call to wait for it to complete
                await bot.send_voice(chat_id=chat_id, voice=voice_note)
            print("Message sent successfully! ✅")
        else:
            print(f"Error: File '{chosen_file}' not found.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# 4. Create a main async function to run your loop
async def main():
    """The main async loop to run the bot task."""
    my_bot = telegram.Bot(token=API_TOKEN)
    print("Bot started. Sending the first message now...")
    
    while True:
        await send_random_voice_message(my_bot, CHAT_ID)
        print("Waiting for 1 hour until the next message... 🕒")
        # Use asyncio's sleep, as time.sleep() can block async code
        await asyncio.sleep(3600)

# --- START THE SCRIPT ---
if __name__ == '__main__':
    # 5. Use asyncio.run() to start the asynchronous program
    asyncio.run(main())

