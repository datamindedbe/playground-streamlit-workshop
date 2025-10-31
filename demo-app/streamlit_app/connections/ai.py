import google.generativeai as genai
from PIL import Image


def get_ai_response_on_stringified_dataframe(
    prompt: str,
    stringified_dataframe: str,
    model_name: str = "gemini-2.0-flash",
) -> str:
    model = genai.GenerativeModel(model_name)

    content_to_send = []

    # If a dataframe string is given, combine it with the prompt.
    # This provides clear context to the model.
    combined_prompt = f"""
    You are a data analyst. Please analyze the following data:

    <data>
    {stringified_dataframe}
    </data>

    Based *only* on the data provided, please answer this question:
    {prompt}

    Keep your answer as succint and to the point as possible.
    """
    content_to_send = [combined_prompt]

    # Generate the content
    response = model.generate_content(content_to_send)

    return response.text


def get_ai_response_on_image(
    prompt: str, image: Image, model_name: str = "gemini-2.0-flash"
) -> str:
    content_to_send = [prompt, image]
    model = genai.GenerativeModel(model_name)

    response = model.generate_content(contents=content_to_send)

    return response.text
