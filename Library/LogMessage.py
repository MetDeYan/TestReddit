# Used to generate messages
class LogMessage:
    @staticmethod
    def post_message(title):
        return 'Создан новый пост с заголовком "' + title + '!"'

    @staticmethod
    def delete_post_message(title):
        return 'Пост с заголовком "' + title + ' был удален!"'

    @staticmethod
    def comment_message(comment):
        return 'Добавлен новый комментарий: "' + comment + '!"'
