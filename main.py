import re

from counter import count_words__counter
from stopwords import without_stopwords
from morph import get_nouns, normalize


def load(path: str, encoding: str = "utf-8") -> str:
    with open(path, encoding=encoding, errors="ignore") as f:
        data = f.read()

    return data


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w{3,}", text)


if __name__ == "__main__":
    text = load("data/wizard_oz.txt", encoding="cp1251")
    words = without_stopwords(tokenize(text))
    nouns = normalize(get_nouns(words))
    print(count_words__counter(nouns))
