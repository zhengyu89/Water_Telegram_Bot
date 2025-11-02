import telegram
import os
import asyncio
from dotenv import load_dotenv

# python -m Sent_message.py

# --- SCRIPT SETUP ---
# Load environment variables from a .env file
load_dotenv()

# Get API Token and Chat ID from environment variables
API_TOKEN = os.getenv('API_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# --- SCRIPT LOGIC ---

async def send_text_message(bot, chat_id, message_text):
    """Sends a given text message to the specified chat ID."""
    
    # Check if the message is not empty
    if not message_text:
        print("Message is empty. Nothing to send.")
        return

    try:
        print(f"Sending message: '{message_text}'...")
        # Use 'await' to wait for the message sending to complete
        await bot.send_message(chat_id=chat_id, text=message_text)
        print("Message sent successfully! ✅")
        
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

async def main():
    """The main async function to run the bot task."""
    
    # Check if API_TOKEN and CHAT_ID are set
    if not API_TOKEN or not CHAT_ID:
        print("Error: API_TOKEN or CHAT_ID is not set in the .env file.")
        print("Please create a '.env' file with your bot's API_TOKEN and the target CHAT_ID.")
        return

    # Initialize the bot with your token
    my_bot = telegram.Bot(token=API_TOKEN)
    print("Bot is ready. You can now send messages.")
    print("Type your message and press Enter. Type 'exit' or 'quit' to close the program.")
    
    # Loop indefinitely to keep asking for user input
    while True:
        # Get input from the user in the terminal
        user_input = input("\n> ")

        # Allow the user to exit the loop
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting program. Goodbye!")
            break
        
        # Call the asynchronous function to send the message
        await send_text_message(my_bot, CHAT_ID, user_input)

# --- START THE SCRIPT ---
if __name__ == '__main__':
    # Use asyncio.run() to start the asynchronous program
    asyncio.run(main())
