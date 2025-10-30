import google.generativeai as genai


# TODO
def pass_upload_to_ai():
    pass


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
    """
    content_to_send = [combined_prompt]

    # Generate the content
    response = model.generate_content(content_to_send)

    return response.text
