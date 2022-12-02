import praw
from Variables import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD


class AuthorizationProvider:
    @staticmethod
    def reddit_authorization():
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
            username=USERNAME,
            password=PASSWORD
        )
        return reddit
