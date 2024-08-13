**Hugging Face Repository Test Script**

**Overview**

This script is designed to:

- Test the connection to Hugging Face by creating a repository.
- Upload a test file to the created repository.

Unique repository and file names are generated using the current date and time to avoid conflicts with existing repositories or files.

**Features**

- **Dynamic Repository Creation**: Prompts for a base repository name and appends the current date and time to ensure uniqueness.
- **Test File Upload**: Generates and uploads a simple text file with a timestamped name to the created repository.
- **Error Handling**: Manages scenarios where repository creation fails, such as if the repository already exists.

**Usage**

**Prerequisites**

- Python 3.x
- The `huggingface_hub` package

Install the required package using pip:

```
pip install huggingface_hub
```

**Running the Script**

1. **Clone the Repository**:

```
git clone https://github.com/DigitEgal/HF_Connection-Test/
cd HF_Connection-Test
```

2. **Run the Script**:

```
python test_hf.py
```

- Enter your Hugging Face token.
- Enter a base repository name (e.g., `yourusername/test_repo`).

3. **Check the Output**:

The script creates a new repository on Hugging Face with a name that includes the current date and time. A test file is also uploaded to this repository.

**Example Output**

```
Please enter your Hugging Face token: [your_token]
Please enter your repository name (e.g., 'username/repo_name'): yourusername/test_repo
Repository yourusername/test_repo_20240813_154530 created successfully at https://huggingface.co/yourusername/test_repo_20240813_154530.
Successfully connected to Hugging Face and uploaded test_20240813_154530.txt to yourusername/test_repo_20240813_154530.
```

**Customization**

- **Repository Name**: Modify `base_repo_name` to change the default repository name.
- **Test File Content**: Adjust the `f.write()` line in the script to change the content of the test file.

**Known Issues**

- **Repository Name Conflicts**: The script is designed to avoid conflicts by appending a timestamp, but running the script multiple times within the same second might cause a conflict.

**License**

This project is free to use for everybody.

**Contributing**

Contributions are welcome! For suggestions or improvements, please create a pull request or open an issue.
