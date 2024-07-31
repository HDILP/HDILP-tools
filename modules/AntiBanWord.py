
def conversion(text):
    after_conversion_text = ""
    for letter in text:
        after_conversion_text = after_conversion_text + letter + u'\u200B'

    return after_conversion_text

