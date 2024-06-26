class Error(Exception):
    pass


# class ClientError(Error):
#     def __init__(self, status_code, error_code, error_message, header, error_data=None):
#         # https status code
#         self.status_code = status_code
#         # error code returned from server
#         self.error_code = error_code
#         # error message returned from server
#         self.error_message = error_message
#         # the whole response header returned from server
#         self.header = header
#         # return data if it's returned from server
#         self.error_data = error_data
#
#
# class ServerError(Error):
#     def __init__(self, status_code, message):
#         self.status_code = status_code
#         self.message = message


class ResponseError(Error):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)


class ParameterRequiredError(Error):
    def __init__(self, params):
        self.params = params

    def __str__(self):
        return "%s is mandatory, but received empty." % (", ".join(self.params))


class ParameterValueError(Error):
    def __init__(self, msg=None, params=None):
        self.msg = msg
        self.params = params

    def __str__(self):
        if self.msg:
            text = self.msg
        else:
            text = "the enum value %s is invalid." % (", ".join(self.params))
        return text

# class ParameterTypeError(Error):
#     def __init__(self, params):
#         self.params = params
#
#     def __str__(self):
#         return f"{self.params[0]} data old_type has to be {self.params[1]}"
#
#
# class ParameterArgumentError(Error):
#     def __init__(self, error_message):
#         self.error_message = error_message
#
#     def __str__(self):
#         return self.error_message
