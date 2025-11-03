"""Hugging Face LLMs module for LangChain integration."""

from typing import Optional

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

from config.logging import Logger
from config.settings import get_settings
from config.singleton import Singleton


class HuggingFaceLLM(metaclass=Singleton):
    """A class to interact with Hugging Face LLMs using the LangChain interface."""

    def __init__(
        self,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        streaming: bool = False,
        max_tokens: Optional[int] = None,
    ):
        """
        Initialize the HuggingFaceLLM class.
        Args:
            model (str): The name of the Hugging Face model to use.
                        Default is "meta-llama/Meta-Llama-3-8B-Instruct".
            temperature (float): Temperature for generation.
            streaming (bool): Whether to stream responses.
            max_tokens (int): Maximum number of tokens to generate.
        """
        self.settings = get_settings()
        self.logger = Logger().get_logger(self.__class__.__name__)

        self.model = model or self.settings.HUGGING_FACE_DEFAULT_MODEL
        self.temperature = temperature or self.settings.HUGGING_FACE_DEFAULT_TEMPERATURE
        self.streaming = streaming
        self.max_tokens = max_tokens or 1024

    def get_llm(self):
        """Get the Hugging Face LLM instance."""
        self.logger.debug(f"Initializing Hugging Face LLM with model: {self.model}")

        hgf_endpoint = HuggingFaceEndpoint(
            repo_id=self.model,
            temperature=self.temperature,
            max_new_tokens=self.max_tokens,
            huggingfacehub_api_token=self.settings.HUGGING_FACE_API_KEY,
            streaming=self.streaming,
        )

        llm = ChatHuggingFace(llm=hgf_endpoint)

        return llm


class HuggingFaceInferenceLLM(metaclass=Singleton):
    """Alternative using Hugging Face Inference API directly (for newer models)."""

    def __init__(
        self,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        streaming: bool = False,
        max_tokens: Optional[int] = None,
    ):
        """
        Initialize the HuggingFaceInferenceLLM class.
        This uses the Hugging Face Inference API with chat models.
        """
        self.settings = get_settings()
        self.logger = Logger().get_logger(self.__class__.__name__)

        self.model = model or self.settings.HUGGING_FACE_DEFAULT_MODEL
        self.temperature = temperature or self.settings.HUGGING_FACE_DEFAULT_TEMPERATURE
        self.streaming = streaming
        self.max_tokens = max_tokens or 1024

    def get_llm(self):
        """Get the Hugging Face Inference LLM instance."""
        self.logger.debug(f"Initializing HF Inference LLM with model: {self.model}")

        return HuggingFaceEndpoint(
            repo_id=self.model,
            temperature=self.temperature,
            max_new_tokens=self.max_tokens,
            huggingfacehub_api_token=self.settings.HUGGING_FACE_API_KEY,
            streaming=self.streaming,
            task="text-generation",
        )


if __name__ == "__main__":
    print("Testing HuggingFace LLM...")
    hf_llm = HuggingFaceLLM()
    llm_instance = hf_llm.get_llm()
    print(f"LLM instance: {llm_instance}")
    print("================================================")

    try:
        response = llm_instance.invoke("What is the capital of France?")
        print(response.content)
    except Exception as e:
        print(f"Error: {e}")

    print("================================================")
