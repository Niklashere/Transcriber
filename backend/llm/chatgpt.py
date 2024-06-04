"""
ChatGPT model integration using OpenAI API.
"""

import os

from openai import OpenAI

def get_chatgpt(prompt: str, content: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Get text completion from ChatGPT model.
    
    :param prompt: The input instruction for the LLM.
    :param content: The input content for ChatGPT.
    :param model: The ChatGPT model to use.
    :return: Generated text.
    """
    client = OpenAI(
        api_key = os.environ["OPENAI_API_KEY"],
    )
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": content}],
            model=model,
        )
        return chat_completion.choices[0].message.content # pylint: disable=unsubscriptable-object
    except Exception as e:
        raise RuntimeError(f"ChatGPT generation failed: {str(e)}") from e
