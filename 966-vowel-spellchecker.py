def spellchecker(wordlist, queries):
    def devowel(word):
        return ''.join('*' if c in 'aeiou' else c for c in word.lower())

    exact_words = set(wordlist)
    case_insensitive = {}
    vowel_errors = {}

    for word in wordlist:
        lower_word = word.lower()
        if lower_word not in case_insensitive:
            case_insensitive[lower_word] = word
        devoweled_word = devowel(word)
        if devoweled_word not in vowel_errors:
            vowel_errors[devoweled_word] = word

    result = []
    for query in queries:
        if query in exact_words:
            result.append(query)
        elif query.lower() in case_insensitive:
            result.append(case_insensitive[query.lower()])
        elif devowel(query) in vowel_errors:
            result.append(vowel_errors[devowel(query)])
        else:
            result.append("")
    return result

# Example usage
wordlist1 = ["KiTe","kite","hare","Hare"]
queries1 = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
print(spellchecker(wordlist1, queries1))

# wordlist2 = ["yellow"]
# queries2 = ["YellOw"]
# print(spellchecker(wordlist2, queries2))
