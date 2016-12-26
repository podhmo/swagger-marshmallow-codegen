# -*- coding:utf-8 -*-
from marshmallow import(
    Schema,
    fields
)
from marshmallow.validate import(
    Length,
    OneOf
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
