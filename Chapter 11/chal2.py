def count_vowels(text):
    
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_count = 0
    unique_vowels = set()

    for i in text:

        if i in vowels:

            vowel_count += 1

            unique_vowels.add(i)


    return vowel_count, unique_vowels