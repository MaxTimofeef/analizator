text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]
for char in punctuation:
  text = text.replace(char, "")

words = text.split()
print(words)