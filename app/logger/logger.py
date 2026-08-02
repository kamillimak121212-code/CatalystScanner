import logging
import os
import sys

os.makedirs(
    "logs",
    exist_ok=True
)

logging.basicConfig(

    level=logging.INFO,

    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    ),

    handlers=[

        logging.FileHandler(
            "logs/scanner.log"
        ),

        logging.StreamHandler(
            sys.stdout
        )

    ]

)

logger = logging.getLogger(
    "CatalystScanner"
)