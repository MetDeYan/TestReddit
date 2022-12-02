# Used to create community, create and delete post, add comment, checks
from AuthorizationProvider import AuthorizationProvider
from Title import TitleGeneration
from Variables import TITLE, COMMUNITY, POST_TEXT, COMMENT_TEXT


class RedditPostLibrary:
    reddit = AuthorizationProvider.reddit_authorization()

    @classmethod
    def create_community(cls):
        cls.reddit.subreddit.create(COMMUNITY, selfstr='public')

    @classmethod
    def create_post(cls):
        title = TitleGeneration.title_generation(TITLE)
        post_id = cls.reddit.subreddit(COMMUNITY).submit(title, selftext=POST_TEXT)
        return str(post_id), title

    @classmethod
    def create_comment(cls, post_id):
        cls.reddit.submission(id=post_id).reply(COMMENT_TEXT)

    @classmethod
    def delete_post(cls, post_id):
        cls.reddit.submission(post_id).delete()

    @classmethod
    def post_availability_check(cls, post_id):
        for post in cls.reddit.subreddit(COMMUNITY).stream.submissions(pause_after=-1):
            if not post:
                return False
            if post == post_id:
                return True
