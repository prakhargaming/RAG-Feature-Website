import requests
import os
import base64
from pathlib import Path

# GitHub credentials
GITHUB_USERNAME = "prakhargaming"
GITHUB_TOKEN = os.getenv("REPO")  # or set as a string directly

# Create output directory
OUTPUT_DIR = Path("github_repos_info")
OUTPUT_DIR.mkdir(exist_ok=True)

# GitHub API headers
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_repositories():
    all_repos = []
    page = 1

    while True:
        url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100&page={page}&type=all"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error fetching repos: {response.status_code} - {response.text}")
        
        repos = response.json()
        if not repos:
            break

        all_repos.extend(repos)
        page += 1

    return all_repos

def fetch_readme(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/readme"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json().get("content")
        if content:
            return base64.b64decode(content).decode("utf-8", errors="ignore")
    return "README not found or could not be fetched."

def save_repo_info(repo, readme_content):
    filename = OUTPUT_DIR / f"{repo['name'].replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Repository Name: {repo['name']}\n")
        f.write(f"Full Name: {repo['full_name']}\n")
        f.write(f"Description: {repo['description']}\n")
        f.write(f"Visibility: {'Private' if repo['private'] else 'Public'}\n")
        f.write(f"URL: {repo['html_url']}\n")
        f.write(f"Clone URL: {repo['clone_url']}\n")
        f.write(f"Stars: {repo['stargazers_count']}\n")
        f.write(f"Forks: {repo['forks_count']}\n")
        f.write(f"Watchers: {repo['watchers_count']}\n")
        f.write(f"Language: {repo['language']}\n")
        f.write(f"Topics: {', '.join(repo.get('topics', []))}\n")
        f.write(f"Created At: {repo['created_at']}\n")
        f.write(f"Updated At: {repo['updated_at']}\n\n")

        f.write("README:\n")
        f.write("-" * 80 + "\n")
        f.write(readme_content)

def main():
    print("Fetching repositories...")
    repos = fetch_repositories()
    print(f"Found {len(repos)} repositories.\n")

    for repo in repos:
        print(f"Processing {repo['name']}...")
        readme = fetch_readme(repo['name'])
        save_repo_info(repo, readme)

    print("\nAll repository info saved to folder 'github_repos_info'.")

if __name__ == "__main__":
    main()
