import sys
import json
from githubschema import Repo, Emojis


d = json.loads("""{
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "created_at": "2011-01-26T19:01:12Z",
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
    "gravatar_id": "somehexcode",
    "id": 1,
    "login": "octocat",
    "type": "Organization",
    "url": "https://api.github.com/users/octocat"
  },
  "owner": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "somehexcode",
    "id": 1,
    "login": "octocat",
    "url": "https://api.github.com/users/octocat"
  },
  "parent": {
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "created_at": "2011-01-26T19:01:12Z",
    "description": "This your first repo!",
    "fork": true,
    "forks_count": 9,
    "full_name": "octocat/Hello-World",
    "git_url": "git://github.com/octocat/Hello-World.git",
    "homepage": "https://github.com",
    "html_url": "https://github.com/octocat/Hello-World",
    "id": 1296269,
    "language": "",
    "mirror_url": "git://git.example.com/octocat/Hello-World",
    "name": "Hello-World",
    "open_issues_count": 0,
    "owner": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "somehexcode",
      "id": 1,
      "login": "octocat",
      "url": "https://api.github.com/users/octocat"
    },
    "private": false,
    "pushed_at": "2011-01-26T19:06:43Z",
    "size": 108,
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "updated_at": "2011-01-26T19:14:43Z",
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "watchers_count": 80
  },
  "private": false,
  "pushed_at": "2011-01-26T19:06:43Z",
  "size": 108,
  "source": {
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "created_at": "2011-01-26T19:01:12Z",
    "description": "This your first repo!",
    "fork": true,
    "forks_count": 9,
    "full_name": "octocat/Hello-World",
    "git_url": "git://github.com/octocat/Hello-World.git",
    "homepage": "https://github.com",
    "html_url": "https://github.com/octocat/Hello-World",
    "id": 1296269,
    "language": "",
    "mirror_url": "git://git.example.com/octocat/Hello-World",
    "name": "Hello-World",
    "open_issues_count": 0,
    "owner": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "somehexcode",
      "id": 1,
      "login": "octocat",
      "url": "https://api.github.com/users/octocat"
    },
    "private": false,
    "pushed_at": "2011-01-26T19:06:43Z",
    "size": 108,
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "updated_at": "2011-01-26T19:14:43Z",
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "watchers_count": 80
  },
  "ssh_url": "git@github.com:octocat/Hello-World.git",
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
