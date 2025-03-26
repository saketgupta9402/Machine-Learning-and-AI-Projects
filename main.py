import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure the Gemini API with the secret API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    raise ValueError("API key not found. Please set GEMINI_API_KEY in your environment variables.")

def load_csv(file_path):
    """Loads the CSV file from the given path and returns it as a DataFrame."""
    try:
        data = pd.read_csv(file_path)
        print("CSV file loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def format_csv_for_prompt(data, max_rows=70):
    """
    Converts a portion of the CSV data to a string format suitable for the prompt.
    Limits the number of rows included to avoid overloading the prompt.
    """
    csv_sample = data.head(max_rows).to_string(index=False)
    summary = f"The CSV file has {data.shape[0]} rows and {data.shape[1]} columns.\n"
    summary += "Here are some sample rows from the CSV data:\n"
    summary += csv_sample + "\n\n"  # Add CSV data sample to the context
    return summary

def ask_csv_question(data, question):
    """
    Takes the CSV data and a question, then generates an AI response.
    The response is based on the content in the CSV data.
    """
    # Prepare the CSV context
    context = format_csv_for_prompt(data)
    prompt = f"CSV Data:\n{context}\n\nQuestion: {question}"

    # Generate response with Gemini API
    try:
        response = model.generate_content(prompt)
        print("Answer:")
        print(response.text)

    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't process the question."

def main():
    """
    Main function to interact with the user.
    Prompts for a CSV file path, loads the CSV, and allows for interactive Q&A.
    """
    # Load CSV file
    csv_file = input("Enter the path to your CSV file: ")
    data = load_csv(csv_file)

    if data is not None:
        print("\nYou can now ask questions about the CSV data.")
        while True:
            question = input("Ask a question (or type 'exit' to quit): ")
            if question.lower() == 'exit':
                print("Goodbye!")
                break
            ask_csv_question(data, question)

# # Run the script
if __name__ == "__main__":
    main()