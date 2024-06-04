"""
Interface for Large Language Models (LLMs) like ChatGPT.
"""

from llm.chatgpt import get_chatgpt
from llm.falcon import get_falcon

def get_llm_text(prompt: str, content: str, model: str = "chatgpt/gpt-3.5-turbo") -> str:
    """
    Get text generated by LLM based on provided content.
    
    :param prompt: The input instruction for the LLM.
    :param content: The input content for LLM.
    :param model: The LLM model to use.
    :return: Generated text.
    """
    model = "chatgpt/gpt-3.5-turbo" if model == None else model
    llm_family, llm_model = model.split("/")

    if llm_family == "chatgpt":
        return get_chatgpt(prompt, content, llm_model)
    if llm_family == "falcon":
        return get_falcon(prompt, content, llm_model)
    raise ValueError(f"Unsupported LLM family: {llm_family}")
