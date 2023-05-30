from textblob import TextBlob

def correct_word(input_word):
    blob = TextBlob(input_word)
    corrected_word = str(blob.correct())
    return corrected_word

# Example usage
input_word = input("Enter a word: ")
corrected_word = correct_word(input_word)

if corrected_word != input_word:
    print(f"Did you mean '{corrected_word}'?")
else:
    print("No correction found.")
