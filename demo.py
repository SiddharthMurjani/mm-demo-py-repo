import requests


def get_total_files(repo_url):
    # Extract the owner and repository name from the URL
    url_parts = repo_url.split("/")
    owner = url_parts[-2]
    repo_name = url_parts[-1].split(".")[0]  # Remove .git if present

    # Construct the GitHub API URL
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}"

    # Send a GET request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        repo_data = response.json()
        total_files = repo_data["size"]  # "size" attribute represents the total number of files
        return total_files
    else:
        print("Error:", response.status_code)
        return None


# Replace with your GitHub repository URL
repo_url = "https://github.com/SiddharthMurjani/On-ramp-2023"

total_files = get_total_files(repo_url)
if total_files is not None:
    print(f"Total files in the repository: {total_files}")
