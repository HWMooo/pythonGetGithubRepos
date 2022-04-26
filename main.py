import requests
import asyncio


class Arepo():
    def __init__(self, name, url, stargazers_count, watchers_count, language, forks_count):
        self.name = name
        self.url = url
        self.stargazers_count = stargazers_count
        self.watchers_count = watchers_count
        self.language = language
        self.forks_count = forks_count

    def get_repo(self):
        return self.name, self.url, self.stargazers_count, self.watchers_count, self.language, self.forks_count


def run():
    i = 0
    exit = False
    username = input("enter your github username: ")
    repos = get_hub(username)
    print("here are all your repos :")
    for reps in repos:
        i += 1
        print(f"{i}. {reps.name}")
    while exit == False:
        userinput = input("input a number to see more about that repo or exit to leave: ")
        if(userinput != "exit"):
            userinput = int(userinput) - 1
            print(repos[userinput].get_repo())
        else:
            exit = True

    return 0

def get_hub(username):
    allReps = []
    repos = requests.get("https://api.github.com/users/" + username + "/repos")
    repos = repos.json()
    for repo in repos:
        allReps.append(Arepo(repo["name"], repo["url"], repo["stargazers_count"], repo["watchers_count"], repo["language"], repo["forks_count"]))
    return allReps
    
    




run()
