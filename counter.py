from collections import Counter, defaultdict


def count_words(words: list[str]) -> dict[str, int]:
    counter = {}
    for word in words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1
    return counter


def count_words__default(words: list[str]) -> dict[str, int]:
    counter = defaultdict(int)
    for word in words:
        counter[word] += 1
    return counter


def count_words__count(words: list[str]) -> dict[str, int]:
    counter = {}
    for word in set(words):
        counter[word] = words.count(word)

    return counter


def count_words__counter(words: list[str]) -> dict[str, int]:
    counter = Counter(words)
    return counter.most_common(10)
