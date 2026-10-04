import re
from collections import Counter

import nltk
from nltk.corpus import stopwords


# Download stopwords
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))


# -----------------------------------
# Keyword Extraction Function
# -----------------------------------

def extract_keywords(text, number_of_keywords=10):

    # Convert text to lowercase
    text = text.lower()

    # Extract words only
    words = re.findall(r'\b[a-zA-Z]+\b', text)

    # Remove stop words
    filtered_words = []

    for word in words:

        if word not in stop_words and len(word) > 2:

            filtered_words.append(word)

    # Count word frequency
    word_frequency = Counter(filtered_words)

    # Get most common keywords
    keywords = word_frequency.most_common(
        number_of_keywords
    )

    return keywords


# -----------------------------------
# Main Program
# -----------------------------------

print("=" * 50)
print("       TEXT KEYWORD EXTRACTOR")
print("=" * 50)

print("\nEnter your paragraph.")
print("Type END on a new line when finished.\n")


lines = []

while True:

    line = input()

    if line.strip().upper() == "END":

        break

    lines.append(line)


text = " ".join(lines)


# Check input
if not text.strip():

    print("\n❌ No text entered.")

else:

    keywords = extract_keywords(
        text,
        10
    )

    print("\n" + "=" * 50)
    print("           TOP KEYWORDS")
    print("=" * 50)

    for position, (word, frequency) in enumerate(
        keywords,
        start=1
    ):

        print(
            f"{position}. {word} "
            f"({frequency} times)"
        )

    print("\n✅ Keyword extraction completed.")