import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_meaning(word):
    url = BASE_URL + word
    response = requests.get(url)

    if response.status_code != 200:
        print(" Word not found!")
        return

    data = response.json()

    meaning = data[0]["meanings"][0]["definitions"][0]["definition"]

    example = data[0]["meanings"][0]["definitions"][0].get(
        "example", "No example available"
    )

    synonyms_list = data[0]["meanings"][0]["definitions"][0].get("synonyms", [])

    if len(synonyms_list) >= 2:
        synonym1 = synonyms_list[0]
        synonym2 = synonyms_list[1]
    elif len(synonyms_list) == 1:
        synonym1 = synonyms_list[0]
        synonym2 = "Not available"
    else:
        synonym1 = "Not available"
        synonym2 = "Not available"

    print("\n WORD:", word)
    print(" Meaning:", meaning)
    print(" Synonym 1:", synonym1)
    print(" Synonym 2:", synonym2)
    print(" Example:", example)


def main():
    while True:
        word = input("\nEnter a word (or type exit): ")

        if word.lower() == "exit":
            print(" Program Ended")
            break

        get_meaning(word)


if __name__ == "__main__":
    main()
