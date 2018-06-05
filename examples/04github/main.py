import sys
import json
from githubschema import Repo, Emojis


d = json.loads("""{
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "created_at": "2011-01-26T19:01:12Z",
  "default_branch": "master",
  "description": "This your first repo!",
  "fork": false,
  "forks_count": 9,
  "full_name": "octocat/Hello-World",
  "git_url": "git://github.com/octocat/Hello-World.git",
  "has_downloads": true,
  "has_issues": true,
  "has_wiki": true,
  "homepage": "https://github.com",
  "html_url": "https://github.com/octocat/Hello-World",
  "id": 1296269,
  "language": "",
  "mirror_url": "git://git.example.com/octocat/Hello-World",
  "name": "Hello-World",
  "open_issues_count": 0,
  "organization": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "gravatar_id": "somehexcode",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "login": "octocat",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "type": "Organization",
    "url": "https://api.github.com/users/octocat"
  },
  "owner": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "gravatar_id": "somehexcode",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "login": "octocat",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/octocat"
  },
  "parent": {
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "created_at": "2011-01-26T19:01:12Z",
    "default_branch": "master",
    "description": "This your first repo!",
    "fork": true,
    "forks_count": 9,
    "full_name": "octocat/Hello-World",
    "git_url": "git://github.com/octocat/Hello-World.git",
    "has_downloads": true,
    "has_issues": true,
    "has_wiki": true,
    "homepage": "https://github.com",
    "html_url": "https://github.com/octocat/Hello-World",
    "id": 1296269,
    "language": "",
    "mirror_url": "git://git.example.com/octocat/Hello-World",
    "name": "Hello-World",
    "open_issues_count": 0,
    "owner": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "gravatar_id": "somehexcode",
      "html_url": "https://github.com/octocat",
      "id": 1,
      "login": "octocat",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/octocat"
    },
    "permissions": {
      "admin": false,
      "pull": true,
      "push": false
    },
    "private": false,
    "pushed_at": "2011-01-26T19:06:43Z",
    "size": 108,
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_count": 80,
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "updated_at": "2011-01-26T19:14:43Z",
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "watchers_count": 80
  },
  "permissions": {
    "admin": false,
    "pull": true,
    "push": false
  },
  "private": false,
  "pushed_at": "2011-01-26T19:06:43Z",
  "size": 108,
  "source": {
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "created_at": "2011-01-26T19:01:12Z",
    "default_branch": "master",
    "description": "This your first repo!",
    "fork": true,
    "forks_count": 9,
    "full_name": "octocat/Hello-World",
    "git_url": "git://github.com/octocat/Hello-World.git",
    "has_downloads": true,
    "has_issues": true,
    "has_wiki": true,
    "homepage": "https://github.com",
    "html_url": "https://github.com/octocat/Hello-World",
    "id": 1296269,
    "language": "",
    "mirror_url": "git://git.example.com/octocat/Hello-World",
    "name": "Hello-World",
    "open_issues_count": 0,
    "owner": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "gravatar_id": "somehexcode",
      "html_url": "https://github.com/octocat",
      "id": 1,
      "login": "octocat",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/octocat"
    },
    "permissions": {
      "admin": false,
      "pull": true,
      "push": false
    },
    "private": false,
    "pushed_at": "2011-01-26T19:06:43Z",
    "size": 108,
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_count": 80,
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "updated_at": "2011-01-26T19:14:43Z",
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "watchers_count": 80
  },
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_count": 80,
  "subscribers_count": 42,
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "updated_at": "2011-01-26T19:14:43Z",
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "watchers_count": 80
}
""")


if __name__ == "__main__":
    try:
        data = Repo().load(d)
        print("ok", json.dumps(data, indent=2))
    except Exception as e:
        print("ng", e)
        sys.exit(-1)

    try:
        d = {"8ball": "hmm"}
        data = Emojis().load(d)
        print("ok", data, Emojis().dump(data))
    except Exception as e:
        print("ng", e)
        sys.exit(-1)
