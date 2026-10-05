import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sessions import StringSession

load_dotenv()

TG_API_ID = os.getenv("TG_API_ID")
TG_API_HASH = os.getenv("TG_API_HASH")
TG_PHONE = os.getenv("TG_PHONE")

async def main():
    if not TG_API_ID or not TG_API_HASH:
        print("Please ensure TG_API_ID and TG_API_HASH are set in .env")
        return

    print("=======================================================")
    print("  Telegram StringSession Generator for Cloud / GitHub  ")
    print("=======================================================\n")
    
    async with TelegramClient(StringSession(), int(TG_API_ID), TG_API_HASH) as client:
        session_str = client.session.save()
        print("\nSUCCESS! Your TG_SESSION_STRING is:\n")
        print(session_str)
        print("\n=======================================================")
        print("Copy the string above and add it as a secret named")
        print("TG_SESSION_STRING in your GitHub Repository Secrets.")
        print("=======================================================\n")

        # Also append it to local .env for convenience
        with open(".env", "a", encoding="utf-8") as f:
            f.write(f"\nTG_SESSION_STRING={session_str}\n")
        print("Saved to .env as well.")

if __name__ == "__main__":
    asyncio.run(main())
