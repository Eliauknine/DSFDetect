"""
OpenAI / LLM API client wrapper.

Reads configuration from src.config (API key, base URL, model).
"""
import openai
from src.config import OPENAI_API_KEY, OPENAI_BASE_URL, LLM_MODEL


def configure():
    """Initialize the OpenAI client with project settings."""
    openai.api_key = OPENAI_API_KEY
    openai.base_url = OPENAI_BASE_URL


def chat(messages, model=None, temperature=0.2, max_tokens=1000, response_format=None):
    """
    Send a chat completion request.

    Args:
        messages: List of message dicts [{"role": ..., "content": ...}]
        model: Model name override (defaults to LLM_MODEL from config)
        temperature: Sampling temperature (0.0-1.0)
        max_tokens: Max tokens in response
        response_format: Optional {"type": "json_object"} for JSON mode

    Returns:
        Response text string, or empty string on failure.
    """
    configure()
    try:
        kwargs = {
            "model": model or LLM_MODEL,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if response_format:
            kwargs["response_format"] = response_format

        response = openai.chat.completions.create(**kwargs)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[LLM Error] {e}")
        return ""
