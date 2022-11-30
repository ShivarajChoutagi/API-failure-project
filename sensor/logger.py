import logging
import os
from datetime import datetime
import os
#log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H_%M_%S')}.log"
#log dir name
LOG_FILE_DIR = os.path.join(os.getcwd(),'logs')

#create folder if not awailable
os.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctim)s]%(lineno)d%(names)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

