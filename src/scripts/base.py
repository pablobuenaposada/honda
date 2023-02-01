import asyncio
import logging
from datetime import datetime

from part.lambdas import add_stock
from part.models import Part
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)


class Config:
    client = None
    manager_method = "stocked_parts_last"


def run():
    client = Config.client()
    current = 0
    for part in getattr(Part.objects, Config.manager_method)().iterator():

        def log_message(message, part):
            return f"{datetime.now()}: Stock:{part.reference} {message}"

        logger.info(log_message("searching stock", part))
        try:
            parsed_stock = asyncio.run(client.get_part(part.reference))
            if parsed_stock:
                if type(parsed_stock) == list:
                    for stock in parsed_stock:
                        add_stock(stock)
                else:
                    add_stock(parsed_stock)
            else:
                logger.info(log_message("not found"))
        except Exception as error:
            capture_exception(error)
            logger.info(log_message(error))
        current += 1
