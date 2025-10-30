import google.generativeai as genai


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

    ---
    IMPORTANT:
    - If the question asks you to return a modified or new table/dataframe,
        return *ONLY* the data, formatted as a **CSV**.
    - Do not include backticks (```) or the word "csv" in your response.
    - Do not include any other text, explanation, or greeting.
    - If the question is a simple query (e.g., "how many rows..."),
        just answer the question in a natural language sentence.
    ---
    """
    content_to_send = [combined_prompt]

    # Generate the content
    response = model.generate_content(content_to_send)

    return response.text
