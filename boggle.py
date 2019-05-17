def is_word(word):
    if word in dictionary:
        return True
    return False

def find_words():
    for word in dictionary:
        for char in word:
            for i in range (0,len(boggle[0])):
                for j in range(0,len(boggle)):
                    if boggle[i][j] == char:
                        print char


if __name__ == "__main__":
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    boggle = [['G', 'I', 'Z'],
              ['U', 'E', 'K'],
              ['Q', 'S', 'E']]
    find_words()