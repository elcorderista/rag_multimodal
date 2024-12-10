from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from settings.config import Config
def get_vision_model(model_name: str = Config.CHAT_MODEL, temperature: float = Config.MODEL_TEMPERATURE):
    """
    Initialize and return a vision model.
    :param model_name: The name of the vision model.
    :param temperature: The temperature of the vision model.
    :return: ChatOpenAI Initialized vision model.
    """

    vision_model = ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
    )

    return vision_model

def get_output_parser():
    """
    Initialize and return a output parser.
    :return: StrOutputParser: Parser to convert LLM output to string.
    """

    return StrOutputParser()