from marshmallow import (
    Schema,
    fields,
)


class Message(Schema):
    message = fields.String(required=True)


class MessageInput:
    class Get:
        """
        Get a message of the day
        """

        class Path(Schema):
            name = fields.String(description='name to include in the message')




class MessageOutput:
    class Get200(Message):
        """Successful response"""
        pass
