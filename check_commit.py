import requests
import json
import os
import sys

# Replace with your GitHub repository details
REPO_NAME = "rajivsharma92/ci-cd-project"  # Update with your GitHub username and repository name
BRANCH_NAME = sys.argv[1] if len(sys.argv) > 1 else "main"  # Default to 'main' if no branch specified
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_NAME}/commits?sha={BRANCH_NAME}"
LAST_COMMIT_FILE = "/home/rajiv/htmlcicd/last_commit.txt"  # Store the last commit hash

def get_latest_commit():
    response = requests.get(GITHUB_API_URL)
    if response.status_code == 200:
        commits = json.loads(response.text)
        if commits:  # Check if there are any commits
            latest_commit = commits[0]['sha']
            return latest_commit
        else:
            print("No commits found on this branch.")
            return None
    else:
        print(f"Error fetching commits: {response.status_code} - {response.text}")
        return None

def save_last_commit(commit_hash):
    with open(LAST_COMMIT_FILE, "w") as file:
        file.write(commit_hash)

def read_last_commit():
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, "r") as file:
            return file.read().strip()
    return None

def main():
    latest_commit = get_latest_commit()
    if not latest_commit:
        print("Error retrieving latest commit.")
        return

    last_commit = read_last_commit()
    if last_commit != latest_commit:
        print("New commit found! Deploying...")
        save_last_commit(latest_commit)
        os.system("/home/rajiv/htmlcicd/deploy.sh")  # Trigger deployment script
    else:
        print("No new commit.")

if __name__ == "__main__":
    main()
