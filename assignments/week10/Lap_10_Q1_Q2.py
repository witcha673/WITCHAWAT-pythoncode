#1

name1 = input("ENTER YOUR NAME")


if not all (x.isalpha() or x.isspace() for x in name1) or not name1:
    print("Wrong name")

age = input("ENTER AGE")

agechange = int(age)

if agechange < 18 or agechange > 65:
    print("Wrong age, must be between 18 and 65")



phone = input("ENTER YOUR 10-DIGIT PHONE NUMBER: ").strip()

if not (phone.isdigit() and len(phone) == 10):
    print("Phone is wrong")




print("Personal Information:")
print("Name: {}".format(name1.upper()))
print("Age: {}".format(agechange))
print("Phone: {}".format(phone))



#2

text = input("Enter text: ")

total_chars_with_spaces = len(text)
total_chars_without_spaces = len(text.replace(" ", ""))

vowels_list = "aeiouAEIOU"
vowels = [ch for ch in text if ch in vowels_list]
consonants = [ch for ch in text if ch.isalpha() and ch not in vowels_list]


most_frequent_char = max(text.replace(" ", ""), key=text.count)


words = text.split()
total_words = len(words)
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

words_starting_with_vowels = [w for w in words if w[0].lower() in vowels_list]
words_starting_with_consonants = [w for w in words if w[0].isalpha() and w[0].lower() not in vowels_list]

title_case = text.title()
upper_case = text.upper()
lower_case = text.lower()
acronym = "".join(w[0].upper() for w in words)
reversed_text = text[::-1]
words_reversed = " ".join(w[::-1] for w in words)


print("\n=== TEXT ANALYSIS REPORT ===")
print("Character Analysis:")
print(f"- Total characters: {total_chars_with_spaces} (with spaces), {total_chars_without_spaces} (without spaces)")
print(f"- Vowels: {len(vowels)} ({', '.join(vowels)})")
print(f"- Consonants: {len(consonants)}")
print(f"- Most : '{most_frequent_char}' (appears {text.count(most_frequent_char)} times)")

print("\nWord Analysis:")
print(f"- Total words: {total_words}")
print(f"- Longest word: \"{longest_word}\" ({len(longest_word)} letters)")
print(f"- Shortest word: \"{shortest_word}\" ({len(shortest_word)} letters)")
print(f"- Words starting with vowels: {len(words_starting_with_vowels)} ({', '.join(words_starting_with_vowels)})")
print(f"- Words starting with consonants: {len(words_starting_with_consonants)}")

print("\nTransformations:")
print(f"- TitleCase: {title_case}")
print(f"- UpperCase: {upper_case}")
print(f"- LowerCase: {lower_case}")
print(f"- Acronym: {acronym}")
print(f"- Reversed Text: {reversed_text}")
print(f"- WordsReversed: {words_reversed}")