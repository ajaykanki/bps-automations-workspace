import asyncio
import sys
from settings import config
from procrastinate import App, PsycopgConnector

# Set event loop policy only on Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = App(
    connector=PsycopgConnector(conninfo=config.database_url.encoded_string()),
    import_paths=config.worker.import_paths,
)
