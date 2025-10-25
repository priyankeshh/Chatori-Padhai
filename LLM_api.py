import time
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and configuration from environment variables
API_KEY = os.getenv("GEMINI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.0-flash")
SITE_URL = os.getenv("SITE_URL", "http://localhost:8501")
SITE_NAME = os.getenv("SITE_NAME", "Evihian")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")

# Configure the Gemini API
genai.configure(api_key=API_KEY)

# Create the model
model = genai.GenerativeModel(LLM_MODEL)

def send_request(prompt):
    """Send a single request to the Gemini API and return the result."""
    print(f"Sending request to Gemini...")
    start_time = time.time()

    try:
        # Generate content using Gemini
        response = model.generate_content(prompt)

        end_time = time.time()
        elapsed_time = end_time - start_time

        content = response.text
        print(f"Response: {content[:100]}...")
        print(f"Generation time: {elapsed_time:.2f} seconds")

        return content

    except Exception as e:
        print(f"Error generating content: {e}")
        return f"I apologize, but I encountered an error: {str(e)}. Please try again."

def call_gemini(prompt):
    """Call the Gemini API with a prompt and return the response."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try again."

def main():
    prompt = "What is the meaning of life?"

    print("Starting Gemini API test...")
    overall_start_time = time.time()

    response = send_request(prompt)

    overall_end_time = time.time()
    overall_elapsed_time = overall_end_time - overall_start_time

    print(f"\n===== SUMMARY =====")
    print(f"Total execution time: {overall_elapsed_time:.2f} seconds")
    print(f"Model used: {LLM_MODEL}")

if __name__ == "__main__":
    main()
