#!/usr/bin/python3
""" 100 - github_commits.py """


if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(sys.argv[2], sys.argv[1]))
    if resp.status_code >= 400:
        print('None')
    else:
        for comment in resp.json()[:10]:
            print("{}: {}".format(comment.get('sha'),
                                  comment.get('commit')
                                         .get('author')
                                         .get('name')))
