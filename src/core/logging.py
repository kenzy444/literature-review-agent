import logging

log = logging.getLogger("lra")
log.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

# this for files

# file_handler = logging.FileHandler("lra.log")
# file_handler.setFormatter(formatter)
# log.addHandler(file_handler)
