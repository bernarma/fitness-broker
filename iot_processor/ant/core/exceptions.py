class ANTException(Exception):
    pass


class DriverError(ANTException):
    pass


class MessageError(ANTException):
    def __init__(self, msg, internal=''):
        super().__init__(msg)
        self.internal = internal


class NodeError(ANTException):
    pass


class ChannelError(ANTException):
    pass