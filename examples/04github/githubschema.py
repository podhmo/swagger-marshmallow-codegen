# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)
from marshmallow.validate import (
    Length,
    OneOf
)
from swagger_marshmallow_codegen.schema import (
    PrimitiveValueSchema
)


class Asset(Schema):
    content_type = fields.String()
    created_at = fields.String()
    download_count = fields.Number()
    id = fields.Number()
    label = fields.String()
    name = fields.String()
    size = fields.Number()
    state = fields.String()
    updated_at = fields.String()
    uploader = fields.Nested('AssetUploader')
    url = fields.String()


class AssetUploader(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Number()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class AssetPatch(Schema):
    label = fields.String()
    name = fields.String(required=True)


class AssetsItem(Schema):
    content_type = fields.String()
    created_at = fields.String()
    download_count = fields.Number()
    id = fields.Number()
    label = fields.String()
    name = fields.String()
    size = fields.Number()
    state = fields.String()
    updated_at = fields.String()
    uploader = fields.Nested('AssetsItemUploader')
    url = fields.String()


class AssetsItemUploader(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Number()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class AssigneesItem(Schema):
    avatar_url = fields.Integer()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Blob(Schema):
    content = fields.String()
    encoding = fields.String(validate=[OneOf(choices=['utf-8', 'base64'], labels=[])])
    sha = fields.String()
    size = fields.Integer()


class Blobs(Schema):
    sha = fields.String()


class Branch(Schema):
    _links = fields.Nested('Branch_links')
    commit = fields.Nested('BranchCommit')
    name = fields.String()


class BranchCommit(Schema):
    author = fields.Nested('BranchCommitAuthor')
    commit = fields.Nested('BranchCommitCommit')
    committer = fields.Nested('BranchCommitCommitter')
    parents = fields.List(fields.Nested('BranchCommitParentsItem', ))
    sha = fields.String()
    url = fields.String()


class BranchCommitParentsItem(Schema):
    sha = fields.String()
    url = fields.String()


class BranchCommitCommitter(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class BranchCommitCommit(Schema):
    author = fields.Nested('BranchCommitCommitAuthor')
    committer = fields.Nested('BranchCommitCommitCommitter')
    message = fields.String()
    tree = fields.Nested('BranchCommitCommitTree')
    url = fields.String()


class BranchCommitCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class BranchCommitCommitCommitter(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class BranchCommitCommitAuthor(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class BranchCommitAuthor(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Branch_links(Schema):
    html = fields.String()
    self = fields.String()


class BranchesItem(Schema):
    commit = fields.Nested('BranchesItemCommit')
    name = fields.String()


class BranchesItemCommit(Schema):
    sha = fields.String()
    url = fields.String()


class CollaboratorsItem(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Comment(Schema):
    body = fields.String()


class CommentBody(Schema):
    body = fields.String(required=True)


class CommentsItem(Schema):
    body = fields.String()
    created_at = fields.String(description='ISO 8601.')
    id = fields.Integer()
    url = fields.String()
    user = fields.Nested('CommentsItemUser')


class CommentsItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Commit(Schema):
    author = fields.Nested('CommitAuthor')
    commit = fields.Nested('CommitCommit')
    committer = fields.Nested('CommitCommitter')
    files = fields.List(fields.Nested('CommitFilesItem', ))
    parents = fields.List(fields.Nested('CommitParentsItem', ))
    sha = fields.String()
    stats = fields.Nested('CommitStats')
    url = fields.String()


class CommitStats(Schema):
    additions = fields.Integer()
    deletions = fields.Integer()
    total = fields.Integer()


class CommitParentsItem(Schema):
    sha = fields.String()
    url = fields.String()


class CommitFilesItem(Schema):
    additions = fields.Integer()
    blob_url = fields.String()
    changes = fields.Integer()
    deletions = fields.Integer()
    filename = fields.String()
    patch = fields.String()
    raw_url = fields.String()
    status = fields.String()


class CommitCommitter(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class CommitCommit(Schema):
    author = fields.Nested('CommitCommitAuthor')
    committer = fields.Nested('CommitCommitCommitter')
    message = fields.String()
    tree = fields.Nested('CommitCommitTree')
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


class CommitActivityStatsItem(Schema):
    days = fields.List(fields.Integer())
    total = fields.Integer()
    week = fields.Integer()


class CommitBody(Schema):
    body = fields.String(required=True)
    line = fields.String(description='Deprecated - Use position parameter instead.')
    number = fields.String(description='Line number in the file to comment on. Defaults to null.')
    path = fields.String(description='Relative path of the file to comment on.')
    position = fields.Integer(description='Line index in the diff to comment on.')
    sha = fields.String(required=True, description='SHA of the commit to comment on.')


class CommitComments(Schema):
    body = fields.String()
    commit_id = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    html_url = fields.String()
    id = fields.Integer()
    line = fields.Integer()
    path = fields.String()
    position = fields.Integer()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('CommitCommentsUser')


class CommitCommentsUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class CommitsItem(Schema):
    author = fields.Nested('CommitsItemAuthor')
    commit = fields.Nested('CommitsItemCommit')
    committer = fields.Nested('CommitsItemCommitter')
    parents = fields.List(fields.Nested('CommitsItemParentsItem', ))
    sha = fields.String()
    url = fields.String()


class CommitsItemParentsItem(Schema):
    sha = fields.String()
    url = fields.String()


class CommitsItemCommitter(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class CommitsItemCommit(Schema):
    author = fields.Nested('CommitsItemCommitAuthor')
    committer = fields.Nested('CommitsItemCommitCommitter')
    message = fields.String()
    tree = fields.Nested('CommitsItemCommitTree')
    url = fields.String()


class CommitsItemCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class CommitsItemCommitCommitter(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class CommitsItemCommitAuthor(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class CommitsItemAuthor(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Compare_commits(Schema):
    ahead_by = fields.Integer()
    base_commit = fields.Nested('Compare_commitsBase_commit')
    behind_by = fields.Integer()
    commits = fields.List(fields.Nested('Compare_commitsCommitsItem', ))
    diff_url = fields.String()
    files = fields.List(fields.Nested('Compare_commitsFilesItem', ))
    html_url = fields.String()
    patch_url = fields.String()
    permalink_url = fields.String()
    status = fields.String()
    total_commits = fields.Integer()
    url = fields.String()


class Compare_commitsFilesItem(Schema):
    additions = fields.Integer()
    blob_url = fields.String()
    changes = fields.Integer()
    contents_url = fields.String()
    deletions = fields.Integer()
    filename = fields.String()
    patch = fields.String()
    raw_url = fields.String()
    sha = fields.String()
    status = fields.String()


class Compare_commitsCommitsItem(Schema):
    author = fields.Nested('Compare_commitsCommitsItemAuthor')
    commit = fields.Nested('Compare_commitsCommitsItemCommit')
    committer = fields.Nested('Compare_commitsCommitsItemCommitter')
    parents = fields.List(fields.Nested('Compare_commitsCommitsItemParentsItem', ))
    sha = fields.String()
    url = fields.String()


class Compare_commitsCommitsItemParentsItem(Schema):
    sha = fields.String()
    url = fields.String()


class Compare_commitsCommitsItemCommitter(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Compare_commitsCommitsItemCommit(Schema):
    author = fields.Nested('Compare_commitsCommitsItemCommitAuthor')
    committer = fields.Nested('Compare_commitsCommitsItemCommitCommitter')
    message = fields.String()
    tree = fields.Nested('Compare_commitsCommitsItemCommitTree')
    url = fields.String()


class Compare_commitsCommitsItemCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class Compare_commitsCommitsItemCommitCommitter(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class Compare_commitsCommitsItemCommitAuthor(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class Compare_commitsCommitsItemAuthor(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Compare_commitsBase_commit(Schema):
    author = fields.Nested('Compare_commitsBase_commitAuthor')
    commit = fields.Nested('Compare_commitsBase_commitCommit')
    committer = fields.Nested('Compare_commitsBase_commitCommitter')
    parents = fields.List(fields.Nested('Compare_commitsBase_commitParentsItem', ))
    sha = fields.String()
    url = fields.String()


class Compare_commitsBase_commitParentsItem(Schema):
    sha = fields.String()
    url = fields.String()


class Compare_commitsBase_commitCommitter(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Compare_commitsBase_commitCommit(Schema):
    author = fields.Nested('Compare_commitsBase_commitCommitAuthor')
    committer = fields.Nested('Compare_commitsBase_commitCommitCommitter')
    message = fields.String()
    tree = fields.Nested('Compare_commitsBase_commitCommitTree')
    url = fields.String()


class Compare_commitsBase_commitCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class Compare_commitsBase_commitCommitCommitter(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class Compare_commitsBase_commitCommitAuthor(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class Compare_commitsBase_commitAuthor(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Contents_path(Schema):
    _links = fields.Nested('Contents_path_links')
    content = fields.String()
    encoding = fields.String()
    git_url = fields.String()
    html_url = fields.String()
    name = fields.String()
    path = fields.String()
    sha = fields.String()
    size = fields.Integer()
    type = fields.String()
    url = fields.String()


class Contents_path_links(Schema):
    git = fields.String()
    html = fields.String()
    self = fields.String()


class ContributorsItem(Schema):
    avatar_url = fields.String()
    contributions = fields.Integer()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class ContributorsStatsItem(Schema):
    author = fields.Nested('ContributorsStatsItemAuthor')
    total = fields.Integer(description='The Total number of commits authored by the contributor.')
    weeks = fields.List(fields.Nested('ContributorsStatsItemWeeksItem', ))


class ContributorsStatsItemWeeksItem(Schema):
    a = fields.Integer(description='Number of additions.')
    c = fields.Integer(description='Number of commits.')
    d = fields.Integer(description='Number of deletions.')
    w = fields.String(description='Start of the week.')


class ContributorsStatsItemAuthor(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class CreateDownload(Schema):
    accesskeyid = fields.String()
    acl = fields.String()
    bucket = fields.String()
    content_type = fields.String()
    description = fields.String()
    download_count = fields.Integer()
    expirationdate = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    html_url = fields.String()
    id = fields.Integer()
    mime_type = fields.String()
    name = fields.String()
    path = fields.String()
    policy = fields.String()
    prefix = fields.String()
    redirect = fields.Boolean()
    s3_url = fields.String()
    signature = fields.String()
    size = fields.Integer()
    url = fields.String()


class CreateFile(Schema):
    commit = fields.Nested('CreateFileCommit')
    content = fields.Nested('CreateFileContent')


class CreateFileContent(Schema):
    _links = fields.Nested('CreateFileContent_links')
    git_url = fields.String()
    html_url = fields.String()
    name = fields.String()
    path = fields.String()
    sha = fields.String()
    size = fields.Integer()
    type = fields.String()
    url = fields.String()


class CreateFileContent_links(Schema):
    git = fields.String()
    html = fields.String()
    self = fields.String()


class CreateFileCommit(Schema):
    author = fields.Nested('CreateFileCommitAuthor')
    committer = fields.Nested('CreateFileCommitCommitter')
    html_url = fields.String()
    message = fields.String()
    parents = fields.List(fields.Nested('CreateFileCommitParentsItem', ))
    sha = fields.String()
    tree = fields.Nested('CreateFileCommitTree')
    url = fields.String()


class CreateFileCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class CreateFileCommitParentsItem(Schema):
    html_url = fields.String()
    sha = fields.String()
    url = fields.String()


class CreateFileCommitCommitter(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class CreateFileCommitAuthor(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class CreateFileBody(Schema):
    committer = fields.Nested('CreateFileBodyCommitter')
    content = fields.String()
    message = fields.String()


class CreateFileBodyCommitter(Schema):
    email = fields.String()
    name = fields.String()


class DeleteFile(Schema):
    commit = fields.Nested('DeleteFileCommit')
    content = fields.String()


class DeleteFileCommit(Schema):
    author = fields.Nested('DeleteFileCommitAuthor')
    committer = fields.Nested('DeleteFileCommitCommitter')
    html_url = fields.String()
    message = fields.String()
    parents = fields.Nested('DeleteFileCommitParents')
    sha = fields.String()
    tree = fields.Nested('DeleteFileCommitTree')
    url = fields.String()


class DeleteFileCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class DeleteFileCommitParents(Schema):
    html_url = fields.String()
    sha = fields.String()
    url = fields.String()


class DeleteFileCommitCommitter(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class DeleteFileCommitAuthor(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class DeleteFileBody(Schema):
    committer = fields.Nested('DeleteFileBodyCommitter')
    message = fields.String()
    sha = fields.String()


class DeleteFileBodyCommitter(Schema):
    email = fields.String()
    name = fields.String()


class Deployment(Schema):
    description = fields.String()
    payload = fields.Nested('DeploymentPayload')
    ref = fields.String()


class DeploymentPayload(Schema):
    deploy_user = fields.String()
    environment = fields.String()
    room_id = fields.Number()


class Deployment_resp(Schema):
    created_at = fields.String()
    creator = fields.Nested('Deployment_respCreator')
    description = fields.String()
    id = fields.Integer()
    payload = fields.String()
    sha = fields.String()
    statuses_url = fields.String()
    updated_at = fields.String()
    url = fields.String()


class Deployment_respCreator(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Deployment_statusesItem(Schema):
    created_at = fields.String()
    creator = fields.Nested('Deployment_statusesItemCreator')
    description = fields.String()
    id = fields.Integer()
    payload = fields.String()
    state = fields.String()
    target_url = fields.String()
    updated_at = fields.String()
    url = fields.String()


class Deployment_statusesItemCreator(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Deployment_statuses_create(Schema):
    description = fields.String()
    state = fields.String()
    target_url = fields.String()


class DownloadBody(Schema):
    content_type = fields.String()
    description = fields.String()
    name = fields.String(required=True)
    size = fields.Integer(required=True, description='Size of file in bytes.')


class Downloads(Schema):
    content_type = fields.String()
    description = fields.String()
    download_count = fields.Integer()
    html_url = fields.String()
    id = fields.Integer()
    name = fields.String()
    size = fields.Integer()
    url = fields.String()


class EditTeam(Schema):
    name = fields.String(required=True)
    permission = fields.String(validate=[OneOf(choices=['pull', 'push', 'admin'], labels=[])])


class Emojis(Schema):
    n100 = fields.String(dump_to='100', load_from='100')
    n1234 = fields.String(dump_to='1234', load_from='1234')
    x1 = fields.String(dump_to='+1', load_from='+1')
    x_1 = fields.String(dump_to='-1', load_from='-1')
    n8ball = fields.String(dump_to='8ball', load_from='8ball')
    a = fields.String()
    ab = fields.String()


class Event(Schema):
    actor = fields.Nested('EventActor')
    commit_id = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    event = fields.String()
    issue = fields.Nested('EventIssue')
    url = fields.String()


class EventIssue(Schema):
    assignee = fields.Nested('EventIssueAssignee')
    body = fields.String()
    closed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    comments = fields.Integer()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    html_url = fields.String()
    labels = fields.List(fields.Nested('EventIssueLabelsItem', ))
    milestone = fields.Nested('EventIssueMilestone')
    number = fields.Integer()
    pull_request = fields.Nested('EventIssuePull_request')
    state = fields.String(validate=[OneOf(choices=['open', 'closed'], labels=[])])
    title = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('EventIssueUser')


class EventIssueUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class EventIssuePull_request(Schema):
    diff_url = fields.String()
    html_url = fields.String()
    patch_url = fields.String()


class EventIssueMilestone(Schema):
    closed_issues = fields.Integer()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    creator = fields.Nested('EventIssueMilestoneCreator')
    description = fields.String()
    due_on = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    number = fields.Integer()
    open_issues = fields.Integer()
    state = fields.String(validate=[OneOf(choices=['open', 'closed'], labels=[])])
    title = fields.String()
    url = fields.String()


class EventIssueMilestoneCreator(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class EventIssueLabelsItem(Schema):
    color = fields.String()
    name = fields.String()
    url = fields.String()


class EventIssueAssignee(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class EventActor(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Events(Schema):
    actor = fields.Nested('EventsActor')
    created_at = fields.Field()
    id = fields.Integer()
    org = fields.Nested('EventsOrg')
    payload = fields.Nested('EventsPayload')
    public = fields.Boolean()
    repo = fields.Nested('EventsRepo')
    type = fields.String()


class EventsRepo(Schema):
    id = fields.Integer()
    name = fields.String()
    url = fields.String()


class EventsPayload(Schema):
    pass


class EventsOrg(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class EventsActor(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Feeds(Schema):
    _links = fields.Nested('Feeds_links')
    current_user_actor_url = fields.String()
    current_user_organization_url = fields.String()
    current_user_public = fields.String()
    current_user_url = fields.String()
    timeline_url = fields.String()
    user_url = fields.String()


class Feeds_links(Schema):
    current_user = fields.Nested('Feeds_linksCurrent_user')
    current_user_actor = fields.Nested('Feeds_linksCurrent_user_actor')
    current_user_organization = fields.Nested('Feeds_linksCurrent_user_organization')
    current_user_public = fields.Nested('Feeds_linksCurrent_user_public')
    timeline = fields.Nested('Feeds_linksTimeline')
    user = fields.Nested('Feeds_linksUser')


class Feeds_linksUser(Schema):
    href = fields.String()
    type = fields.String()


class Feeds_linksTimeline(Schema):
    href = fields.String()
    type = fields.String()


class Feeds_linksCurrent_user_public(Schema):
    href = fields.String()
    type = fields.String()


class Feeds_linksCurrent_user_organization(Schema):
    href = fields.String()
    type = fields.String()


class Feeds_linksCurrent_user_actor(Schema):
    href = fields.String()
    type = fields.String()


class Feeds_linksCurrent_user(Schema):
    href = fields.String()
    type = fields.String()


class Fork(Schema):
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('ForkOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class ForkOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class ForkBody(Schema):
    organization = fields.String()


class ForksItem(Schema):
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('ForksItemOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class ForksItemOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Gist(Schema):
    comments = fields.Integer()
    comments_url = fields.String()
    created_at = fields.String(description='Timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.')
    description = fields.String()
    files = fields.Nested('GistFiles')
    forks = fields.List(fields.Nested('GistForksItem', ))
    git_pull_url = fields.String()
    git_push_url = fields.String()
    history = fields.List(fields.Nested('GistHistoryItem', ))
    html_url = fields.String()
    id = fields.String()
    public = fields.Boolean()
    url = fields.String()
    user = fields.Nested('GistUser')


class GistUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class GistHistoryItem(Schema):
    change_status = fields.Nested('GistHistoryItemChange_status')
    committed_at = fields.String(description='Timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.')
    url = fields.String()
    user = fields.Nested('GistHistoryItemUser')
    version = fields.String()


class GistHistoryItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class GistHistoryItemChange_status(Schema):
    additions = fields.Integer()
    deletions = fields.Integer()
    total = fields.Integer()


class GistForksItem(Schema):
    created_at = fields.String(description='Timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.')
    url = fields.String()
    user = fields.Nested('GistForksItemUser')


class GistForksItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class GistFiles(Schema):
    ringerl = fields.Nested('GistFilesRingerl', dump_to='ring.erl', load_from='ring.erl')


class GistFilesRingerl(Schema):
    filename = fields.String()
    raw_url = fields.String()
    size = fields.Integer()


class GistsItem(Schema):
    comments = fields.Integer()
    comments_url = fields.String()
    created_at = fields.String()
    description = fields.String()
    files = fields.Nested('GistsItemFiles')
    git_pull_url = fields.String()
    git_push_url = fields.String()
    html_url = fields.String()
    id = fields.String()
    public = fields.Boolean()
    url = fields.String()
    user = fields.Nested('GistsItemUser')


class GistsItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class GistsItemFiles(Schema):
    ringerl = fields.Nested('GistsItemFilesRingerl', dump_to='ring.erl', load_from='ring.erl')


class GistsItemFilesRingerl(Schema):
    filename = fields.String()
    raw_url = fields.String()
    size = fields.Integer()


class GitCommit(Schema):
    author = fields.Nested('GitCommitAuthor')
    message = fields.String()
    parents = fields.String()
    tree = fields.String()


class GitCommitAuthor(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class GitRefPatch(Schema):
    force = fields.Boolean()
    sha = fields.String()


class Gitignore_lang(Schema):
    name = fields.String()
    source = fields.String()


class HeadBranch(Schema):
    object = fields.Nested('HeadBranchObject')
    ref = fields.String()
    url = fields.String()


class HeadBranchObject(Schema):
    sha = fields.String()
    type = fields.String()
    url = fields.String()


class HeadBranchBody(Schema):
    force = fields.Boolean(required=True, description='Boolean indicating whether to force the update or to make sure the update is a fast-forward update. The default is false, so leaving this out or setting it to false will make sure you’re not overwriting work.')
    sha = fields.String(required=True, description='String of the SHA1 value to set this reference to.')


class HeadsItem(Schema):
    commit = fields.Nested('HeadsItemCommit')
    name = fields.String()
    tarball_url = fields.String()
    zipball_url = fields.String()


class HeadsItemCommit(Schema):
    sha = fields.String()
    url = fields.String()


class HookItem(Schema):
    active = fields.Boolean()
    config = fields.Nested('HookItemConfig')
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    events = fields.List(fields.String())
    id = fields.Integer()
    name = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()


class HookItemConfig(Schema):
    content_type = fields.String()
    url = fields.String()


class HookBody(Schema):
    active = fields.Boolean()
    add_events = fields.List(fields.String())


class Issue(Schema):
    assignee = fields.String()
    body = fields.String()
    labels = fields.List(fields.String())
    milestone = fields.Number()
    title = fields.String()


class IssueBody(Schema):
    assignee = fields.String()
    body = fields.String()
    labels = fields.List(fields.String())
    milestone = fields.Number()
    title = fields.String()


class IssuesItem(Schema):
    assignee = fields.Nested('IssuesItemAssignee')
    body = fields.String()
    closed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    comments = fields.Integer()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    html_url = fields.String()
    labels = fields.List(fields.Nested('IssuesItemLabelsItem', ))
    milestone = fields.Nested('IssuesItemMilestone')
    number = fields.Integer()
    pull_request = fields.Nested('IssuesItemPull_request')
    state = fields.String(validate=[OneOf(choices=['open', 'closed'], labels=[])])
    title = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('IssuesItemUser')


class IssuesItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class IssuesItemPull_request(Schema):
    diff_url = fields.String()
    html_url = fields.String()
    patch_url = fields.String()


class IssuesItemMilestone(Schema):
    closed_issues = fields.Integer()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    creator = fields.Nested('IssuesItemMilestoneCreator')
    description = fields.String()
    due_on = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    number = fields.Integer()
    open_issues = fields.Integer()
    state = fields.String(validate=[OneOf(choices=['open', 'closed'], labels=[])])
    title = fields.String()
    url = fields.String()


class IssuesItemMilestoneCreator(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class IssuesItemLabelsItem(Schema):
    color = fields.String()
    name = fields.String()
    url = fields.String()


class IssuesItemAssignee(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class IssuesComment(Schema):
    body = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    html_url = fields.String()
    id = fields.Integer()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('IssuesCommentUser')


class IssuesCommentUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class IssuesCommentsItem(Schema):
    _links = fields.Nested('IssuesCommentsItem_links')
    body = fields.String()
    commit_id = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    id = fields.Integer()
    path = fields.String()
    position = fields.Integer()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('IssuesCommentsItemUser')


class IssuesCommentsItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class IssuesCommentsItem_links(Schema):
    html = fields.Nested('IssuesCommentsItem_linksHtml')
    pull_request = fields.Nested('IssuesCommentsItem_linksPull_request')
    self = fields.Nested('IssuesCommentsItem_linksSelf')


class IssuesCommentsItem_linksSelf(Schema):
    href = fields.String()


class IssuesCommentsItem_linksPull_request(Schema):
    href = fields.String()


class IssuesCommentsItem_linksHtml(Schema):
    href = fields.String()


class Key(Schema):
    id = fields.Integer()
    key = fields.String()
    title = fields.String()
    url = fields.String()


class KeyBody(Schema):
    key = fields.String()
    title = fields.String()


class KeysItem(Schema):
    id = fields.Integer()
    key = fields.String()
    title = fields.String()
    url = fields.String()


class Label(Schema):
    color = fields.String(validate=[Length(min=6, max=6, equal=None)])
    name = fields.String()
    url = fields.String()


class LabelsItem(Schema):
    color = fields.String(validate=[Length(min=6, max=6, equal=None)])
    name = fields.String()
    url = fields.String()


class Languages(Schema):
    pass


class Markdown(Schema):
    context = fields.String()
    mode = fields.String()
    text = fields.String()


class MembersItem(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Merge(Schema):
    merged = fields.Boolean()
    message = fields.String()
    sha = fields.String()


class MergePullBody(Schema):
    commit_message = fields.String()


class MergesBody(Schema):
    base = fields.String()
    commit_message = fields.String()
    head = fields.String()


class MergesConflict(Schema):
    message = fields.String(description='Error message')


class MergesSuccessful(Schema):
    author = fields.Nested('MergesSuccessfulAuthor')
    comments_url = fields.String()
    commit = fields.Nested('MergesSuccessfulCommit')
    committer = fields.Nested('MergesSuccessfulCommitter')
    merged = fields.Boolean()
    message = fields.String()
    parents = fields.List(fields.Nested('MergesSuccessfulParentsItem', ))
    sha = fields.String()
    url = fields.String()


class MergesSuccessfulParentsItem(Schema):
    sha = fields.String()
    url = fields.String()


class MergesSuccessfulCommitter(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class MergesSuccessfulCommit(Schema):
    author = fields.Nested('MergesSuccessfulCommitAuthor')
    comment_count = fields.Integer()
    committer = fields.Nested('MergesSuccessfulCommitCommitter')
    message = fields.String()
    tree = fields.Nested('MergesSuccessfulCommitTree')
    url = fields.String()


class MergesSuccessfulCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class MergesSuccessfulCommitCommitter(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class MergesSuccessfulCommitAuthor(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class MergesSuccessfulAuthor(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Meta(Schema):
    git = fields.List(fields.String())
    hooks = fields.List(fields.String())


class Milestone(Schema):
    closed_issues = fields.Integer()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    creator = fields.Nested('MilestoneCreator')
    description = fields.String()
    due_on = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    number = fields.Integer()
    open_issues = fields.Integer()
    state = fields.String(validate=[OneOf(choices=['open', 'closed'], labels=[])])
    title = fields.String()
    url = fields.String()


class MilestoneCreator(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class MilestoneBody(Schema):
    description = fields.String()
    due_on = fields.String()
    state = fields.String()
    title = fields.String()


class MilestoneUpdate(Schema):
    description = fields.String()
    due_on = fields.String()
    state = fields.String()
    title = fields.String()


class NotificationMarkRead(Schema):
    last_read_at = fields.String()


class Notifications(Schema):
    id = fields.Integer()
    last_read_at = fields.String()
    reason = fields.String()
    repository = fields.Nested('NotificationsRepository')
    subject = fields.Nested('NotificationsSubject')
    unread = fields.Boolean()
    updated_at = fields.String()
    url = fields.String()


class NotificationsSubject(Schema):
    latest_comment_url = fields.String()
    title = fields.String()
    type = fields.String()
    url = fields.String()


class NotificationsRepository(Schema):
    description = fields.String()
    fork = fields.Boolean()
    full_name = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    name = fields.String()
    owner = fields.Nested('NotificationsRepositoryOwner')
    private = fields.Boolean()
    url = fields.String()


class NotificationsRepositoryOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class OrgMembersItem(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class OrgPublicMembersItem(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class OrgTeamsItem(Schema):
    id = fields.Integer()
    name = fields.String()
    url = fields.String()


class OrgTeamsPost(Schema):
    name = fields.String(required=True)
    permission = fields.String(validate=[OneOf(choices=['pull', 'push', 'admin'], labels=[])])
    repo_names = fields.List(fields.String())


class Organization(Schema):
    avatar_url = fields.String()
    blog = fields.String()
    company = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    followers = fields.Integer()
    following = fields.Integer()
    html_url = fields.String()
    id = fields.Integer()
    location = fields.String()
    login = fields.String()
    name = fields.String()
    public_gists = fields.Integer()
    public_repos = fields.Integer()
    type = fields.String()
    url = fields.String()


class OrganizationAsTeamMember(Schema):
    errors = fields.List(fields.Nested('OrganizationAsTeamMemberErrorsItem', ))
    message = fields.String()


class OrganizationAsTeamMemberErrorsItem(Schema):
    code = fields.String()
    field = fields.String()
    resource = fields.String()


class ParticipationStats(Schema):
    all = fields.List(fields.Integer())
    owner = fields.List(fields.Integer())


class PatchGist(Schema):
    description = fields.String()
    files = fields.Nested('PatchGistFiles')


class PatchGistFiles(Schema):
    delete_this_filetxt = fields.String(dump_to='delete_this_file.txt', load_from='delete_this_file.txt')
    file1txt = fields.Nested('PatchGistFilesFile1txt', dump_to='file1.txt', load_from='file1.txt')
    new_filetxt = fields.Nested('PatchGistFilesNew_filetxt', dump_to='new_file.txt', load_from='new_file.txt')
    old_nametxt = fields.Nested('PatchGistFilesOld_nametxt', dump_to='old_name.txt', load_from='old_name.txt')


class PatchGistFilesOld_nametxt(Schema):
    content = fields.String()
    filename = fields.String()


class PatchGistFilesNew_filetxt(Schema):
    content = fields.String()


class PatchGistFilesFile1txt(Schema):
    content = fields.String()


class PatchOrg(Schema):
    billing_email = fields.String(description='Billing email address. This address is not publicized.')
    company = fields.String()
    email = fields.String(description='Publicly visible email address.')
    location = fields.String()
    name = fields.String()


class PostComment(Schema):
    body = fields.String(required=True)


class PostGist(Schema):
    description = fields.String()
    files = fields.Nested('PostGistFiles')
    public = fields.Boolean()


class PostGistFiles(Schema):
    file1txt = fields.Nested('PostGistFilesFile1txt', dump_to='file1.txt', load_from='file1.txt')


class PostGistFilesFile1txt(Schema):
    content = fields.String()


class PostRepo(Schema):
    auto_init = fields.Boolean(description='True to create an initial commit with empty README. Default is false.')
    description = fields.String()
    gitignore_template = fields.String(description='Desired language or platform .gitignore template to apply. Use the name of the template without the extension. For example, "Haskell" Ignored if auto_init parameter is not provided. ')
    has_downloads = fields.Boolean(description='True to enable downloads for this repository, false to disable them. Default is true.')
    has_issues = fields.Boolean(description='True to enable issues for this repository, false to disable them. Default is true.')
    has_wiki = fields.Boolean(description='True to enable the wiki for this repository, false to disable it. Default is true.')
    homepage = fields.String()
    name = fields.String(required=True)
    private = fields.Boolean(description='True to create a private repository, false to create a public one. Creating private repositories requires a paid GitHub account.')
    team_id = fields.Integer(description='The id of the team that will be granted access to this repository. This is only valid when creating a repo in an organization.')


class PullRequest(Schema):
    _links = fields.Nested('PullRequest_links')
    additions = fields.Integer()
    base = fields.Nested('PullRequestBase')
    body = fields.String()
    changed_files = fields.Integer()
    closed_at = fields.String()
    comments = fields.Integer()
    commits = fields.Integer()
    created_at = fields.String()
    deletions = fields.Integer()
    diff_url = fields.String()
    head = fields.Nested('PullRequestHead')
    html_url = fields.String()
    issue_url = fields.String()
    merge_commit_sha = fields.String()
    mergeable = fields.Boolean()
    merged = fields.Boolean()
    merged_at = fields.String()
    merged_by = fields.Nested('PullRequestMerged_by')
    number = fields.Integer()
    patch_url = fields.String()
    state = fields.String()
    title = fields.String()
    updated_at = fields.String()
    url = fields.String()
    user = fields.Nested('PullRequestUser')


class PullRequestUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullRequestMerged_by(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullRequestHead(Schema):
    label = fields.String()
    ref = fields.String()
    repo = fields.Nested('PullRequestHeadRepo')
    sha = fields.String()
    user = fields.Nested('PullRequestHeadUser')


class PullRequestHeadUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullRequestHeadRepo(Schema):
    clone_url = fields.String()
    created_at = fields.String()
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.Field()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('PullRequestHeadRepoOwner')
    private = fields.Boolean()
    pushed_at = fields.String()
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String()
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class PullRequestHeadRepoOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullRequestBase(Schema):
    label = fields.String()
    ref = fields.String()
    repo = fields.Nested('PullRequestBaseRepo')
    sha = fields.String()
    user = fields.Nested('PullRequestBaseUser')


class PullRequestBaseUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullRequestBaseRepo(Schema):
    clone_url = fields.String()
    created_at = fields.String()
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.Field()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('PullRequestBaseRepoOwner')
    private = fields.Boolean()
    pushed_at = fields.String()
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String()
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class PullRequestBaseRepoOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullRequest_links(Schema):
    comments = fields.Nested('PullRequest_linksComments')
    html = fields.Nested('PullRequest_linksHtml')
    review_comments = fields.Nested('PullRequest_linksReview_comments')
    self = fields.Nested('PullRequest_linksSelf')


class PullRequest_linksSelf(Schema):
    href = fields.String()


class PullRequest_linksReview_comments(Schema):
    href = fields.String()


class PullRequest_linksHtml(Schema):
    href = fields.String()


class PullRequest_linksComments(Schema):
    href = fields.String()


class PullUpdate(Schema):
    body = fields.String()
    state = fields.String()
    title = fields.String()


class PullsItem(Schema):
    _links = fields.Nested('PullsItem_links')
    base = fields.Nested('PullsItemBase')
    body = fields.String()
    closed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    diff_url = fields.String()
    head = fields.Nested('PullsItemHead')
    html_url = fields.String()
    issue_url = fields.String()
    merged_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    number = fields.Integer()
    patch_url = fields.String()
    state = fields.String(validate=[OneOf(choices=['open', 'closed'], labels=[])])
    title = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('PullsItemUser')


class PullsItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullsItemHead(Schema):
    label = fields.String()
    ref = fields.String()
    repo = fields.Nested('PullsItemHeadRepo')
    sha = fields.String()
    user = fields.Nested('PullsItemHeadUser')


class PullsItemHeadUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullsItemHeadRepo(Schema):
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('PullsItemHeadRepoOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class PullsItemHeadRepoOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullsItemBase(Schema):
    label = fields.String()
    ref = fields.String()
    repo = fields.Nested('PullsItemBaseRepo')
    sha = fields.String()
    user = fields.Nested('PullsItemBaseUser')


class PullsItemBaseUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullsItemBaseRepo(Schema):
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('PullsItemBaseRepoOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class PullsItemBaseRepoOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullsItem_links(Schema):
    comments = fields.Nested('PullsItem_linksComments')
    html = fields.Nested('PullsItem_linksHtml')
    review_comments = fields.Nested('PullsItem_linksReview_comments')
    self = fields.Nested('PullsItem_linksSelf')


class PullsItem_linksSelf(Schema):
    href = fields.String()


class PullsItem_linksReview_comments(Schema):
    href = fields.String()


class PullsItem_linksHtml(Schema):
    href = fields.String()


class PullsItem_linksComments(Schema):
    href = fields.String()


class PullsComment(Schema):
    _links = fields.Nested('PullsComment_links')
    body = fields.String()
    commit_id = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    id = fields.Integer()
    path = fields.String()
    position = fields.Integer()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('PullsCommentUser')


class PullsCommentUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullsComment_links(Schema):
    html = fields.Nested('PullsComment_linksHtml')
    pull_request = fields.Nested('PullsComment_linksPull_request')
    self = fields.Nested('PullsComment_linksSelf')


class PullsComment_linksSelf(Schema):
    href = fields.String()


class PullsComment_linksPull_request(Schema):
    href = fields.String()


class PullsComment_linksHtml(Schema):
    href = fields.String()


class PullsCommentPost(Schema):
    body = fields.String()
    commit_id = fields.String()
    path = fields.String()
    position = fields.Number()


class PullsCommentsItem(Schema):
    _links = fields.Nested('PullsCommentsItem_links')
    body = fields.String()
    commit_id = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    id = fields.Integer()
    path = fields.String()
    position = fields.Integer()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('PullsCommentsItemUser')


class PullsCommentsItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class PullsCommentsItem_links(Schema):
    html = fields.Nested('PullsCommentsItem_linksHtml')
    pull_request = fields.Nested('PullsCommentsItem_linksPull_request')
    self = fields.Nested('PullsCommentsItem_linksSelf')


class PullsCommentsItem_linksSelf(Schema):
    href = fields.String()


class PullsCommentsItem_linksPull_request(Schema):
    href = fields.String()


class PullsCommentsItem_linksHtml(Schema):
    href = fields.String()


class PullsPost(Schema):
    base = fields.String()
    body = fields.String()
    head = fields.String()
    title = fields.String()


class PutSubscription(Schema):
    created_at = fields.String()
    ignored = fields.Boolean()
    reason = fields.Field()
    subscribed = fields.Boolean()
    thread_url = fields.String()
    url = fields.String()


class Rate_limit(Schema):
    rate = fields.Nested('Rate_limitRate')


class Rate_limitRate(Schema):
    limit = fields.Integer()
    remaining = fields.Integer()
    reset = fields.Integer()


class Readme(Schema):
    _links = fields.Nested('Readme_links')
    content = fields.String()
    encoding = fields.String()
    git_url = fields.String()
    html_url = fields.String()
    name = fields.String()
    path = fields.String()
    sha = fields.String()
    size = fields.Integer()
    type = fields.String()
    url = fields.String()


class Readme_links(Schema):
    git = fields.String()
    html = fields.String()
    self = fields.String()


class RefItem(Schema):
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    creator = fields.Nested('RefItemCreator')
    description = fields.String()
    id = fields.Integer()
    state = fields.String()
    target_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()


class RefItemCreator(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class RefBody(Schema):
    object = fields.Nested('RefBodyObject')
    ref = fields.String()
    url = fields.String()


class RefBodyObject(Schema):
    sha = fields.String()
    type = fields.String()
    url = fields.String()


class RefStatusItem(Schema):
    commit_url = fields.String()
    name = fields.String()
    repository_url = fields.String()
    sha = fields.String()
    state = fields.String()
    statuses = fields.List(fields.Nested('RefStatusItemStatusesItem', ))


class RefStatusItemStatusesItem(Schema):
    context = fields.String()
    created_at = fields.String()
    description = fields.String()
    id = fields.Number()
    state = fields.String()
    target_url = fields.String()
    updated_at = fields.String()
    url = fields.String()


class RefsItem(Schema):
    object = fields.Nested('RefsItemObject')
    ref = fields.String()
    url = fields.String()


class RefsItemObject(Schema):
    sha = fields.String()
    type = fields.String()
    url = fields.String()


class RefsBody(Schema):
    ref = fields.String()
    sha = fields.String()


class Release(Schema):
    assets = fields.List(fields.Nested('ReleaseAssetsItem', ))
    assets_url = fields.String()
    author = fields.Nested('ReleaseAuthor')
    body = fields.String()
    created_at = fields.String()
    draft = fields.Boolean()
    html_url = fields.String()
    id = fields.Integer()
    name = fields.String()
    prerelease = fields.Boolean()
    published_at = fields.String()
    tag_name = fields.String()
    tarball_url = fields.String()
    target_commitish = fields.String()
    upload_url = fields.String()
    url = fields.String()
    zipball_url = fields.String()


class ReleaseAuthor(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class ReleaseAssetsItem(Schema):
    content_type = fields.String()
    created_at = fields.String()
    download_count = fields.Integer()
    id = fields.Integer()
    label = fields.String()
    name = fields.String()
    size = fields.Integer()
    state = fields.String()
    updated_at = fields.String()
    uploader = fields.Nested('ReleaseAssetsItemUploader')
    url = fields.String()


class ReleaseAssetsItemUploader(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Release_create(Schema):
    body = fields.String()
    draft = fields.Boolean()
    name = fields.String()
    prerelease = fields.Boolean()
    tag_name = fields.String()
    target_commitish = fields.String()


class ReleasesItem(Schema):
    assets = fields.List(fields.Nested('ReleasesItemAssetsItem', ))
    assets_url = fields.String()
    author = fields.Nested('ReleasesItemAuthor')
    body = fields.String()
    created_at = fields.String()
    draft = fields.Boolean()
    html_url = fields.String()
    id = fields.Integer()
    name = fields.String()
    prerelease = fields.Boolean()
    published_at = fields.String()
    tag_name = fields.String()
    tarball_url = fields.String()
    target_commitish = fields.String()
    upload_url = fields.String()
    url = fields.String()
    zipball_url = fields.String()


class ReleasesItemAuthor(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class ReleasesItemAssetsItem(Schema):
    content_type = fields.String()
    created_at = fields.String()
    download_count = fields.Integer()
    id = fields.Integer()
    label = fields.String()
    name = fields.String()
    size = fields.Integer()
    state = fields.String()
    updated_at = fields.String()
    uploader = fields.Nested('ReleasesItemAssetsItemUploader')
    url = fields.String()


class ReleasesItemAssetsItemUploader(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Repo(Schema):
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    has_downloads = fields.Boolean()
    has_issues = fields.Boolean()
    has_wiki = fields.Boolean()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    organization = fields.Nested('RepoOrganization')
    owner = fields.Nested('RepoOwner')
    parent = fields.Nested('RepoParent', description='Is present when the repo is a fork. Parent is the repo this repo was forked from.')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    source = fields.Nested('RepoSource', description='Is present when the repo is a fork. Source is the ultimate source for the network.')
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class RepoSource(Schema):
    """Is present when the repo is a fork. Source is the ultimate source for the network."""
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('RepoSourceOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class RepoSourceOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class RepoParent(Schema):
    """Is present when the repo is a fork. Parent is the repo this repo was forked from."""
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('RepoParentOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class RepoParentOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class RepoOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class RepoOrganization(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    type = fields.String()
    url = fields.String()


class Repo_deploymentsItem(Schema):
    created_at = fields.String()
    creator = fields.Nested('Repo_deploymentsItemCreator')
    description = fields.String()
    id = fields.Integer()
    payload = fields.String()
    sha = fields.String()
    statuses_url = fields.String()
    updated_at = fields.String()
    url = fields.String()


class Repo_deploymentsItemCreator(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    site_admin = fields.Boolean()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class RepoCommentsItem(Schema):
    body = fields.String()
    commit_id = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    html_url = fields.String()
    id = fields.Integer()
    line = fields.Integer()
    path = fields.String()
    position = fields.Integer()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    user = fields.Nested('RepoCommentsItemUser')


class RepoCommentsItemUser(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class RepoCommit(Schema):
    author = fields.Nested('RepoCommitAuthor')
    committer = fields.Nested('RepoCommitCommitter')
    message = fields.String()
    parents = fields.List(fields.Nested('RepoCommitParentsItem', ))
    sha = fields.String()
    tree = fields.Nested('RepoCommitTree')
    url = fields.String()


class RepoCommitTree(Schema):
    sha = fields.String()
    url = fields.String()


class RepoCommitParentsItem(Schema):
    sha = fields.String()
    url = fields.String()


class RepoCommitCommitter(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class RepoCommitAuthor(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class RepoCommitBody(Schema):
    author = fields.Nested('RepoCommitBodyAuthor')
    message = fields.String(required=True)
    parents = fields.List(fields.String(required=True))
    tree = fields.String(required=True)


class RepoCommitBodyAuthor(Schema):
    date = fields.String()
    email = fields.String()
    name = fields.String()


class RepoEdit(Schema):
    description = fields.String()
    has_downloads = fields.Boolean()
    has_issues = fields.Boolean()
    has_wiki = fields.Boolean()
    homepage = fields.String()
    name = fields.String()
    private = fields.Boolean()


class ReposItem(Schema):
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('ReposItemOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class ReposItemOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class RepositoriesItem(Schema):
    description = fields.String()
    fork = fields.Boolean()
    full_name = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    name = fields.String()
    owner = fields.Nested('RepositoriesItemOwner')
    private = fields.Boolean()
    url = fields.String()


class RepositoriesItemOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Search_code(Schema):
    items = fields.List(fields.Nested('Search_codeItemsItem', ))
    total_count = fields.Integer()


class Search_codeItemsItem(Schema):
    git_url = fields.String()
    html_url = fields.String()
    name = fields.String()
    path = fields.String()
    repository = fields.Nested('Search_codeItemsItemRepository')
    score = fields.Number()
    sha = fields.String()
    url = fields.String()


class Search_codeItemsItemRepository(Schema):
    archive_url = fields.String()
    assignees_url = fields.String()
    blobs_url = fields.String()
    branches_url = fields.String()
    collaborators_url = fields.String()
    comments_url = fields.String()
    commits_url = fields.String()
    compare_url = fields.String()
    contents_url = fields.String()
    contributors_url = fields.String()
    description = fields.String()
    downloads_url = fields.String()
    events_url = fields.String()
    fork = fields.Boolean()
    forks_url = fields.String()
    full_name = fields.String()
    git_commits_url = fields.String()
    git_refs_url = fields.String()
    git_tags_url = fields.String()
    hooks_url = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    issue_comment_url = fields.String()
    issue_events_url = fields.String()
    issues_url = fields.String()
    keys_url = fields.String()
    labels_url = fields.String()
    languages_url = fields.String()
    merges_url = fields.String()
    milestones_url = fields.String()
    name = fields.String()
    notifications_url = fields.String()
    owner = fields.Nested('Search_codeItemsItemRepositoryOwner')
    private = fields.Boolean()
    pulls_url = fields.String()
    stargazers_url = fields.String()
    statuses_url = fields.String()
    subscribers_url = fields.String()
    subscription_url = fields.String()
    tags_url = fields.String()
    teams_url = fields.String()
    trees_url = fields.String()
    url = fields.String()


class Search_codeItemsItemRepositoryOwner(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Search_issues(Schema):
    items = fields.List(fields.Nested('Search_issuesItemsItem', ))
    total_count = fields.Integer()


class Search_issuesItemsItem(Schema):
    assignee = fields.Field()
    body = fields.String()
    closed_at = fields.Field()
    comments = fields.Integer()
    comments_url = fields.String()
    created_at = fields.String()
    events_url = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    labels = fields.List(fields.Nested('Search_issuesItemsItemLabelsItem', ))
    labels_url = fields.String()
    milestone = fields.Field()
    number = fields.Integer()
    pull_request = fields.Nested('Search_issuesItemsItemPull_request')
    score = fields.Number()
    state = fields.String()
    title = fields.String()
    updated_at = fields.String()
    url = fields.String()
    user = fields.Nested('Search_issuesItemsItemUser')


class Search_issuesItemsItemUser(Schema):
    avatar_url = fields.String()
    events_url = fields.String()
    followers_url = fields.String()
    following_url = fields.String()
    gists_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    starred_url = fields.String()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Search_issuesItemsItemPull_request(Schema):
    diff_url = fields.Field()
    html_url = fields.Field()
    patch_url = fields.Field()


class Search_issuesItemsItemLabelsItem(Schema):
    color = fields.String()
    name = fields.String()
    url = fields.String()


class Search_issues_by_keyword(Schema):
    issues = fields.List(fields.Nested('Search_issues_by_keywordIssuesItem', ))


class Search_issues_by_keywordIssuesItem(Schema):
    body = fields.String()
    comments = fields.Integer()
    created_at = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    labels = fields.List(fields.String())
    number = fields.Integer()
    position = fields.Integer()
    state = fields.String()
    title = fields.String()
    updated_at = fields.String()
    user = fields.String()
    votes = fields.Integer()


class Search_repositories(Schema):
    items = fields.List(fields.Nested('Search_repositoriesItemsItem', ))
    total_count = fields.Integer()


class Search_repositoriesItemsItem(Schema):
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    default_branch = fields.String()
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('Search_repositoriesItemsItemOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    score = fields.Number()
    size = fields.Integer()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class Search_repositoriesItemsItemOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    received_events_url = fields.String()
    type = fields.String()
    url = fields.String()


class Search_repositories_by_keyword(Schema):
    repositories = fields.List(fields.Nested('Search_repositories_by_keywordRepositoriesItem', ))


class Search_repositories_by_keywordRepositoriesItem(Schema):
    created = fields.String()
    created_at = fields.String()
    description = fields.String()
    followers = fields.Integer()
    fork = fields.Boolean()
    forks = fields.Integer()
    has_downloads = fields.Boolean()
    has_issues = fields.Boolean()
    has_wiki = fields.Boolean()
    homepage = fields.String()
    language = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    owner = fields.String()
    private = fields.Boolean()
    pushed = fields.String()
    pushed_at = fields.String()
    score = fields.Number()
    size = fields.Integer()
    type = fields.String()
    url = fields.String()
    username = fields.String()
    watchers = fields.Integer()


class Search_user_by_email(Schema):
    user = fields.Nested('Search_user_by_emailUser')


class Search_user_by_emailUser(Schema):
    blog = fields.String()
    company = fields.String()
    created = fields.String()
    created_at = fields.String()
    email = fields.String()
    followers_count = fields.Integer()
    following_count = fields.Integer()
    gravatar_id = fields.String()
    id = fields.Integer()
    location = fields.String()
    login = fields.String()
    name = fields.String()
    public_gist_count = fields.Integer()
    public_repo_count = fields.Integer()
    type = fields.String()


class Search_users(Schema):
    items = fields.List(fields.Nested('Search_usersItemsItem', ))
    total_count = fields.Integer()


class Search_usersItemsItem(Schema):
    avatar_url = fields.String()
    followers_url = fields.String()
    gravatar_id = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    organizations_url = fields.String()
    received_events_url = fields.String()
    repos_url = fields.String()
    score = fields.Number()
    subscriptions_url = fields.String()
    type = fields.String()
    url = fields.String()


class Search_users_by_keyword(Schema):
    users = fields.List(fields.Nested('Search_users_by_keywordUsersItem', ))


class Search_users_by_keywordUsersItem(Schema):
    created = fields.String()
    created_at = fields.String()
    followers = fields.Integer()
    followers_count = fields.Integer()
    fullname = fields.String()
    gravatar_id = fields.String()
    id = fields.String()
    language = fields.String()
    location = fields.String()
    login = fields.String()
    name = fields.String()
    public_repo_count = fields.Integer()
    repos = fields.Integer()
    score = fields.Number()
    type = fields.String()
    username = fields.String()


class StargazersItem(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Subscribition(Schema):
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    ignored = fields.Boolean()
    reason = fields.String()
    repository_url = fields.String()
    subscribed = fields.Boolean()
    url = fields.String()


class SubscribitionBody(Schema):
    ignored = fields.Boolean()
    subscribed = fields.Boolean()


class Subscription(Schema):
    created_at = fields.String()
    ignored = fields.Boolean()
    reason = fields.Boolean()
    subscribed = fields.Boolean()
    thread_url = fields.String()
    url = fields.String()


class Tag(Schema):
    message = fields.String()
    object = fields.Nested('TagObject')
    sha = fields.String()
    tag = fields.String()
    tagger = fields.Nested('TagTagger')
    url = fields.String()


class TagTagger(Schema):
    date = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String()
    name = fields.String()


class TagObject(Schema):
    sha = fields.String()
    type = fields.String()
    url = fields.String()


class Tags(Schema):
    message = fields.String(required=True, description='String of the tag message.')
    object = fields.String(required=True, description='String of the SHA of the git object this is tagging.')
    tag = fields.String(required=True)
    tagger = fields.Nested('TagsTagger', required=True)
    type = fields.String(required=True, description='String of the type of the object we’re tagging. Normally this is a commit but it can also be a tree or a blob.')


class TagsTagger(Schema):
    date = fields.String(description='Timestamp of when this object was tagged.')
    email = fields.String(description='String of the email of the author of the tag.')
    name = fields.String(description='String of the name of the author of the tag.')


class Team(Schema):
    id = fields.Integer()
    members_count = fields.Integer()
    name = fields.String()
    permission = fields.String()
    repos_count = fields.Integer()
    url = fields.String()


class TeamMembership(Schema):
    state = fields.String()
    url = fields.String()


class TeamReposItem(Schema):
    clone_url = fields.String()
    created_at = fields.String()
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.Field()
    master_branch = fields.String()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('TeamReposItemOwner')
    private = fields.Boolean()
    pushed_at = fields.String()
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String()
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class TeamReposItemOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class TeamsItem(Schema):
    id = fields.Integer()
    name = fields.String()
    url = fields.String()


class Teams_listItem(Schema):
    id = fields.Integer()
    members_count = fields.Integer()
    name = fields.String()
    organization = fields.Nested('Teams_listItemOrganization')
    permission = fields.String()
    repos_count = fields.Integer()
    url = fields.String()


class Teams_listItemOrganization(Schema):
    avatar_url = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class Tree(Schema):
    sha = fields.String()
    tree = fields.List(fields.Nested('TreeTreeItem', ))
    url = fields.String()


class TreeTreeItem(Schema):
    mode = fields.String()
    path = fields.String()
    sha = fields.String()
    size = fields.Integer()
    type = fields.String()
    url = fields.String()


class Trees(Schema):
    base_tree = fields.String()
    sha = fields.String(description='SHA1 checksum ID of the object in the tree.')
    tree = fields.List(fields.Nested('TreesTreeItem', ))
    url = fields.String()


class TreesTreeItem(Schema):
    mode = fields.String(description='One of 100644 for file (blob), 100755 for executable (blob), 040000 for subdirectory (tree), 160000 for submodule (commit) or 120000 for a blob that specifies the path of a symlink.', validate=[OneOf(choices=['100644', '100755', '040000', '160000', '120000'], labels=[])])
    path = fields.String()
    sha = fields.String(description='SHA1 checksum ID of the object in the tree.')
    type = fields.String(validate=[OneOf(choices=['blob', 'tree', 'commit'], labels=[])])
    url = fields.String()


class User(Schema):
    avatar_url = fields.String()
    bio = fields.String()
    blog = fields.String()
    collaborators = fields.Integer()
    company = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    disk_usage = fields.Integer()
    email = fields.String()
    followers = fields.Integer()
    following = fields.Integer()
    gravatar_id = fields.String()
    hireable = fields.Boolean()
    html_url = fields.String()
    id = fields.Integer()
    location = fields.String()
    login = fields.String()
    name = fields.String()
    owned_private_repos = fields.Integer()
    plan = fields.Nested('UserPlan')
    private_gists = fields.Integer()
    public_gists = fields.Integer()
    public_repos = fields.Integer()
    total_private_repos = fields.Integer()
    type = fields.String()
    url = fields.String()


class UserPlan(Schema):
    collaborators = fields.Integer()
    name = fields.String()
    private_repos = fields.Integer()
    space = fields.Integer()


class User_keys_keyId(Schema):
    id = fields.Integer()
    key = fields.String()
    title = fields.String()
    url = fields.String()


class User_keys_post(Schema):
    key = fields.String()
    title = fields.String()


class User_update(Schema):
    bio = fields.String()
    blog = fields.String()
    company = fields.String()
    email = fields.String()
    hireable = fields.Boolean()
    location = fields.String()
    name = fields.String()


class User_userId(Schema):
    avatar_url = fields.String()
    bio = fields.String()
    blog = fields.String()
    company = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    email = fields.String(description='Note: The returned email is the user’s publicly visible email address (or null if the user has not specified a public email address in their profile).')
    followers = fields.Integer()
    following = fields.Integer()
    gravatar_id = fields.String()
    hireable = fields.Boolean()
    html_url = fields.String()
    id = fields.Integer()
    location = fields.String()
    login = fields.String()
    name = fields.String()
    public_gists = fields.Integer()
    public_repos = fields.Integer()
    type = fields.String()
    url = fields.String()


class User_userId_subscribitionsItem(Schema):
    clone_url = fields.String()
    created_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    description = fields.String()
    fork = fields.Boolean()
    forks = fields.Integer()
    forks_count = fields.Integer()
    full_name = fields.String()
    git_url = fields.String()
    homepage = fields.String()
    html_url = fields.String()
    id = fields.Integer()
    language = fields.String()
    master_branch = fields.Integer()
    mirror_url = fields.String()
    name = fields.String()
    open_issues = fields.Integer()
    open_issues_count = fields.Integer()
    owner = fields.Nested('User_userId_subscribitionsItemOwner')
    private = fields.Boolean()
    pushed_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    size = fields.Integer()
    ssh_url = fields.String()
    svn_url = fields.String()
    updated_at = fields.String(description='ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ')
    url = fields.String()
    watchers = fields.Integer()
    watchers_count = fields.Integer()


class User_userId_subscribitionsItemOwner(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class UsersItem(Schema):
    avatar_url = fields.String()
    gravatar_id = fields.String()
    id = fields.Integer()
    login = fields.String()
    url = fields.String()


class EmojisInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class EventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class FeedsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class GistsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            since = fields.String(description='Timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ.\nOnly gists updated at or after this time are returned.\n')


    class Post(object):
        class Body(PostGist):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class GistsPublicInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            since = fields.String(description='Timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ.\nOnly gists updated at or after this time are returned.\n')




class GistsStarredInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            since = fields.String(description='Timestamp in ISO 8601 format YYYY-MM-DDTHH:MM:SSZ.\nOnly gists updated at or after this time are returned.\n')




class GistsIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')


    class Patch(object):
        class Body(PatchGist):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')




class GistsIdCommentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')


    class Post(object):
        class Body(CommentBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')




class GistsIdCommentsCommentIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')
            commentId = fields.Integer(description='Id of comment.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')
            commentId = fields.Integer(description='Id of comment.')


    class Patch(object):
        class Body(Comment):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')
            commentId = fields.Integer(description='Id of comment.')




class GistsIdForksInput(object):
    class Post(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')




class GistsIdStarInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of gist.')




class GitignoreTemplatesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class GitignoreTemplatesLanguageInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            language = fields.String()




class IssuesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            filter = fields.String(description="Issues assigned to you / created by you / mentioning you / you're\nsubscribed to updates for / All issues the authenticated user can see\n", missing=lambda: 'all', validate=[OneOf(choices=['assigned', 'created', 'mentioned', 'subscribed', 'all'], labels=[])])
            state = fields.String(missing=lambda: 'open', validate=[OneOf(choices=['open', 'closed'], labels=[])])
            labels = fields.String(description='String list of comma separated Label names. Example - bug,ui,@high.')
            sort = fields.String(missing=lambda: 'created', validate=[OneOf(choices=['created', 'updated', 'comments'], labels=[])])
            direction = fields.String(missing=lambda: 'desc', validate=[OneOf(choices=['asc', 'desc'], labels=[])])
            since = fields.String(description='Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nOnly issues updated at or after this time are returned.\n')




class LegacyIssuesSearchOwnerRepositoryStateKeywordInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            keyword = fields.String(description='The search term.')
            state = fields.String(description='Indicates the state of the issues to return. Can be either open or closed.', validate=[OneOf(choices=['open', 'closed'], labels=[])])
            owner = fields.String()
            repository = fields.String()




class LegacyReposSearchKeywordInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            keyword = fields.String(description='The search term')

        class Query(Schema):
            order = fields.String(description='The sort field. if sort param is provided. Can be either asc or desc.', missing=lambda: 'desc', validate=[OneOf(choices=['desc', 'asc'], labels=[])])
            language = fields.String(description='Filter results by language')
            start_page = fields.String(description='The page number to fetch')
            sort = fields.String(description='The sort field. One of stars, forks, or updated. Default: results are sorted by best match.', validate=[OneOf(choices=['updated', 'stars', 'forks'], labels=[])])




class LegacyUserEmailEmailInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            email = fields.String(description='The email address')




class LegacyUserSearchKeywordInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            keyword = fields.String(description='The search term')

        class Query(Schema):
            order = fields.String(description='The sort field. if sort param is provided. Can be either asc or desc.', missing=lambda: 'desc', validate=[OneOf(choices=['desc', 'asc'], labels=[])])
            start_page = fields.String(description='The page number to fetch')
            sort = fields.String(description='The sort field. One of stars, forks, or updated. Default: results are sorted by best match.', validate=[OneOf(choices=['updated', 'stars', 'forks'], labels=[])])




class MarkdownInput(object):
    class Post(object):
        class Body(Markdown):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class MarkdownRawInput(object):
    class Post(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class MetaInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class NetworksOwnerRepoEventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of the owner.')
            repo = fields.String(description='Name of repository.')




class NotificationsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            all = fields.Boolean(description='True to show notifications marked as read.')
            participating = fields.Boolean(description='True to show only notifications in which the user is directly participating\nor mentioned.\n')
            since = fields.String(description='The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nExample: "2012-10-09T23:39:01Z".\n')


    class Put(object):
        class Body(NotificationMarkRead):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class NotificationsThreadsIdInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of thread.')


    class Patch(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of thread.')




class NotificationsThreadsIdSubscriptionInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of thread.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of thread.')


    class Put(object):
        class Body(PutSubscription):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            id = fields.Integer(description='Id of thread.')




class OrgsOrgInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')


    class Patch(object):
        class Body(PatchOrg):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')




class OrgsOrgEventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')




class OrgsOrgIssuesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')

        class Query(Schema):
            filter = fields.String(description="Issues assigned to you / created by you / mentioning you / you're\nsubscribed to updates for / All issues the authenticated user can see\n", missing=lambda: 'all', validate=[OneOf(choices=['assigned', 'created', 'mentioned', 'subscribed', 'all'], labels=[])])
            state = fields.String(missing=lambda: 'open', validate=[OneOf(choices=['open', 'closed'], labels=[])])
            labels = fields.String(description='String list of comma separated Label names. Example - bug,ui,@high.')
            sort = fields.String(missing=lambda: 'created', validate=[OneOf(choices=['created', 'updated', 'comments'], labels=[])])
            direction = fields.String(missing=lambda: 'desc', validate=[OneOf(choices=['asc', 'desc'], labels=[])])
            since = fields.String(description='Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nOnly issues updated at or after this time are returned.\n')




class OrgsOrgMembersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')




class OrgsOrgMembersUsernameInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')
            username = fields.String(description='Name of the user.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')
            username = fields.String(description='Name of the user.')




class OrgsOrgPublicMembersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')




class OrgsOrgPublicMembersUsernameInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')
            username = fields.String(description='Name of the user.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')
            username = fields.String(description='Name of the user.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')
            username = fields.String(description='Name of the user.')




class OrgsOrgReposInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')

        class Query(Schema):
            type = fields.String(missing=lambda: 'all', validate=[OneOf(choices=['all', 'public', 'private', 'forks', 'sources', 'member'], labels=[])])


    class Post(object):
        class Body(PostRepo):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')




class OrgsOrgTeamsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')


    class Post(object):
        class Body(OrgTeamsPost):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            org = fields.String(description='Name of organisation.')




class RateLimitInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class ReposOwnerRepoInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Patch(object):
        class Body(RepoEdit):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoAssigneesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoAssigneesAssigneeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            assignee = fields.String(description='Login of the assignee.')




class ReposOwnerRepoBranchesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoBranchesBranchInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            branch = fields.String(description='Name of the branch.')




class ReposOwnerRepoCollaboratorsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoCollaboratorsUserInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            user = fields.String(description='Login of the user.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            user = fields.String(description='Login of the user.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            user = fields.String(description='Login of the user.')




class ReposOwnerRepoCommentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoCommentsCommentIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='Id of comment.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='Id of comment.')


    class Patch(object):
        class Body(CommentBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='Id of comment.')




class ReposOwnerRepoCommitsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            since = fields.String(description='The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nExample: "2012-10-09T23:39:01Z".\n')
            sha = fields.String(description='Sha or branch to start listing commits from.')
            path = fields.String(description='Only commits containing this file path will be returned.')
            author = fields.String(description='GitHub login, name, or email by which to filter by commit author.')
            until = fields.String(description='ISO 8601 Date - Only commits before this date will be returned.')




class ReposOwnerRepoCommitsRefStatusInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            ref = fields.String()




class ReposOwnerRepoCommitsShaCodeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            shaCode = fields.String(description='SHA-1 code of the commit.')




class ReposOwnerRepoCommitsShaCodeCommentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            shaCode = fields.String(description='SHA-1 code of the commit.')


    class Post(object):
        class Body(CommitBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            shaCode = fields.String(description='SHA-1 code of the commit.')




class ReposOwnerRepoCompareBaseIdheadIdInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            baseId = fields.String()
            headId = fields.String()




class ReposOwnerRepoContentsPathInput(object):
    class Delete(object):
        class Body(DeleteFileBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            path = fields.String()


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            path = fields.String()

        class Query(Schema):
            path = fields.String(description='The content path.')
            ref = fields.String(description="The String name of the Commit/Branch/Tag. Defaults to 'master'.")


    class Put(object):
        class Body(CreateFileBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            path = fields.String()




class ReposOwnerRepoContributorsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            anon = fields.String(description='Set to 1 or true to include anonymous contributors in results.')




class ReposOwnerRepoDeploymentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Post(object):
        class Body(Deployment):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoDeploymentsIdStatusesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.Integer(description='The Deployment ID to list the statuses from.')


    class Post(object):
        class Body(Deployment_statuses_create):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.Integer(description='The Deployment ID to list the statuses from.')




class ReposOwnerRepoDownloadsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoDownloadsDownloadIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            downloadId = fields.Integer(description='Id of download.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            downloadId = fields.Integer(description='Id of download.')




class ReposOwnerRepoEventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoForksInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            sort = fields.String(missing=lambda: 'newes', validate=[OneOf(choices=['newes', 'oldes', 'watchers'], labels=[])])


    class Post(object):
        class Body(ForkBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoGitBlobsInput(object):
    class Post(object):
        class Body(Blob):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoGitBlobsShaCodeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            shaCode = fields.String(description='SHA-1 code.')




class ReposOwnerRepoGitCommitsInput(object):
    class Post(object):
        class Body(RepoCommitBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoGitCommitsShaCodeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            shaCode = fields.String(description='SHA-1 code.')




class ReposOwnerRepoGitRefsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Post(object):
        class Body(RefsBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoGitRefsRefInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            ref = fields.String()


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            ref = fields.String()


    class Patch(object):
        class Body(GitRefPatch):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            ref = fields.String()




class ReposOwnerRepoGitTagsInput(object):
    class Post(object):
        class Body(Tag):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoGitTagsShaCodeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            shaCode = fields.String()




class ReposOwnerRepoGitTreesInput(object):
    class Post(object):
        class Body(Tree):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoGitTreesShaCodeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            shaCode = fields.String(description='Tree SHA.')

        class Query(Schema):
            recursive = fields.Integer(description='Get a Tree Recursively. (0 or 1)')




class ReposOwnerRepoHooksInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Post(object):
        class Body(HookBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoHooksHookIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            hookId = fields.Integer(description='Id of hook.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            hookId = fields.Integer(description='Id of hook.')


    class Patch(object):
        class Body(HookBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            hookId = fields.Integer(description='Id of hook.')




class ReposOwnerRepoHooksHookIdTestsInput(object):
    class Post(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            hookId = fields.Integer(description='Id of hook.')




class ReposOwnerRepoIssuesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            filter = fields.String(description="Issues assigned to you / created by you / mentioning you / you're\nsubscribed to updates for / All issues the authenticated user can see\n", missing=lambda: 'all', validate=[OneOf(choices=['assigned', 'created', 'mentioned', 'subscribed', 'all'], labels=[])])
            state = fields.String(missing=lambda: 'open', validate=[OneOf(choices=['open', 'closed'], labels=[])])
            labels = fields.String(description='String list of comma separated Label names. Example - bug,ui,@high.')
            sort = fields.String(missing=lambda: 'created', validate=[OneOf(choices=['created', 'updated', 'comments'], labels=[])])
            direction = fields.String(missing=lambda: 'desc', validate=[OneOf(choices=['asc', 'desc'], labels=[])])
            since = fields.String(description='Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nOnly issues updated at or after this time are returned.\n')


    class Post(object):
        class Body(Issue):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoIssuesCommentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            direction = fields.String(description="Ignored without 'sort' parameter.")
            sort = fields.String(description='', validate=[OneOf(choices=['created', 'updated'], labels=[])])
            since = fields.String(description='The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nExample: "2012-10-09T23:39:01Z".\n')




class ReposOwnerRepoIssuesCommentsCommentIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='ID of comment.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='ID of comment.')


    class Patch(object):
        class Body(CommentBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='ID of comment.')




class ReposOwnerRepoIssuesEventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoIssuesEventsEventIdInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            eventId = fields.Integer(description='Id of the event.')




class ReposOwnerRepoIssuesNumberInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Patch(object):
        class Body(Issue):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')




class ReposOwnerRepoIssuesNumberCommentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Post(object):
        class Body(CommentBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')




class ReposOwnerRepoIssuesNumberEventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')




class ReposOwnerRepoIssuesNumberLabelsInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Post(object):
        class Body(PrimitiveValueSchema):
            v = fields.String()

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Put(object):
        class Body(PrimitiveValueSchema):
            v = fields.String()

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')




class ReposOwnerRepoIssuesNumberLabelsNameInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')
            name = fields.String(description='Name of the label.')




class ReposOwnerRepoKeysInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Post(object):
        class Body(User_keys_post):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoKeysKeyIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            keyId = fields.Integer(description='Id of key.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            keyId = fields.Integer(description='Id of key.')




class ReposOwnerRepoLabelsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Post(object):
        class Body(PrimitiveValueSchema):
            v = fields.String()

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoLabelsNameInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            name = fields.String(description='Name of the label.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            name = fields.String(description='Name of the label.')


    class Patch(object):
        class Body(PrimitiveValueSchema):
            v = fields.String()

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            name = fields.String(description='Name of the label.')




class ReposOwnerRepoLanguagesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoMergesInput(object):
    class Post(object):
        class Body(MergesBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoMilestonesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            state = fields.String(description='String to filter by state.', missing=lambda: 'open', validate=[OneOf(choices=['open', 'closed'], labels=[])])
            direction = fields.String(description="Ignored without 'sort' parameter.")
            sort = fields.String(description='', missing=lambda: 'due_date', validate=[OneOf(choices=['due_date', 'completeness'], labels=[])])


    class Post(object):
        class Body(MilestoneUpdate):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoMilestonesNumberInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of milestone.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of milestone.')


    class Patch(object):
        class Body(MilestoneUpdate):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of milestone.')




class ReposOwnerRepoMilestonesNumberLabelsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of milestone.')




class ReposOwnerRepoNotificationsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            all = fields.Boolean(description='True to show notifications marked as read.')
            participating = fields.Boolean(description='True to show only notifications in which the user is directly participating\nor mentioned.\n')
            since = fields.String(description='The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nExample: "2012-10-09T23:39:01Z".\n')


    class Put(object):
        class Body(NotificationMarkRead):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoPullsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            state = fields.String(description='String to filter by state.', missing=lambda: 'open', validate=[OneOf(choices=['open', 'closed'], labels=[])])
            head = fields.String(description="Filter pulls by head user and branch name in the format of 'user:ref-name'.\nExample: github:new-script-format.\n")
            base = fields.String(description='Filter pulls by base branch name. Example - gh-pages.')


    class Post(object):
        class Body(PullsPost):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoPullsCommentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            direction = fields.String(description="Ignored without 'sort' parameter.")
            sort = fields.String(description='', validate=[OneOf(choices=['created', 'updated'], labels=[])])
            since = fields.String(description='The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nExample: "2012-10-09T23:39:01Z".\n')




class ReposOwnerRepoPullsCommentsCommentIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='Id of comment.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='Id of comment.')


    class Patch(object):
        class Body(CommentBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            commentId = fields.Integer(description='Id of comment.')




class ReposOwnerRepoPullsNumberInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')


    class Patch(object):
        class Body(PullUpdate):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')




class ReposOwnerRepoPullsNumberCommentsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')


    class Post(object):
        class Body(PullsCommentPost):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')




class ReposOwnerRepoPullsNumberCommitsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')




class ReposOwnerRepoPullsNumberFilesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')




class ReposOwnerRepoPullsNumberMergeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')


    class Put(object):
        class Body(MergePullBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Id of pull.')




class ReposOwnerRepoReadmeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')

        class Query(Schema):
            ref = fields.String(description='The String name of the Commit/Branch/Tag. Defaults to master.')




class ReposOwnerRepoReleasesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Post(object):
        class Body(Release_create):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoReleasesAssetsIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.String()


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.String()


    class Patch(object):
        class Body(AssetPatch):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.String()




class ReposOwnerRepoReleasesIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.String()


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.String()


    class Patch(object):
        class Body(Release_create):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.String()




class ReposOwnerRepoReleasesIdAssetsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            id = fields.String()




class ReposOwnerRepoStargazersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoStatsCodeFrequencyInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoStatsCommitActivityInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoStatsContributorsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoStatsParticipationInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoStatsPunchCardInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoStatusesRefInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            ref = fields.String(description='Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.\n')


    class Post(object):
        class Body(HeadBranch):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            ref = fields.String(description='Ref to list the statuses from. It can be a SHA, a branch name, or a tag name.\n')




class ReposOwnerRepoSubscribersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoSubscriptionInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')


    class Put(object):
        class Body(SubscribitionBody):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoTagsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoTeamsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoWatchersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')




class ReposOwnerRepoArchiveFormatPathInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            archive_format = fields.String(validate=[OneOf(choices=['tarball', 'zipball'], labels=[])])
            path = fields.String(description="Valid Git reference, defaults to 'master'.")




class RepositoriesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            since = fields.String(description='The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nExample: "2012-10-09T23:39:01Z".\n')




class SearchCodeInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            order = fields.String(description='The sort field. if sort param is provided. Can be either asc or desc.', missing=lambda: 'desc', validate=[OneOf(choices=['desc', 'asc'], labels=[])])
            q = fields.String(description="The search terms. This can be any combination of the supported code\nsearch parameters:\n'Search In' Qualifies which fields are searched. With this qualifier\nyou can restrict the search to just the file contents, the file path,\nor both.\n'Languages' Searches code based on the language it's written in.\n'Forks' Filters repositories based on the number of forks, and/or\nwhether code from forked repositories should be included in the results\nat all.\n'Size' Finds files that match a certain size (in bytes).\n'Path' Specifies the path that the resulting file must be at.\n'Extension' Matches files with a certain extension.\n'Users' or 'Repositories' Limits searches to a specific user or repository.\n")
            sort = fields.String(description="Can only be 'indexed', which indicates how recently a file has been indexed\nby the GitHub search infrastructure. If not provided, results are sorted\nby best match.\n", validate=[OneOf(choices=['indexed'], labels=[])])




class SearchIssuesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            order = fields.String(description='The sort field. if sort param is provided. Can be either asc or desc.', missing=lambda: 'desc', validate=[OneOf(choices=['desc', 'asc'], labels=[])])
            q = fields.String(description='The q search term can also contain any combination of the supported issue search qualifiers:')
            sort = fields.String(description='The sort field. Can be comments, created, or updated. Default: results are sorted by best match.', validate=[OneOf(choices=['updated', 'created', 'comments'], labels=[])])




class SearchRepositoriesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            order = fields.String(description='The sort field. if sort param is provided. Can be either asc or desc.', missing=lambda: 'desc', validate=[OneOf(choices=['desc', 'asc'], labels=[])])
            q = fields.String(description="The search terms. This can be any combination of the supported repository\nsearch parameters:\n'Search In' Qualifies which fields are searched. With this qualifier you\ncan restrict the search to just the repository name, description, readme,\nor any combination of these.\n'Size' Finds repositories that match a certain size (in kilobytes).\n'Forks' Filters repositories based on the number of forks, and/or whether\nforked repositories should be included in the results at all.\n'Created' and 'Last Updated' Filters repositories based on times of\ncreation, or when they were last updated.\n'Users or Repositories' Limits searches to a specific user or repository.\n'Languages' Searches repositories based on the language they are written in.\n'Stars' Searches repositories based on the number of stars.\n")
            sort = fields.String(description='If not provided, results are sorted by best match.', validate=[OneOf(choices=['stars', 'forks', 'updated'], labels=[])])




class SearchUsersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            order = fields.String(description='The sort field. if sort param is provided. Can be either asc or desc.', missing=lambda: 'desc', validate=[OneOf(choices=['desc', 'asc'], labels=[])])
            q = fields.String(description="The search terms. This can be any combination of the supported user\nsearch parameters:\n'Search In' Qualifies which fields are searched. With this qualifier you\ncan restrict the search to just the username, public email, full name,\nlocation, or any combination of these.\n'Repository count' Filters users based on the number of repositories they\nhave.\n'Location' Filter users by the location indicated in their profile.\n'Language' Search for users that have repositories that match a certain\nlanguage.\n'Created' Filter users based on when they joined.\n'Followers' Filter users based on the number of followers they have.\n")
            sort = fields.String(description='If not provided, results are sorted by best match.', validate=[OneOf(choices=['followers', 'repositories', 'joined'], labels=[])])




class TeamsTeamIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')


    class Patch(object):
        class Body(EditTeam):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')




class TeamsTeamIdMembersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')




class TeamsTeamIdMembersUsernameInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            username = fields.String(description='Name of a member.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            username = fields.String(description='Name of a member.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            username = fields.String(description='Name of a member.')




class TeamsTeamIdMembershipsUsernameInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            username = fields.String(description='Name of a member.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            username = fields.String(description='Name of a member.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            username = fields.String(description='Name of a member.')




class TeamsTeamIdReposInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')




class TeamsTeamIdReposOrgRepoInput(object):
    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            org = fields.String(description='Name of a organization.')
            repo = fields.String(description='Name of a repository.')




class TeamsTeamIdReposOwnerRepoInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            owner = fields.String(description='Name of a repository owner.')
            repo = fields.String(description='Name of a repository.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            teamId = fields.Integer(description='Id of team.')
            owner = fields.String(description='Name of a repository owner.')
            repo = fields.String(description='Name of a repository.')




class UserInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')


    class Patch(object):
        class Body(User_update):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserEmailsInput(object):
    class Delete(object):
        class Body(PrimitiveValueSchema):
            v = fields.String()

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')


    class Post(object):
        class Body(PrimitiveValueSchema):
            v = fields.String()

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserFollowersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserFollowingInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserFollowingUsernameInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UserIssuesInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            filter = fields.String(description="Issues assigned to you / created by you / mentioning you / you're\nsubscribed to updates for / All issues the authenticated user can see\n", missing=lambda: 'all', validate=[OneOf(choices=['assigned', 'created', 'mentioned', 'subscribed', 'all'], labels=[])])
            state = fields.String(missing=lambda: 'open', validate=[OneOf(choices=['open', 'closed'], labels=[])])
            labels = fields.String(description='String list of comma separated Label names. Example - bug,ui,@high.')
            sort = fields.String(missing=lambda: 'created', validate=[OneOf(choices=['created', 'updated', 'comments'], labels=[])])
            direction = fields.String(missing=lambda: 'desc', validate=[OneOf(choices=['asc', 'desc'], labels=[])])
            since = fields.String(description='Optional string of a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nOnly issues updated at or after this time are returned.\n')




class UserKeysInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')


    class Post(object):
        class Body(User_keys_post):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserKeysKeyIdInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            keyId = fields.Integer(description='ID of key.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            keyId = fields.Integer(description='ID of key.')




class UserOrgsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserReposInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            type = fields.String(missing=lambda: 'all', validate=[OneOf(choices=['all', 'public', 'private', 'forks', 'sources', 'member'], labels=[])])


    class Post(object):
        class Body(PostRepo):
            pass

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserStarredInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            direction = fields.String(description="Ignored without 'sort' parameter.")
            sort = fields.String(description='', missing=lambda: 'created', validate=[OneOf(choices=['created', 'updated'], labels=[])])




class UserStarredOwnerRepoInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of a repository owner.')
            repo = fields.String(description='Name of a repository.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of a repository owner.')
            repo = fields.String(description='Name of a repository.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of a repository owner.')
            repo = fields.String(description='Name of a repository.')




class UserSubscriptionsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UserSubscriptionsOwnerRepoInput(object):
    class Delete(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of the owner.')
            repo = fields.String(description='Name of repository.')


    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of the owner.')
            repo = fields.String(description='Name of repository.')


    class Put(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of the owner.')
            repo = fields.String(description='Name of repository.')




class UserTeamsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')




class UsersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Query(Schema):
            since = fields.Integer(description="The integer ID of the last User that you've seen.")




class UsersUsernameInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameEventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameEventsOrgsOrgInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')
            org = fields.String()




class UsersUsernameFollowersInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameFollowingTargetUserInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')
            targetUser = fields.String(description='Name of user.')




class UsersUsernameGistsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')

        class Query(Schema):
            since = fields.String(description='The time should be passed in as UTC in the ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.\nExample: "2012-10-09T23:39:01Z".\n')




class UsersUsernameKeysInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameOrgsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameReceivedEventsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameReceivedEventsPublicInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameReposInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')

        class Query(Schema):
            type = fields.String(missing=lambda: 'all', validate=[OneOf(choices=['all', 'public', 'private', 'forks', 'sources', 'member'], labels=[])])




class UsersUsernameStarredInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class UsersUsernameSubscriptionsInput(object):
    class Get(object):
        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            username = fields.String(description='Name of user.')




class EmojisOutput(object):
    class Get200(Emojis):
        """OK"""
        pass



class EventsOutput(object):
    class Get200(Events):
        """OK"""
        pass



class FeedsOutput(object):
    class Get200(Feeds):
        """OK"""
        pass



class GistsOutput(object):
    class Get200(GistsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Gist):
        """Created"""
        pass



class GistsPublicOutput(object):
    class Get200(GistsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class GistsStarredOutput(object):
    class Get200(GistsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class GistsIdOutput(object):
    class Get200(Gist):
        """OK"""
        pass

    class Patch200(Gist):
        """OK"""
        pass



class GistsIdCommentsOutput(object):
    class Get200(CommentsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Comment):
        """Created"""
        pass



class GistsIdCommentsCommentIdOutput(object):
    class Get200(Comment):
        """OK"""
        pass

    class Patch200(Comment):
        """OK"""
        pass



class GitignoreTemplatesOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Field()



class GitignoreTemplatesLanguageOutput(object):
    class Get200(Gitignore_lang):
        """OK"""
        pass



class IssuesOutput(object):
    class Get200(IssuesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class LegacyIssuesSearchOwnerRepositoryStateKeywordOutput(object):
    class Get200(Search_issues_by_keyword):
        """OK"""
        pass



class LegacyReposSearchKeywordOutput(object):
    class Get200(Search_repositories_by_keyword):
        """OK"""
        pass



class LegacyUserEmailEmailOutput(object):
    class Get200(Search_user_by_email):
        """OK"""
        pass



class LegacyUserSearchKeywordOutput(object):
    class Get200(Search_users_by_keyword):
        """OK"""
        pass



class MetaOutput(object):
    class Get200(Meta):
        """OK"""
        pass



class NetworksOwnerRepoEventsOutput(object):
    class Get200(Events):
        """OK"""
        pass



class NotificationsOutput(object):
    class Get200(Notifications):
        """OK"""
        pass



class NotificationsThreadsIdOutput(object):
    class Get200(Notifications):
        """OK"""
        pass



class NotificationsThreadsIdSubscriptionOutput(object):
    class Get200(Subscription):
        """OK"""
        pass

    class Put200(Subscription):
        """OK"""
        pass



class OrgsOrgOutput(object):
    class Get200(Organization):
        """OK"""
        pass

    class Patch200(Organization):
        """OK"""
        pass



class OrgsOrgEventsOutput(object):
    class Get200(Events):
        """OK"""
        pass



class OrgsOrgIssuesOutput(object):
    class Get200(IssuesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class OrgsOrgMembersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class OrgsOrgPublicMembersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class OrgsOrgReposOutput(object):
    class Get200(ReposItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(ReposItem):
        """Created"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class OrgsOrgTeamsOutput(object):
    class Get200(TeamsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Team):
        """Created"""
        pass



class RateLimitOutput(object):
    class Get200(Rate_limit):
        """OK"""
        pass



class ReposOwnerRepoOutput(object):
    class Get200(Repo):
        """OK"""
        pass

    class Patch200(Repo):
        """OK"""
        pass



class ReposOwnerRepoAssigneesOutput(object):
    class Get200(AssigneesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoBranchesOutput(object):
    class Get200(BranchesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoBranchesBranchOutput(object):
    class Get200(Branch):
        """OK"""
        pass



class ReposOwnerRepoCollaboratorsOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoCommentsOutput(object):
    class Get200(RepoCommentsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoCommentsCommentIdOutput(object):
    class Get200(CommitComments):
        """OK"""
        pass

    class Patch200(CommitComments):
        """OK"""
        pass



class ReposOwnerRepoCommitsOutput(object):
    class Get200(CommitsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoCommitsRefStatusOutput(object):
    class Get200(RefStatusItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoCommitsShaCodeOutput(object):
    class Get200(Commit):
        """OK"""
        pass



class ReposOwnerRepoCommitsShaCodeCommentsOutput(object):
    class Get200(RepoCommentsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(CommitComments):
        """Created"""
        pass



class ReposOwnerRepoCompareBaseIdheadIdOutput(object):
    class Get200(Compare_commits):
        """OK"""
        pass



class ReposOwnerRepoContentsPathOutput(object):
    class Delete200(DeleteFile):
        """OK"""
        pass

    class Get200(Contents_path):
        """OK"""
        pass

    class Put200(CreateFile):
        """OK"""
        pass



class ReposOwnerRepoContributorsOutput(object):
    class Get200(ContributorsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoDeploymentsOutput(object):
    class Get200(Repo_deploymentsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Deployment_resp):
        """Created"""
        pass



class ReposOwnerRepoDeploymentsIdStatusesOutput(object):
    class Get200(Deployment_statusesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoDownloadsOutput(object):
    class Get200(Downloads):
        """OK"""
        pass



class ReposOwnerRepoDownloadsDownloadIdOutput(object):
    class Get200(Downloads):
        """OK"""
        pass



class ReposOwnerRepoEventsOutput(object):
    class Get200(Events):
        """OK"""
        pass



class ReposOwnerRepoForksOutput(object):
    class Get200(ForksItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Fork):
        """Created"""
        pass



class ReposOwnerRepoGitBlobsOutput(object):
    class Post201(Blobs):
        """Created"""
        pass



class ReposOwnerRepoGitBlobsShaCodeOutput(object):
    class Get200(Blob):
        """OK"""
        pass



class ReposOwnerRepoGitCommitsOutput(object):
    class Post201(GitCommit):
        """Created"""
        pass



class ReposOwnerRepoGitCommitsShaCodeOutput(object):
    class Get200(RepoCommit):
        """OK"""
        pass



class ReposOwnerRepoGitRefsOutput(object):
    class Get200(RefsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(HeadBranch):
        """Created"""
        pass



class ReposOwnerRepoGitRefsRefOutput(object):
    class Get200(HeadBranch):
        """OK"""
        pass

    class Patch200(HeadBranch):
        """OK"""
        pass



class ReposOwnerRepoGitTagsOutput(object):
    class Post201(Tags):
        """Created"""
        pass



class ReposOwnerRepoGitTagsShaCodeOutput(object):
    class Get200(Tag):
        """OK"""
        pass



class ReposOwnerRepoGitTreesOutput(object):
    class Post201(Trees):
        """Created"""
        pass



class ReposOwnerRepoGitTreesShaCodeOutput(object):
    class Get200(Tree):
        """OK"""
        pass



class ReposOwnerRepoHooksOutput(object):
    class Get200(HookItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(HookItem):
        """Created"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoHooksHookIdOutput(object):
    class Get200(HookItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Patch200(HookItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoIssuesOutput(object):
    class Get200(IssuesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Issue):
        """Created"""
        pass



class ReposOwnerRepoIssuesCommentsOutput(object):
    class Get200(IssuesCommentsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoIssuesCommentsCommentIdOutput(object):
    class Get200(IssuesComment):
        """OK"""
        pass

    class Patch200(IssuesComment):
        """OK"""
        pass



class ReposOwnerRepoIssuesEventsOutput(object):
    class Get200(Events):
        """OK"""
        pass



class ReposOwnerRepoIssuesEventsEventIdOutput(object):
    class Get200(Event):
        """OK"""
        pass



class ReposOwnerRepoIssuesNumberOutput(object):
    class Get200(Issue):
        """OK"""
        pass

    class Patch200(Issue):
        """OK"""
        pass



class ReposOwnerRepoIssuesNumberCommentsOutput(object):
    class Get200(IssuesCommentsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(IssuesComment):
        """Created"""
        pass



class ReposOwnerRepoIssuesNumberEventsOutput(object):
    class Get200(Events):
        """OK"""
        pass



class ReposOwnerRepoIssuesNumberLabelsOutput(object):
    class Get200(LabelsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Label):
        """Created"""
        pass

    class Put201(Label):
        """Created"""
        pass



class ReposOwnerRepoKeysOutput(object):
    class Get200(KeysItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(User_keys_keyId):
        """Created"""
        pass



class ReposOwnerRepoKeysKeyIdOutput(object):
    class Get200(User_keys_keyId):
        """OK"""
        pass



class ReposOwnerRepoLabelsOutput(object):
    class Get200(LabelsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Label):
        """Created"""
        pass



class ReposOwnerRepoLabelsNameOutput(object):
    class Get200(Label):
        """OK"""
        pass

    class Patch200(Label):
        """OK"""
        pass



class ReposOwnerRepoLanguagesOutput(object):
    class Get200(Languages):
        """OK"""
        pass



class ReposOwnerRepoMergesOutput(object):
    class Post201(MergesSuccessful):
        """Successful Response (The resulting merge commit)"""
        pass

    class Post404(MergesConflict):
        """Missing base response or missing head response"""
        pass

    class Post409(MergesConflict):
        """Merge conflict response."""
        pass



class ReposOwnerRepoMilestonesOutput(object):
    class Get200(Milestone):
        """OK"""
        pass

    class Post201(Milestone):
        """Created"""
        pass



class ReposOwnerRepoMilestonesNumberOutput(object):
    class Get200(Milestone):
        """OK"""
        pass

    class Patch200(Milestone):
        """OK"""
        pass



class ReposOwnerRepoMilestonesNumberLabelsOutput(object):
    class Get200(LabelsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoNotificationsOutput(object):
    class Get200(Notifications):
        """OK"""
        pass



class ReposOwnerRepoPullsOutput(object):
    class Get200(PullsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(PullsItem):
        """Created"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoPullsCommentsOutput(object):
    class Get200(IssuesCommentsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoPullsCommentsCommentIdOutput(object):
    class Get200(PullsComment):
        """OK"""
        pass

    class Patch200(PullsComment):
        """OK"""
        pass



class ReposOwnerRepoPullsNumberOutput(object):
    class Get200(PullRequest):
        """OK"""
        pass

    class Patch200(Repo):
        """OK"""
        pass



class ReposOwnerRepoPullsNumberCommentsOutput(object):
    class Get200(PullsComment):
        """OK"""
        pass

    class Post201(PullsComment):
        """Created"""
        pass



class ReposOwnerRepoPullsNumberCommitsOutput(object):
    class Get200(CommitsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoPullsNumberFilesOutput(object):
    class Get200(PullsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoPullsNumberMergeOutput(object):
    class Put200(Merge):
        """Response if merge was successful."""
        pass

    class Put405(Merge):
        """Response if merge cannot be performed."""
        pass



class ReposOwnerRepoReadmeOutput(object):
    class Get200(Contents_path):
        """OK"""
        pass



class ReposOwnerRepoReleasesOutput(object):
    class Get200(ReleasesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Release):
        """Created"""
        pass



class ReposOwnerRepoReleasesAssetsIdOutput(object):
    class Get200(Asset):
        """OK"""
        pass

    class Patch200(Asset):
        """OK"""
        pass



class ReposOwnerRepoReleasesIdOutput(object):
    class Get200(Release):
        """OK"""
        pass

    class Patch200(Release):
        """OK"""
        pass



class ReposOwnerRepoReleasesIdAssetsOutput(object):
    class Get200(AssetsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoStargazersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoStatsCodeFrequencyOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Integer()



class ReposOwnerRepoStatsCommitActivityOutput(object):
    class Get200(CommitActivityStatsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoStatsContributorsOutput(object):
    class Get200(ContributorsStatsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoStatsParticipationOutput(object):
    class Get200(ParticipationStats):
        """OK"""
        pass



class ReposOwnerRepoStatsPunchCardOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Integer()



class ReposOwnerRepoStatusesRefOutput(object):
    class Get200(RefItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(RefItem):
        """Created"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoSubscribersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoSubscriptionOutput(object):
    class Get200(Subscribition):
        """OK"""
        pass

    class Put200(Subscribition):
        """OK"""
        pass



class ReposOwnerRepoTagsOutput(object):
    class Get200(Tags):
        """OK"""
        pass



class ReposOwnerRepoTeamsOutput(object):
    class Get200(TeamsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class ReposOwnerRepoWatchersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class RepositoriesOutput(object):
    class Get200(RepositoriesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class SearchCodeOutput(object):
    class Get200(Search_code):
        """OK"""
        pass



class SearchIssuesOutput(object):
    class Get200(Search_issues):
        """OK"""
        pass



class SearchRepositoriesOutput(object):
    class Get200(Search_repositories):
        """OK"""
        pass



class SearchUsersOutput(object):
    class Get200(Search_users):
        """OK"""
        pass



class TeamsTeamIdOutput(object):
    class Get200(Team):
        """OK"""
        pass

    class Patch200(Team):
        """OK"""
        pass



class TeamsTeamIdMembersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class TeamsTeamIdMembersUsernameOutput(object):
    class Put422(OrganizationAsTeamMember):
        """If you attempt to add an organization to a team, you will get this."""
        pass



class TeamsTeamIdMembershipsUsernameOutput(object):
    class Get200(TeamMembership):
        """User is a member."""
        pass

    class Put200(TeamMembership):
        """Team member added."""
        pass

    class Put422(OrganizationAsTeamMember):
        """If you attempt to add an organization to a team, you will get this."""
        pass



class TeamsTeamIdReposOutput(object):
    class Get200(TeamReposItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UserOutput(object):
    class Get200(User):
        """OK"""
        pass

    class Patch200(User):
        """OK"""
        pass



class UserEmailsOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.String()



class UserFollowersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UserFollowingOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UserIssuesOutput(object):
    class Get200(IssuesItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UserKeysOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Field()

    class Post201(User_keys_keyId):
        """Created"""
        pass



class UserKeysKeyIdOutput(object):
    class Get200(User_keys_keyId):
        """OK"""
        pass



class UserOrgsOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Field()



class UserReposOutput(object):
    class Get200(ReposItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(ReposItem):
        """Created"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UserStarredOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Field()



class UserSubscriptionsOutput(object):
    class Get200(User_userId_subscribitionsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UserTeamsOutput(object):
    class Get200(Teams_listItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UsersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UsersUsernameOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UsersUsernameFollowersOutput(object):
    class Get200(UsersItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UsersUsernameGistsOutput(object):
    class Get200(GistsItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class UsersUsernameKeysOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Field()



class UsersUsernameOrgsOutput(object):
    class Get200(PrimitiveValueSchema):
        v = fields.Field()



class UsersUsernameReposOutput(object):
    class Get200(ReposItem):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)
