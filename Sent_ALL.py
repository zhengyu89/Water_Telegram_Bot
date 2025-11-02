import telegram
import os
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- CONFIGURATION ---
# Get your API Token and Chat ID from environment variables
API_TOKEN = os.getenv('API_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# --- SCRIPT LOGIC ---
async def main():
    """
    Connects to the bot, sends all voice messages in sequence,
    and then sends a final confirmation message.
    """
    # --- Part 1: Initialization ---
    if not API_TOKEN or not CHAT_ID:
        print("Error: API_TOKEN or CHAT_ID is not set.")
        print("Please make sure your .env file is configured correctly.")
        return

    print("Initializing bot...")
    my_bot = telegram.Bot(token=API_TOKEN)
    print("Bot started successfully! ✅")

    # Create a list of all the voice files you want to send
    voice_files = [f'Water {i}.ogg' for i in range(1, 9)] # Creates ['Water 1.ogg', 'Water 2.ogg', ..., 'Water 8.ogg']

    # --- Part 2: Send All Voice Messages ---
    print("\n--- Starting to send all voice messages ---")
    all_sent_successfully = True
    for file_to_send in voice_files:
        try:
            # Check if the file exists before trying to send it
            if os.path.exists(file_to_send):
                print(f"Sending {file_to_send}...")
                # Open the file in binary read mode ('rb')
                with open(file_to_send, 'rb') as voice_note:
                    # Send the voice message
                    await my_bot.send_voice(chat_id=CHAT_ID, voice=voice_note)
                print(f"Successfully sent {file_to_send}! ✅")
            else:
                print(f"Error: File '{file_to_send}' not found. Skipping.")
                all_sent_successfully = False
            
            # A small delay between messages can prevent rate-limiting issues
            await asyncio.sleep(1)

        except Exception as e:
            print(f"An error occurred while sending {file_to_send}: {e}")

    print("\n--- All voice messages have been sent. ---")

    # --- Part 3: Send the Final Text Message ---
    try:
        if all_sent_successfully:
            final_message = "Sequence complete! All 8 voice messages have been sent. 😄"
        else:
            final_message = "Sequence finished, but one or more messages failed to send. Please check the log."
            
        print(f"Sending final message: \"{final_message}\"")
        await my_bot.send_message(chat_id=CHAT_ID, text=final_message)
        print("Final message sent successfully! ✅")
    except Exception as e:
        print(f"An error occurred while sending the final message: {e}")

    print("\n--- Script finished ---")


# --- START THE SCRIPT ---
if __name__ == '__main__':
    # Use asyncio.run() to start the asynchronous program
    asyncio.run(main())