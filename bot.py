import env
import logging
import asyncio
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(level=logging.INFO, encoding="utf-8", format="%(asctime)s - %(levelname)s - \033[32m%(pathname)s: \033[31m\033[1m%(message)s \033[0m")

app = Client(
    "Session_bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins={'root': 'StringSessionBot'},
)

async def main():
    logging.info("Starting the bot")
    try:
        await app.start()  # Await the app.start() coroutine
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    
    uname = "lisztomanic_string_bot"
    logging.info(f"@{uname} is now running!")
    
    await idle()  # Await the idle coroutine
    await app.stop()  # Await the app.stop() coroutine
    
    logging.info("Bot stopped. Alvida!")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine in the event loop
