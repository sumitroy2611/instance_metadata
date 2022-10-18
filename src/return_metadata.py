import boto.utils
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

META_URL = 'http://169.254.169.254'
META_PATH = 'meta-data/'
META_VERSION = 'latest'

# ========================================================================================================
# This methods reads the AWS EC2 instance metadata and returns the results in JSON format to the main method
# ========================================================================================================
def return_metadata():
    try:
        value = boto.utils.get_instance_metadata(version=META_VERSION, url=META_URL, data=META_PATH)
        return json.dumps(value, indent=4, sort_keys=True) #This sorts the keys and returns json object with proper indentation
    
    except Exception as err:
        logger.error("Unable to fetch the AWS EC2 meta data due to exception %s" %err)


# ========================================================================================================
# No runtime parameter required for this main method
# ========================================================================================================
if __name__ == "__main__":
    print(return_metadata())
