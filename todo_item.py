import datetime

class TodoItem:
    """
        Parameters:
        ----------
        title: str
        deadline: datetime object
        is_done: bool

        Raises:
        ----------
        ValueError: when title type isn't str
        ValueError: when deadline type isn't datetime object
    """

    def __init__(self, title, deadline):

        self.title = title
        self.deadline = deadline
        self.is_done = False

        if not isinstance(title, str):
            raise ValueError('Title should be a string type')

        if not isinstance(deadline, datetime.date):
            raise ValueError('Deadline should be a datetime object format')


    def mark(self):

        self.is_done = True


    def unmark(self):

        self.is_done = False


    def __str__(self):

        execution = ' '
        if self.is_done:
            execution = 'x'

        output = '[{}] {} {}'.format(execution, str(self.deadline.day) + '-' + str(self.deadline.month), self.title)

        return output

