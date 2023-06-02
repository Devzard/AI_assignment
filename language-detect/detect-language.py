from langdetect import detect


def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unable to detect the language."


# Example usage
input_text = input("Enter some text: ")
language = detect_language(input_text)
print("Detected language:", language)
