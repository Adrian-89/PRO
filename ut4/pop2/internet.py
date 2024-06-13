class Website:
    def __init__(self, url: str, header: str, footer: str, main: str):
        self.current_url = url
        self.header = header
        self.footer = footer
        self.main = main
        self.links = {}

    @staticmethod
    def is_valid_link(method):
        def wrapper(self, *args, **kwargs):
            # Vamos a suponer que element_id
            # es el primer parámetro nominal
            element_id = kwargs['element_id']
            if element_id in self.links:
                return method(self, *args, **kwargs)
            raise WebsiteError(self.current_url, 'Invalid link id')

        return wrapper

    def add_link(self, url: str, element_id: str) -> None:
        self.links[element_id] = url

    @is_valid_link
    def click_link(self, element_id: str):
        self.current_url = self.links[element_id]


class WebsiteError(Exception):
    BASE_MSG = 'Website Error'

    def __init__(self, url: str, msg: str = ''):
        if msg:
            self.msg = f'{WebsiteError.BASE_MSG}: {msg}'
        else:
            self.msg = WebsiteError.BASE_MSG
        super().__init__(msg)
        self.url = url

    def __str__(self):
        return f'{self.msg} at {self.url}'
