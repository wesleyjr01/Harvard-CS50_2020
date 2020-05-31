import cs50
import re

text = cs50.get_string("Text: ")
sentences = [f for f in re.split(r"[.!?]+", text) if len(f) > 0]
sentences_count = len(sentences)
words = re.findall(r"\b\S+\b", text)
words_count = len(words)
letters_count = 0
for word in words:
    letters_count = letters_count + len(word.replace("'", ""))
fomula = int(
    round(
        0.0588 * letters_count * 100 / words_count
        - 0.296 * sentences_count * 100 / words_count
        - 15.8
    )
)
if fomula >= 16:
    fomula = "16+"
elif fomula < 1:
    fomula = 1
else:
    pass
print(f"Grade {fomula}")
