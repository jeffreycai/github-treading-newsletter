from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import requests
import base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

# Global variables
SERVICE_ACCOUNT_FILE = os.environ.get('SERVICE_ACCOUNT_FILE')
SUBJECT_EMAIL        = os.environ.get('SUBJECT_EMAIL') # the email address of the admin you want to impersonate
SUBJECT              = os.environ.get('SUBJECT')
FROM_EMAIL           = os.environ.get('FROM_EMAIL')
TO_EMAIL             = os.environ.get('TO_EMAIL')

TEMPLATE_FILE = 'email_template.html'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


def create_message(sender, to, subject, message_text_html):
    """Create a message for an email."""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text_html, 'html')
    message.attach(msg)

    raw_message = base64.urlsafe_b64encode(message.as_bytes())
    raw_message = raw_message.decode()
    body = {'raw': raw_message}

    return body

def send_message(service, user_id, message):
    """Send an email message."""
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as e:
        print('An error occurred: %s' % e)
        return None

def get_trending_repos():
    """Fetch trending repositories from GitHub."""
    url = "https://github.com/trending"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    trending_repos = []

    for repo in soup.find_all('article', class_="Box-row"):
        repo_name = repo.h2.get_text(strip=True)
        repo_url = "https://github.com" + repo.h2.a['href']
        repo_description = repo.p
        repo_stars = repo.find('div', class_='f6').find('a').get_text(strip=True)
        repo_stars_today = repo.find('span', class_='float-sm-right').get_text(strip=True)
        trending_repos.append((repo_name, repo_url, repo_description, repo_stars, repo_stars_today))

    return trending_repos

def main():
    # Load the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
        subject=SUBJECT_EMAIL)

    # Build the service
    service = build('gmail', 'v1', credentials=credentials)

    # Fetch trending repos
    trending_repos = get_trending_repos()

    # Prepare the email
    subject = os.environ.get('SUBJECT')
    row_template = """
    <tr>
        <td><b><a href="{repo_url}">{repo_name}</a></b></td>
        <td>{repo_description}</td>
        <td>{repo_stars_today}</td>
        <td>{repo_stars}</td>
    </tr>
    """
    table_rows = ""

    for repo_name, repo_url, repo_description, repo_stars, repo_stars_today in trending_repos:
        table_rows += row_template.format(
            repo_url=repo_url,
            repo_name=repo_name,
            repo_description=repo_description,
            repo_stars=repo_stars,
            repo_stars_today=repo_stars_today)

    with open(TEMPLATE_FILE, 'r') as file:
        body = file.read().replace('{row_template}', table_rows)

    # Create the email message
    message = create_message(FROM_EMAIL, TO_EMAIL, subject, body)

    # Send the email
    send_message(service, 'me', message)

if __name__ == '__main__':
    main()
