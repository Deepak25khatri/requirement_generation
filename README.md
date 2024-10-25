
# Requirements Generation Project

This project leverages multiple language models to analyze and generate requirements.

## Setup Instructions

### Step 1: Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Follow these steps to create and activate a virtual environment named `myenv`.

```bash
python -m venv myenv
```

**For Windows:**
```bash
myenv\Scripts\activate
```

**For macOS/Linux:**
```bash
source myenv/bin/activate
```

### Step 2: Create a `.env` File

Create a `.env` file in the root directory of the project and add the following line with your API key:

```plaintext
.env:
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

Replace `"YOUR_OPENAI_API_KEY"` with your actual API key.

### Step 3: Install Dependencies

Run the following command to install all required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Project

Once all dependencies are installed, run the main script using:

```bash
python main.py
```

## Project Structure

- `requirements.txt` - Contains the list of required dependencies.
- `main.py` - The main script to run the project.
- `.env` - Environment variables including API keys (not included in version control for security).

## Note

- Ensure you have your API keys ready and set them up in the `.env` file.


