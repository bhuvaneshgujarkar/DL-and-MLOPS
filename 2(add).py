add_table = {
    "ed": ["walk", "talk", "cook"],
    "ing": ["walk", "jump", "read"],
    "s": ["cat", "dog", "car"]
}
delete_table = {
    "ed": ["walked", "talked", "cooked"],
    "ing": ["walking", "jumping", "reading"],
    "s": ["cats", "dogs", "cars"]
}
def apply_add_table(add_table):
    print("Words generated using add table:")
    for suffix, roots in add_table.items():
        for root in roots:
            word = root + suffix
            print(f"{root} + {suffix} → {word}")
    print("\n")
def apply_delete_table(delete_table):
    print("Words analyzed using delete table:")
    for suffix, words in delete_table.items():
        for word in words:
            if word.endswith(suffix):
                root = word[:-len(suffix)]
                print(f"{word} - {suffix} → {root}")
    print("\n")
apply_add_table(add_table)
apply_delete_table(delete_table)


# py -3.10 -m pip install spacy
# py -3.10 -m spacy download en_core_web_sm
