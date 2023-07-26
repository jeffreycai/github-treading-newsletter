# GitHub Trending Repositories Emailer

This Python script fetches the currently trending repositories from GitHub and sends an email with the repository details. It is a handy script that keeps you updated with what is hot on Github every day, like a newsletter.

## Features

- Fetches trending repositories from GitHub.
- Sends an email with the names, URLs, descriptions, and stars today of the trending repositories.

## Requirements

- Python 3.x
- Google Cloud Platform service account with Gmail API access
- BeautifulSoup for HTML parsing
- requests for making HTTP requests

## Usage

1. Install the necessary Python packages using pip:

    ```bash
    pip install google-auth google-auth-transport-requests google-auth-oauthlib google-auth-httplib2 google-api-python-client beautifulsoup4 requests
    ```

2. Copy `.env.template` file as `.env` file (`.env` is excluded for git, see [.gitignore](.gitignore))
    
    ```
    cp .env.template .env
    ```

    Update the env vars in the file accordingly.

3. Make sure you have a Google Cloud Platform service account with the Gmail API enabled. Download the service account key file and save it in the same directory as the script. Name the key file `gcp-svc-acc-key.json` (it is excluded from Git so won't be committed)

    See [PREPARE_GOOGLE_ACCOUNT.md](PREPARE_GOOGLE_ACCOUNT.md) for details.

4. Update the global variables in the script with your service account file path, the email address of the admin you want to impersonate, the sender email, and the recipient email.

5. Run the script:

    ```
    bash
    python script_name.py
    ```

    Replace `script_name.py` with the actual name of the script.

## Notes

This script uses web scraping to fetch the trending repositories from GitHub. Please be aware that this is against GitHub's `robots.txt` rules and could result in your IP being blocked by GitHub. Always make sure to respect the website's terms of service and `robots.txt`.
