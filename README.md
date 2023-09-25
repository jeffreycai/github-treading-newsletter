# GitHub Trending Repositories Emailer

Stay updated with what's trending on GitHub every day with this Python script. It fetches the currently trending repositories and sends an email with the repository details, serving as a handy daily newsletter.

## Features

- Fetches trending repositories from GitHub.
- Sends an email with the repository names, URLs, descriptions, and stars count.

## Prerequisites

- Python 3.x
- Google Cloud Platform service account with Gmail API access
- BeautifulSoup for HTML parsing
- requests for making HTTP requests

## Installation & Usage

1. **Install Python Packages**

    Install the necessary Python packages using pip:

    ```bash
    pip install google-auth google-auth-transport-requests google-auth-oauthlib google-auth-httplib2 google-api-python-client beautifulsoup4 requests
    ```

2. **Setup Environment Variables**

    Copy `.env.template` file as `.env` file (`.env` is excluded for git, see [.gitignore](.gitignore))
    
    ```bash
    cp .env.template .env
    ```

    Update the environment variables in the file accordingly.

3. **Configure Google Cloud Platform Service Account**

    Ensure you have a Google Cloud Platform service account with the Gmail API enabled. Download the service account key file and save it in the same directory as the script. Name the key file `gcp-svc-acc-key.json` (it is excluded from Git so won't be committed)

    See [PREPARE_GOOGLE_ACCOUNT.md](PREPARE_GOOGLE_ACCOUNT.md) for details.

4. **Update Script Variables**

    Update the global variables in the script with your service account file path, the email address of the admin you want to impersonate, the sender email, and the recipient email.

5. **Run the Script**

    Execute the script:

    ```bash
    make run
    ```

## Caution

This script uses web scraping to fetch the trending repositories from GitHub. Please be aware that this is against GitHub's `robots.txt` rules and could result in your IP being blocked by GitHub. Always make sure to respect the website's terms of service and `robots.txt`.
