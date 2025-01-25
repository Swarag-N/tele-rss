# Tele-RSS: Telegram RSS Feed Bot

Tele-RSS is a Python-based tool that fetches the latest posts from RSS feeds and sends them to a specified Telegram group or user via a bot. It integrates seamlessly with GitHub Actions to automate daily updates.

## Features

- Fetches posts from multiple RSS feeds.
- Filters and sends the top 5 posts for each feed.
- Automates daily notifications via Telegram.
- Scheduled updates using GitHub Actions.

---

## Getting Started

### Prerequisites

- Python 3.7 or later
- Telegram bot token and group/user ID
- RSS feed URLs (JSON format)

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/tele-rss.git
   cd tele-rss
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` File:**
   Add the following to a `.env` file:
   ```
   BOT_API=<Your_Telegram_Bot_Token>
   G_ID=<Your_Group_or_User_ID>
   ```

4. **Prepare RSS Feed Data:**
   Define your RSS feeds in `data/rss.json`:
   ```json
   {
       "feeds": [
           {
               "link": "https://hnrss.org/newest",
               "name": "HRANK"
           },
           {
               "link": "https://www.theverge.com/rss/index.xml",
               "name": "VERGE"
           },
           {
               "link": "https://www.seangoedecke.com/rss.xml",
               "name": "sean goedecke"
           }
       ]
   }
   ```

---

## Usage

1. **Run the Script Locally:**
   ```bash
   python main.py
   ```

2. **Automate Updates with GitHub Actions:**
   The provided `.github/workflows/SendUpdates.yaml` file is pre-configured to:
   - Run daily at a specified time.
   - Send updates to your Telegram group/user.

   Add your Telegram bot secrets to the repository settings under `Settings > Secrets and variables > Actions`:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHANNEL_ID`

---

## File Structure

```
tele-rss/
├── data/
│   └── rss.json               # RSS feed configuration
├── main.py                    # Main script to fetch and send updates
├── requirements.txt           # Python dependencies
├── .github/
│   └── workflows/
│       └── SendUpdates.yaml   # GitHub Actions workflow
└── README.md                  # Project documentation
```

---

## Example Output

The Telegram bot sends a message like this:

```
HRANK

Post Title 1
Author: Author Name
Link: https://example.com/post1

Post Title 2
Author: Author Name
Link: https://example.com/post2

...

VERGE

Post Title 1
Author: Author Name
Link: https://example.com/post1
```

---

## Contribution

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- [feedparser](https://github.com/kurtmckee/feedparser) for RSS parsing.
- [python-telegram-bot](https://python-telegram-bot.org/) for Telegram integration.
