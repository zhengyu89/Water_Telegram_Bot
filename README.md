## 💧 Automated Water Reminder Bot 
A fun little project I made just to remind my love 💗 to drink water on time. 
Every hour, this bot sends a sweet text message with the current time ⏰ and a random recorded voice message to make it more personal (and funny 😂).

## ✨ Features

  - Sends a cute text message with the current time.
  - Randomly selects a voice recording (from Water 1.ogg to Water 8.ogg) and sends it.
  - Runs forever in a loop — messages are sent every hour.
  - Super simple to set up, just Python + Telegram bot API.

-----

## ⚙️ Setup

1.  Clone this repo:

<!-- end list -->

```bash
git clone <your-repo-url>
cd Automated_water
```

2.  Create a virtual environment and activate it:

<!-- end list -->

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3.  Install dependencies:

<!-- end list -->

```bash
pip install python-telegram-bot python-dotenv
```

4.  Create a `.env` file in the root folder with:

<!-- end list -->

```env
API_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
```

5.  Add your recorded messages into the project folder:

<!-- end list -->

```
Water 1.ogg
Water 2.ogg
...
Water 8.ogg
```

6.  Run the bot:

<!-- end list -->

```bash
python -m Automated_water
```

-----

## 📂 File Structure

```
Automated_water/
├── Automated_water.py   # Main script
├── .env                 # Environment variables (not committed)
├── Water 1.ogg
├── Water 2.ogg
└── ...
```

-----

## 🥤 Why?

## Honestly? Just because I want to remind my love to drink water 🥺💗 in the sweetest and most random way possible. Yes, I could just text her... but where’s the fun in that? 😎

## 🚀 Future Ideas

  - Add more random voice lines.
  - Schedule different reminders (morning vs night).
  - Maybe send stickers or GIFs too.

-----

Made with ❤️, Python, and way too much free time.
