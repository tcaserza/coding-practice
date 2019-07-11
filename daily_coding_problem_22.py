# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
# then return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


def find_sentence(word_dict,word_string):
    return_list = []
    j = 0
    for i in range(len(word_string)+1):
        if word_string[j:i] in word_dict:
            return_list.append(word_string[j:i])
            j = i
    return return_list


print find_sentence(['quick', 'brown', 'the', 'fox'],"thequickbrownfox")