class GithubApiException(Exception):
    """Exception raised when Github API returns unsuccessful response

    Attributes:
        responseCode -- response code from Github API

    """
    def __init__(self , responseCode):
        self.responseCode = responseCode