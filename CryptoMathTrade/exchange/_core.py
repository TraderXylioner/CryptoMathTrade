class Core:
    def __init__(self,
                 proxies=None,
                 headers=None,
                 cookies=None,
                 auth=None,
                 ):
        self.proxies = proxies
        self.headers = headers
        self.cookies = cookies
        self.auth = auth

    def return_args(self, **kwargs):
        if self.proxies:
            kwargs['proxies'] = self.proxies
        if self.headers:
            kwargs['headers'] = self.headers
        if self.cookies:
            kwargs['cookies'] = self.cookies
        if self.auth:
            kwargs['auth'] = self.auth
        return kwargs
