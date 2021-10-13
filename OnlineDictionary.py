#Your python dictionary to get the meaning of any word you want using free dictionary API :)
import requests

def meaning(w):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{w}").json()
    try:
        return response[0]["meanings"][0]["definitions"][0]["definition"] 
    except:
        return "Sorry buddy, Couldn't find the word you were searching for!"

if __name__ == "__main__":
    print("\n-----------------------------------------------")
    print("Welcome to Python Script for Dictionary :-")
    while True:
        word = input("Type word you want to search for or ENTER to exit : ")
        if not word:
            break
        print("\nDefinition : ",meaning(word),"\n")
    print("Thanks for the visit 😊\n")