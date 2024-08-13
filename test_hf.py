import os
from datetime import datetime
from huggingface_hub import HfApi, create_repo, upload_file

# Prompt the user for Hugging Face Token and Base Repository Name
hf_token = input("Please enter your Hugging Face token: ")
base_repo_name = input("Please enter the base repository name (e.g., 'username/repo_name'): ")

# Generate a unique repository name by adding the current date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
hf_repo_name = f"{base_repo_name}_{timestamp}"

def test_huggingface_connection(hf_repo_name, hf_token):
    try:
        # Initialize the Hugging Face API
        api = HfApi()

        # Create a repository with the unique name (if it does not already exist)
        try:
            repo_url = create_repo(repo_id=hf_repo_name, token=hf_token, private=True)
            print(f"Repository {hf_repo_name} created successfully at {repo_url}.")
        except Exception as e:
            print(f"Repository creation failed or already exists: {e}")

        # Create a test file with a unique name using the current date and time
        local_dir = './test_repo'
        os.makedirs(local_dir, exist_ok=True)
        test_file_name = f"test_{timestamp}.txt"
        test_file_path = os.path.join(local_dir, test_file_name)
        with open(test_file_path, "w") as f:
            f.write("This is a test file to check the Hugging Face connection.")

        # Upload the test file to the repository
        upload_file(
            path_or_fileobj=test_file_path,
            path_in_repo=test_file_name,
            repo_id=hf_repo_name,
            token=hf_token,
        )

        print(f"Successfully connected to Hugging Face and uploaded {test_file_name} to {hf_repo_name}.")
    except Exception as e:
        print(f"Failed to connect to Hugging Face: {e}")

# Test the Hugging Face connection
test_huggingface_connection(hf_repo_name, hf_token)
