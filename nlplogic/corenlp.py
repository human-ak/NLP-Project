from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Searching wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize wikipedia"""
    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Getis text blob objects & returns"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name & return back phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
