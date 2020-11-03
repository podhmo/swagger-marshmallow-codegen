from marshmallow import (
    Schema,
    fields,
)


class Commit(Schema):
    author = fields.Nested(lambda: CommitAuthor())
    commit = fields.Nested(lambda: CommitCommit())
    files = fields.List(fields.Nested(lambda: CommitFilesItem()))


class CommitFilesItem(Schema):
    additions = fields.Integer()
    blob_url = fields.String()
    changes = fields.Integer()
    deletions = fields.Integer()
    filename = fields.String()
    patch = fields.String()
    raw_url = fields.String()
    status = fields.String()


class CommitCommit(Schema):
    author = fields.Nested(lambda: CommitCommitAuthor())
    committer = fields.Nested(lambda: CommitCommitCommitter())
    message = fields.String()
    tree = fields.Nested(lambda: CommitCommitTree())
    url = fields.String()


class CommitCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class CommitCommitCommitter(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class CommitCommitAuthor(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class CommitAuthor(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()
