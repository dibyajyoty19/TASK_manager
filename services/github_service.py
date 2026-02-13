import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

class GitHubService:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")
        self.repo_name = os.getenv("GITHUB_REPO")

        print("GitHub token loaded:", bool(self.token))
        print("GitHub repo:", self.repo_name)

        if self.token and self.repo_name:
            self.client = Github(self.token)
            self.repo = self.client.get_repo(self.repo_name)
            print("GitHub repo object created")
        else:
            self.client = None
            self.repo = None

    def create_issue(self, title: str, description: str):
        if not self.repo:
            print("Repo not available, skipping issue creation")
            return None

        try:
            issue = self.repo.create_issue(
                title=title,
                body=description
            )
            print("Issue created with ID:", issue.id)
            return issue.id
        except Exception as e:
            print("GitHub error while creating issue:", e)
            return None
