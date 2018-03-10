import requests
import json

def getUserID():
    userID = input('Enter a GitHub User ID: ')
    return userID

def getCommits(userID, repos):
    commits = []
    for i in repos:
        r = requests.get('https://api.github.com/repos/' + userID + '/' + i + '/commits')
        r = r.json()
        commits.append(len(r))
    return commits


def getRepos(userID):
    r = requests.get('https://api.github.com/users/' + userID + '/repos')
    r = r.json()
    repos = []
    for i in r:
        #print(i['name'])
        repos.append(i['name'])
    return repos


if __name__ == '__main__':
    userID = getUserID()
    repos = getRepos(userID)
    commits = getCommits(userID, repos)

    print('User: ' + userID)
    j = 0
    for i in repos:
        print('Repo: ' + i + ' Number of Commits: ' + str(commits[j]))
        j += 1
