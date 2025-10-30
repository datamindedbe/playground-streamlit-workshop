import google.generativeai as genai


def get_ai_response(
    prompt: str,
    stringified_dataframe: str | None = None,
    model_name: str = "gemini-2.0-flash",
) -> str:
    model = genai.GenerativeModel(model_name)

    content_to_send = []

    if stringified_dataframe is None:
        return None

    # If a dataframe string is given, combine it with the prompt.
    # This provides clear context to the model.
    combined_prompt = f"""
    You are a data analyst. Please analyze the following data:

    <data>
    {stringified_dataframe}
    </data>

    Based *only* on the data provided, please answer this question:
    {prompt}
    """
    content_to_send = [combined_prompt]

    # Generate the content
    response = model.generate_content(content_to_send)

    return response.text
