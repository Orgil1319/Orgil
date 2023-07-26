import webbrowser

text = input("input: ")
url = "https://translate.google.com/#en/mn/" + text

webbrowser.open(url)
