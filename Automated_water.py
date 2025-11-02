#  python -m Automated_water
#  .\venv\Scripts\activate  

# python -m Automated_water
# .\venv\Scripts\activate  

import telegram
import time
import random
import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
print(f"API_TOKEN: {API_TOKEN}")
CHAT_ID = os.getenv('CHAT_ID')
print(f"CHAT_ID: {CHAT_ID}")

# --- SCRIPT LOGIC ---

# MODIFIED: The function now accepts a 'voice_file_path' argument
# instead of choosing a random one inside the function.
async def send_timed_voice_message(bot, chat_id, voice_file_path):
    """Sends a text message with the current time and a specific voice message."""
    
    # --- Part 1: Send the text message with the current time ---
    try:
        now = datetime.now()
        hour_string = now.strftime("%I").lstrip('0')
        minute_string = now.strftime("%M")
        time_string = now.strftime("%I:%M %p").lstrip('0')
        
        message_text = f"Hi there! 💗 The time is now {time_string}."
        
        print("Sending text message with the current time...")
        await bot.send_message(chat_id=chat_id, text=message_text)
        print("Text message sent successfully! ✅")

    except Exception as e:
        print(f"An error occurred while sending the text message: {e}")

    # --- Part 2: Send the provided voice message ---
    try:
        # The function now uses the file path passed to it
        if os.path.exists(voice_file_path):
            print(f"Sending {voice_file_path}...")
            with open(voice_file_path, 'rb') as voice_note:
                await bot.send_voice(chat_id=chat_id, voice=voice_note)
            print("Voice message sent successfully! ✅")
        else:
            print(f"Error: File '{voice_file_path}' not found.")
            
    except Exception as e:
        print(f"An error occurred while sending the voice message: {e}")

# MODIFIED: The main function now handles the shuffling and looping logic.
async def main():
    """The main async loop to run the bot task."""
    my_bot = telegram.Bot(token=API_TOKEN)
    print("Bot started. Initializing message cycle...")
    
    # Create the list of voice files once
    voice_files = [f'Water {i}.ogg' for i in range(1, 9)]
    
    # The outer loop ensures the bot runs forever
    while True:
        print("\n--- Starting a new message cycle. Shuffling files... ---")
        # Shuffle the list of files to randomize the order for this cycle
        random.shuffle(voice_files)
        
        # This inner loop iterates through the shuffled list, sending one file at a time
        for file_to_send in voice_files:
            # Call the function with the specific file from our shuffled list
            await send_timed_voice_message(my_bot, CHAT_ID, file_to_send)
            
            print("Waiting for 1 hour until the next message... 🕒")
            # Use asyncio's sleep, as time.sleep() can block async code
            await asyncio.sleep(3600)
        
        print("\n--- All messages in the cycle have been sent. Restarting loop. ---")


# --- START THE SCRIPT ---
if __name__ == '__main__':
    # Use asyncio.run() to start the asynchronous program
    asyncio.run(main())

