import os
from pathlib import Path
import tempfile
import google.generativeai as genai




def get_ai_response(prompt: str, file = None) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    if file is not None:
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, file.name)
            with open(file_path, "wb") as f:
                f.write(file.read())
            sample_pdf = genai.upload_file(file_path)
            response = model.generate_content([prompt, sample_pdf])
    else:
        response = model.generate_content([prompt])
    
    return response.text
