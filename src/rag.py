from typing import BinaryIO


from models.chat import ChatResponse
from singleton import Singleton


class RetrievalAugmentedGeneration(metaclass=Singleton):
    MAJOR_VERSION = 0
    MINOR_VERSION = 0
    PATCH_VERSION = 0

    def __init__(self,
                 document_intelligence_endpoint: str,
                 document_intelligence_api_key: str,
                 document_intelligence_locale: str,
                 openai_gpt_deployment_name: str,
                 openai_gpt_model_name: str,
                 openai_embedding_deployment_name: str):
        pass

    @classmethod
    def get(cls):
        if cls not in cls._instances:
            raise AttributeError("Singleton class not created. Please, instantiate the first object and then retrieve "
                                 "it through `get()` method")
        return cls._instances[cls]

    def ingest_document(self, stream: BinaryIO, model_id: str):
        pass

    def ask_to_documents(self, question: str) -> ChatResponse:
        pass

    def version(self) -> str:
        return f"{self.MAJOR_VERSION}.{self.MINOR_VERSION}.{self.PATCH_VERSION}"
