import os

from langchain_openai import AzureOpenAI, AzureChatOpenAI
from singleton import Singleton


class SimpleLLMClient(metaclass=Singleton):
    __version__ = "0.0.1"

    @classmethod
    def get(cls):
        if cls not in cls._instances:
            raise AttributeError("Singleton class not created. Please, instantiate the first object and then retrieve "
                                 "it through `get()` method")
        return cls._instances[cls]

    def __init__(self, api_version, deploy_name):
        self.api_version = api_version
        self.llm = AzureChatOpenAI(deployment_name=deploy_name, temperature=0.3, max_tokens=1024)

    def ask(self, question):
        pass

    def ask_with_chain(self, question):
        pass

    def ask_with_document(self, question: str, document: dict):
        pass


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    # Get the Azure Credential
    client = SimpleLLMClient(
        api_version=os.environ["OPENAI_API_VERSION"],
        deploy_name=os.environ["OPENAI_GPT_DEPLOYMENT_NAME"])
    print(client.ask("What AI can do for me"))
    print("######")
    print(client.ask_with_chain("What AI can do for me?"))



