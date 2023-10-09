
import requests
import json
import os

def get_all_commits(owner, repo):
    base_url = "https://api.github.com"
    endpoint = f"/repos/{owner}/{repo}/commits"
    url = base_url + endpoint

    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    all_commits = []

    # Initialize page number and a variable to check if there are more pages
    page_number = 1
    has_more_pages = True

    while has_more_pages:
        # Send the request for the current page
        params = {
            "page": page_number,
            "per_page": 100  # Maximum number of commits per page is 100
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            commits = response.json()
            if len(commits) == 0:
                # No more commits, break the loop
                has_more_pages = False
            else:
                for commit in commits:
                    commit_info = {
                        "sha": commit['sha'],
                        "author": commit['commit']['author']['name'],
                        "date": commit['commit']['author']['date'],
                        "message": commit['commit']['message']
                    }
                    all_commits.append(commit_info)
                # Move to the next page
                page_number += 1
        else:
            print(f"Failed to retrieve Git log. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            break

    return all_commits

if __name__ == "__main__":
    owner = "tongtongwang86"  # Replace with the actual owner username
    repo = "tongtongincwebsite" 

    # Get all commits
    all_commits = get_all_commits(owner, repo)


    


    output_file = os.path.join(os.path.dirname(__file__), "git_log.json")

    # Write the commits to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(all_commits, json_file, indent=4)

    print(f"Git log saved to {output_file}")
