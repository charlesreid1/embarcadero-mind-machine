import boringmindmachine as bmm
import logging
from github import Github
import time, random

class GithubSheep(bmm.BoringSheep):
    """
    Sheep are created by the Shepherd.
    Sheep are initialized with a JSON key file plus parameters from the Shepherd.
    Sheep are expected to take care of their own API instance.
    """
    def __init__(self, bot_key, **kwargs):

        # Initialize your API instance
        self.api = Github(bot_key['token']['access_token'])
        self.params = bot_key
        self.name = bot_key['username']

        # No kwargs used.

    def hello(self):
        time.sleep(random.randint(1,10))
        logger = logging.getLogger('rainbowmindmachine')
        msg = "Hello world! This is bot %s"%(self.name)
        logger.info(msg)

