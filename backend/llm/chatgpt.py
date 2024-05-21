"""
ChatGPT model integration using OpenAI API.
"""

import os

from openai import OpenAI

def get_chatgpt(content: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Get text completion from ChatGPT model.
    
    :param content: The input content for ChatGPT.
    :param model: The ChatGPT model to use.
    :return: Generated text.
    """
    client = OpenAI(
        api_key = os.environ["OPENAI_API_KEY"],
    )
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "system", "content": "You are a part of a transcriber. You will get long transcribed audio files as text and you job is it to summarize the said text into a short and comprehensible summary. Structure the text like following:\n<h2>Topics</h2>Bullet list of all topics<h3>first topic</h3><p>Summery of the first topic</p>n<h3>second topic</h3><p>Summery of the second topic</p>...\nOutput the result in the same language as the text provided by the user. Make sure to always output correct HTML code. DO NOT ADD ADDITIONAL INFORMATION! ONLY USE THE INFORMATION AND CONTEXT FROM THE PROVIDED TEXT!"}, {"role": "user", "content": content}],
            model=model,
        )
        return chat_completion.choices[0].message.content # pylint: disable=unsubscriptable-object
    except Exception as e:
        raise RuntimeError(f"ChatGPT generation failed: {str(e)}") from e
