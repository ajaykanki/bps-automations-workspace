from shared import log
from core import app
from settings import config
from pprint import pprint
import logging

logging.basicConfig(level=logging.DEBUG if config.is_dev else logging.WARNING)


def run_worker():
    log.info("Starting worker...")
    if config.is_dev:
        pprint(config.model_dump())

    validate_config()
    apply_schema()
    app.run_worker(
        concurrency=config.worker.concurrency,
        name=config.worker.name,
        queues=config.worker.queues,
    )


def apply_schema():
    with app.open():
        try:
            app.schema_manager.apply_schema()
        except Exception:
            log.warning("Schema already applied or failed to apply schema")


def validate_config():
    log.info("Validating configuration...")
    if not config.database_url:
        log.error("DATABASE_URL is not set in environment variables. Exiting.")
        exit(1)

    if not config.sap.validate_config():
        log.error("SAP configuration is invalid. Exiting.")
        exit(1)
    return


if __name__ == "__main__":
    run_worker()
