# Insightify
Insightify is a PDF analysis tool that leverages OpenAI's API to extract and summarize key insights from PDF documents. It helps users to easily analyze company reports and financial documents by summarizing critical information like future growth prospects, key business changes, and factors influencing next year’s earnings.

## Features
- Extracts text from PDF files using the `fitz` library (PyMuPDF).
- Uses OpenAI to analyze and summarize key insights from the extracted text.
- Identifies key elements such as:
  - Future growth prospects
  - Key business changes
  - Triggers for growth or decline
  - Material impacts on future earnings and growth
  
## Usage:
### Basic setup and dependency management:
1. Install `pipenv` if you don't have it:
   ```bash
   pip install pipenv
   ```

2. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

3. Install required libraries from the `Pipfile`:
   ```bash
   pipenv install
   ```

4. Ensure that the `.env` file contains your OpenAI API key.

### To run the code:
1. Make sure the environment is activated (step 2).
   
2. Run the script:
   ```bash
   python pdf-analyzer.py
   ```

3. Optional: For Streamlit-based app:
    ```bash
    streamlit run app.py
    ```

4. The script will extract text from the specified PDF and send it to OpenAI for analysis. It will output the key findings from the document.

## Description about various files:
- **.env**: Contains environment variables (e.g., OpenAI API key).
- **app.py**: Streamlit based version of the app.
- **pdf-analyzer.py**: Main Python script to run the PDF analysis.
- **Pipfile**: Specifies the dependencies for the project.
- **Pipfile.lock**: Ensures consistent dependency versions.
- **Sample PDF.pdf**: A sample file for testing the summarization.