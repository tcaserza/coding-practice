# Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings
# which represents each line, fully justified.
#
# More specifically, you should have as many words as possible in each line. There should be at least one space between
# each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as
# equally as possible, with the extra spaces, if any, distributed starting from the left.
#
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
#
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and
# k = 16, you should return the following:
#
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly


def justify_text(word_list,k):
    return_strings = []
    line_length = 0
    words = []
    for i in range(len(word_list)):
        word = word_list[i]
        if line_length + len(word) < k:
            words.append(word)
            line_length += len(word) + 1
        else:
            line = pad_text(words,k)
            return_strings.append(line)
            del words[:]
            words.append(word)
            line_length = len(word) + 1
    last_line = pad_text(words,k)
    return_strings.append(last_line)
    return return_strings


def pad_text(words, k):
    line_length = 0
    retstr = ""
    for i in range(len(words) - 1):
        words[i] += " "
        line_length += len(words[i])
    line_length += len(words[i+1])
    additional_spaces_needed = k - line_length
    i = 0
    while additional_spaces_needed > 0:
        words[i % (len(words) - 1)] += " "
        additional_spaces_needed -= 1
        i += 1
    for word in words:
        retstr += word
    return retstr


text = justify_text(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)
for line in text:
    print "'%s'" % line
