import difflib

correct_line = "my name is Ben and i am 15 years old"

def check_spelling(user_input):
    user_words = user_input.split()
    correct_words = correct_line.split()

    if len(user_words) != len(correct_words):
        return False

    for user_word, correct_word in zip(user_words, correct_words):
        if user_word != correct_word:
            suggestions = difflib.get_close_matches(user_word, [correct_word], n=1)
            if suggestions:
                print(f"Did you mean '{suggestions[0]}' instead of '{user_word}'?")
            else:
                print(f"Spelling mistake: '{user_word}' should be '{correct_word}'.")
            return False

    return True

def main():
    user_input = input("Enter the line: ")
    if check_spelling(user_input):
        print("Correct spelling! Program finished.")
    else:
        print("Spelling mistakes detected. Program terminated.")

if __name__ == "__main__":
    main()
