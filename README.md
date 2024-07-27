
# Hugging Face LLM Project

This project integrates Hugging Face language models with LangChain using a Flask web application. It provides a simple web interface where users can input prompts and receive generated responses from the language model.

## Table of Contents

- [Features](#features)
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

## Installation

### Prerequisites

- Python 3.11+
- Pip (Python package installer)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python run.py
   ```

2. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Enter your prompt in the text area and click "Generate Response" to see the model's output.**

## Configuration

Configure your Hugging Face API URL and API key in the `config.py` file:

```python
class Config:
    DEBUG = True
    HF_API_REPO = 'tiiuae/falcon-7b-instruct'
    HF_API_KEY = 'your-huggingface-api-key'
```

Replace `'your-model-name'` and `'your-huggingface-api-key'` with your actual Hugging Face model name and API key.

## Running Tests

This project uses `pytest` for testing. Ensure all dependencies are installed and run the tests:

```bash
pytest
```

### Test Structure

- **Unit Tests:** Located in `tests/test_models.py` to test the model integration.
- **Route Tests:** Located in `tests/test_routes.py` to test the Flask routes.

## Technologies Used

- Flask
- LangChain
- Hugging Face
- PyTest
- HTML/CSS for frontend

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your actual GitHub username and repository name. Save this content in a file named `README.md` in the root of your project directory.