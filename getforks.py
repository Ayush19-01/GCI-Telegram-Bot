#Made for the sole purpose of GCI-2019
import requests
session = requests.Session()
def getforks():
    url = f'https://api.github.com/orgs/fedora-infra/repos'
    response = session.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError
def text():
    forks = getforks()
    str1= "Number of repositories is :"+str(len(forks))+"\nNumber of forks of repositories:\n"
    for i in forks:
        str1+=(f"{i['name']}:   {i['forks']} forks\n")
    return str1
def textno():
    l =list()
    forks = getforks()
    for i in forks:
        l.append((f"{i['name']}:   {i['forks']} forks\n"))
    return(l)
def textdict():
    d={}
    forks=getforks()
    for i in forks:
        d[f"{i['name']}"]=f"{i['forks']}"
    return d
