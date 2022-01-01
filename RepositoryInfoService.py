import requests
from typing import List
from Repository import Repository
import Constant
from GithubApiException import GithubApiException


def makeRequest(url: str):
    r = requests.get(url , timeout=1)
    if r.status_code != 200:
        raise GithubApiException(r.status_code)
    return r

def getRepositoryList(username:str) -> List[Repository] :

    r = makeRequest('https://api.github.com/users/'+username+'/repos')
    repositoriesInfo = r.json()
    result = [ Repository(repo[Constant.NAME] , repo[Constant.STARGAZERS]) for repo in repositoriesInfo ]
    while len(r.links) > 0 and Constant.NEXT in r.links.keys():
        r = makeRequest(r.links[Constant.NEXT][Constant.URL])
        repositoriesInfo = r.json()
        result = result + [Repository(repo[Constant.NAME] , repo[Constant.STARGAZERS]) for repo in repositoriesInfo]
    return result

def sumStars(repositoriesList: List[Repository]) -> int:
    return sum( repo.stars for repo in repositoriesList)

def getLanguagesInfo(username:str):
    result ={}
    r = makeRequest('https://api.github.com/users/' + username + '/repos')
    repositoriesInfo = r.json()
    languagesUrls = [repo[Constant.LANGUAGE_URL] for repo in repositoriesInfo]
    while len(r.links) > 0 and Constant.NEXT in r.links.keys():
        r = makeRequest(r.links[Constant.NEXT][Constant.URL])
        repositoriesInfo = r.json()
        languagesUrls = languagesUrls + [repo[Constant.LANGUAGE_URL] for repo in repositoriesInfo]
    for url in languagesUrls:
        r = makeRequest(url)
        languageInfo = r.json()
        #print(languageInfo)
        for language , bytes in languageInfo.items():
            if language in result.keys():
                result[language] += bytes
            else:
                result[language] = bytes
    return dict(sorted(result.items(), key=lambda item: item[1] ,reverse=True ))