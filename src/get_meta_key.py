import json
from return_metadata import *
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ========================================================================================================
# This method returns the key that user needs to search from the instance metadata json
# ========================================================================================================
def search(search_key):
     try:
        metadata_json = return_metadata()

        # load the json string into dictionary
        resp = json.loads(metadata_json)

        # loops through the key values in the dictionary
        for key, value in resp.items():
            if key == search_key:
                return(value)
     except Exception as err:
        logger.error("Unable to get the value of the key from the metadata due to exception %s" %err)


# ========================================================================================================
# This main method takes 1 runtime parameter when prompted
# 1. Key to be searched from the instance metadata
# ========================================================================================================
if __name__ == '__main__':
    key = input("Please enter the meta data key to be searched:\n")
    print("%s:%s" %(key,search(key)))
