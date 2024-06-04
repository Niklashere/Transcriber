"""
Falcon model integration using transformers.
"""

from transformers import AutoTokenizer

import transformers
import torch

def get_falcon(prompt: str, content: str, model: str = "falcon-7b-instruct") -> str:
    """
    Get text completion from ChatGPT model.
    
    :param prompt: The input instruction for the LLM.
    :param content: The input content for ChatGPT.
    :param model: The ChatGPT model to use.
    :return: Generated text.
    """
    model = "tiiuae/" + model
    tokenizer = AutoTokenizer.from_pretrained(model)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )

    sequences = pipeline(
        f"SYSTEM:{prompt}\nUSER:{content}\nSUMMARIZED TEXT:",
        max_new_tokens=2048,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )

    result = ""
    for seq in sequences:
        result += seq['generated_text']

    return result.split(content + "\nSUMMARIZED TEXT:")[1]
