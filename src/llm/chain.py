from src.llm.vision_model import get_vision_model, get_output_parser
from langchain_core.prompts import ChatPromptTemplate
from src.llm.prompt_builder import get_bouquet_prompt
def get_bouquet_chain():
    """
    Define and return the chain for bouquet arrangement suggestions.
    :return: LangChain chain combining the prompt, vision model and parser
    """
    vision_model = get_vision_model()
    parser = get_output_parser()
    prompt_template = get_bouquet_prompt()

    vision_chain = prompt_template | vision_model | parser
    return vision_chain
