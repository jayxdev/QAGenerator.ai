import requests
from pprint import pprint
from bs4 import BeautifulSoup


# Example: Get the content of a Wikipedia page
def wikki_extractor(topic, word_limit):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": topic
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Example: Extract the page content from the response
    page_id = list(data["query"]["pages"].keys())[0]
    content = data["query"]["pages"][page_id]["extract"]
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()
    words = text.split()  # Split the string into individual words
    print(len(words))
    para = [' '.join(words[i:i + word_limit]) for i in range(0, len(words), word_limit)]
    return para[0]


pprint(wikki_extractor("money", 200))
