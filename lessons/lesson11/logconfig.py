import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="a",
    format="%(levelname)s -  %(asctime)s  [%(process)d] [%(filename)s] - %(message)s",
)
