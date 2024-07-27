
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
- [Contributing](#contributing)
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
Create and activate a virtual environment:

bash
Copier le code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
Copier le code
pip install -r requirements.txt
Usage
Run the Flask application:

bash
Copier le code
python run.py
Open your web browser and navigate to:

arduino
Copier le code
http://127.0.0.1:5000/
Enter your prompt in the text area and click "Generate Response" to see the model's output.

Configuration
Configure your Hugging Face API URL and API key in the config.py file:

python
Copier le code
class Config:
    DEBUG = True
    HF_API_REPO = 'tiiuae/falcon-7b-instruct'
    HF_API_KEY = 'your-huggingface-api-key'
Replace 'your-model-name' and 'your-huggingface-api-key' with your actual Hugging Face model name and API key.

Running Tests
This project uses pytest for testing. Ensure all dependencies are installed and run the tests:

bash
Copier le code
pytest
Test Structure
Unit Tests: Located in tests/test_models.py to test the model integration.
Route Tests: Located in tests/test_routes.py to test the Flask routes.
Technologies Used
Flask
LangChain
Hugging Face
PyTest
HTML/CSS for frontend
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Create a new Pull Request.
License
This project is proprietary software and is licensed under a custom license. See the LICENSE file for details.

For any questions regarding licensing, please contact nouhaelabed.pro@gmail.com                                                                                                                                                                                                                                                                .