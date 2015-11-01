import logging
import os

log = logging.getLogger(__name__)

CONFIG_DIR = os.path.expanduser("~/.brewbro/")

def init():
	if not os.path.exists(CONFIG_DIR):
		log.info("Creating config directory: %s", CONFIG_DIR)
		os.makedirs(CONFIG_DIR)