import re


def abbreviate(unabbreviated):
    unabbreviated = re.sub('\W', ' ', unabbreviated).split(' ')
    acronym = ''
    #print(unabbreviated)
    for word in unabbreviated:
        if word:
            test = re.findall('[A-Z]', word)
            print(''.join(test))
            acronym += ''.join(test)
            #acronym += word[0].upper()
    print(acronym)
    return acronym


# def abbreviate(unabbreviated):
#     unabbreviated = [letter for letter in unabbreviated if letter.isupper()]
#     print(unabbreviated)

print(abbreviate('HyperText Markup Language'))

# PHP: Hypertext Preprocessor
# Complementary metal-oxide semiconductor
# First In, First Out
# HyperText Markup Language
# Ruby on Rails
# Portable Network Graphics'