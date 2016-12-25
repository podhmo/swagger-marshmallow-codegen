from marshmallow.validate import(
    Length,
    Regexp
)
class X(Schema):
    team = fields.String(validate=[Regexp(regex='team[1-9][0-9]+')])
    team2 = fields.String(validate=[Length(min=None, max=10), Regexp(regex='team[1-9][0-9]+')])
