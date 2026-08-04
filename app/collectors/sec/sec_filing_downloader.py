import time

import requests

from app.logger.logger import logger


class SECFilingDownloader:

    def download(
        self,
        url
    ):

        headers = {

            "User-Agent": (
                "CatalystScanner "
                "(kamillimak121212@gmail.com)"
            )

        }

        try:

            time.sleep(0.2)

            response = requests.get(
                url,
                headers=headers,
                timeout=30
            )

            logger.info(
                f"Download status: {response.status_code}"
            )

            if response.status_code != 200:

                logger.warning(
                    f"Cannot download filing: {url}"
                )

                return None

            logger.info(
                f"Downloaded {len(response.text)} characters"
            )

            return response.text

        except Exception as e:

            logger.error(
                f"Download failed: {e}"
            )

            return None