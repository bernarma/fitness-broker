class ANTException(Exception):
    pass


class DriverError(ANTException):
    pass


class MessageError(ANTException):
    def __init__(self, msg, internal=''):
        Exception.__init__(self, msg)
        self.internal = internal


class NodeError(ANTException):
    pass


class ChannelError(ANTException):
    pass