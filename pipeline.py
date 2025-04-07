import requests
from prefect import flow, task


@flow
def BandoriTeams():
    ownCards = GetOwnDatabase()
    allCards = [GetCards(i) for i in range(1, 21)]
    sortedOwnCards = GetOwnedCards(ownCards, allCards)
    return sortedOwnCards

@task
def GetOwnDatabase():
    file = open("db.csv", "r").readlines()
    return file

@task
def GetCards(id: int):
    response = requests.get(f"https://bandori.party/api/cards/?page_size=100&page={id}").json()
    return response["results"]

@task
def GetOwnedCards(ownCards: list, allCards: list):
    sortedOwnCards = []
    for own in ownCards:
        try:
            own = int(own)
            for elem in allCards:
                if elem[-1]["id"] <= own <= elem[0]["id"]:
                    for card in elem:
                        if card["id"] == own:
                            sortedOwnCards.append(card)
                else:
                    continue
        except:
            continue
    return sortedOwnCards


# @task
# def say_hello():
#     return f"Hello!"

# @task
# def say_hello():
#     return f"Hello!"

if __name__ == "__main__":
    BandoriTeams()

