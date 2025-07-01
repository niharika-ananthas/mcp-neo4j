import os
from openai import AzureOpenAI
import config

class llmConnection():
    def __init__(self):
        self.url = os.environ["llm_endpoint"]
        self.key = os.environ["azure_api_key"]
        self.model = os.environ["model_name"]
        self.api_version = os.environ["api_version"]
        self.deployment = os.environ["deployment"]

    def create_llmConnection(self):
        try:
            llm_connect = AzureOpenAI(
                api_version= self.api_version,
                azure_endpoint=self.url,
                api_key=self.key
            )
        except Exception as e:
            return e