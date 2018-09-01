import json
import random
import sys
import urllib.request

def main():

    content = True
    page = 1
    count = 0
    stargazers = set()
    url = 'https://api.github.com/repos/LiskHQ/lisk-hub/stargazers?page='

    print("Fetching Lisk Stargazers ...")

    while content == True:

        response_json = getStargazerPage(url, page)

        if bool(response_json) == True:
    
            stargazers, count = pullStargazers(response_json, stargazers, count)

            page += 1
            
        else:

            content = False
        
    
    winner1, winner2, winner3 = pickWinners(stargazers)

    reportWinners(winner1, winner2, winner3, count, stargazers)

    input("Press any key to list Lisk Stargazers.")
    
    
    printStargazers(stargazers)

    print()
    print()

    input('Press any key to Exit')


def getStargazerPage(url, page):

    try:

        response = urllib.request.urlopen(url + str(page))

        response_body = response.read()

        response_json = json.loads(response_body.decode("utf-8"))

        return response_json

    except urllib.error.HTTPError:

        print()
        print("GitHub's rate limit has been exceeded.")
        print("Try again in an hour, or use a different IP.")
        print()
        input('Press any key to exit')

        print()

        sys.exit(1)

def pullStargazers(response_json, stargazers, count):

    for each in response_json:

        stargazers.add(each['login'])

        count += 1

    return(stargazers, count)

def pickWinners(stargazers):

    stargazersList = list(stargazers)

    winner1 = stargazersList[random.randrange(len(stargazersList))]
    stargazersList.remove(winner1)
    winner2 = stargazersList[random.randrange(len(stargazersList))]
    stargazersList.remove(winner2)
    winner3 = stargazersList[random.randrange(len(stargazersList))]

    return winner1, winner2, winner3

def reportWinners(winner1, winner2, winner3, count, stargazers):

    print()
    print("!!!Lisk Hub has " + str(count) + " Stargazers!!!")
    print()
    print("WINNERS")
    print("-------")
    print("Winner 1: " + winner1)
    print("Winner 2: " + winner2)
    print("Winner 3: " + winner3)
    print()

def printStargazers(stargazers):
    
    print("Lisk Stargazers:")
    print()

    stargazersList = list(stargazers)
    stargazersList.sort()
    
    for each in stargazersList:

        print(each, end = " ")    

main()
