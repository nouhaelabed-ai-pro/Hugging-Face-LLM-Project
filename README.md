
# Hugging Face LLM Project

This project integrates Hugging Face language models with LangChain using a Flask web application. It provides a simple web interface where users can input prompts and receive generated responses from the language model.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

- Integration with Hugging Face language models using LangChain.
- Flask-based web application with a simple and user-friendly interface.
- Real-time response generation for user prompts.
- TDD approach with comprehensive testing.

## Demo

Here's a quick demo of the application in action:

### Generate Response

![Generate Response](assets/generate-response-demo.gif)

> **Note**: The demo above shows how easy it is to interact with the language model through our web interface. Simply input your prompt and click "Generate Response" to see the output from the Hugging Face model.

## Installation

### Prerequisites

- Python 3.11+
- Pip (Python package installer)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nouhaelabed-ai-pro/LLM-Hugging-Face-Project.git
   cd YOUR_REPOSITORY
   
2. **Create and activate a virtual environment:**

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   
3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
   
## Usage

1. **Run the Flask application:**

    ```bash
    python run.py

2. **Open your web browser and navigate to:**

    http://127.0.0.1:5000/

3. Enter your prompt in the text area and click "Generate Response" to see the model's output.

## Configuration

**Configure your Hugging Face API URL and API key in the config.py file:**

    class Config:
        DEBUG = True
        HF_API_REPO = 'your-model-name'
        HF_API_KEY = 'your-huggingface-api-key'

Replace 'your-model-name' and 'your-huggingface-api-key' with your actual Hugging Face model name and API key.


## Running Tests
This project uses pytest for testing. Ensure all dependencies are installed and run the tests:

    pytest

### Test Structure
1. **Unit Tests:** 
    Located in tests/test_models.py to test the model integration. 

2. **Route Tests:**
    Located in tests/test_routes.py to test the Flask routes.

## Technologies Used

- #### Flask
- #### LangChain
- #### Hugging Face
- #### PyTest
- #### HTML/CSS for frontend


## License
This project is proprietary software. See the LICENSE file for details.
