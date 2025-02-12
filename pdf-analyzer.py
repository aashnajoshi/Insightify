from collections import defaultdict
from dotenv import load_dotenv
import openai
import fitz  # PyMuPDF for reading PDF files
import os
import re

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_file_path):
    '''Extracts text from a given PDF file using PyMuPDF (fitz).'''
    
    try:
        document = fitz.open(pdf_file_path)
        text = ""
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text("text")
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def process_text(text):
    '''Cleans and preprocesses the extracted text (removes extra spaces, newlines, etc.).'''

    cleaned_text = re.sub(r'\s+', ' ', text)
    return cleaned_text

def analyze_text_with_gpt(text):
    '''Sends the extracted and processed text to GPT-3 for analysis and insight generation.'''

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Please analyze the following text and extract key insights such as future growth prospects, key changes in the business, and important triggers for next year's earnings and growth:\n\n{text}"}
            ],
            max_tokens=500,
            temperature=0.7)
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error analyzing text with GPT: {e}")
        return ""

def summarize_findings(text):
    '''Analyzes the extracted text and provides a summary of key findings using GPT-3.5-turbo.'''

    insights = analyze_text_with_gpt(text)
    findings = defaultdict(str)
    findings["Insights"] = insights
    return findings

def main():
    pdf_path = "SJS Transcript Call.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    
    if extracted_text:
        processed_text = process_text(extracted_text)
        summary = summarize_findings(processed_text)
        print("Summary of Key Findings:")
        for key, value in summary.items():
            print(f"{key}: {value}")
    else:
        print("No text extracted from the PDF.")

if __name__ == "__main__":
    main()