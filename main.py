def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents_lower = file_contents.lower()
        # print(count_words(file_contents_lower))
        # print(count_letters(file_contents_lower))
        report_on_letters(file_contents_lower)

def count_words(source):
    words = source.split()
    return len(words)

def count_letters(source):
    characters = {}
    for c in source:
        if c not in characters:
            characters[c] = source.count(c)
    return characters

def report_on_letters(source):
    characters = count_letters_formatted(source)
    print(characters)

    print(f"Start of report")

    for c in characters:
        print(f"Letter {repr(c["name"])} found {c["num"]} times")

        
    print(f"End of report")


def count_letters_formatted(source):
    characters = []
    for c in source:
        if not any(d.get('name') == c for d in characters):
            characters.append({"name": c, "num": source.count(c)})
    characters.sort(reverse=True, key=sort_on)
    return characters

def sort_on(dict):
    return dict["num"]

main()