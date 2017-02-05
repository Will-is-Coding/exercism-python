import re


def abbreviate(unabbreviated):
    prefaceAcronym = re.match('^([A-Z]+)', unabbreviated).group(1)
    if len(prefaceAcronym) > 1:
        return prefaceAcronym
    else:
        unabbreviated = ' '.join([
                        word[0].upper() + word[1:]
                        for word in re.sub('\W', ' ', unabbreviated).split()
        ])
        return ''.join(re.findall('[A-Z]', unabbreviated))

# kentprimrose - exercism
# def abbreviate(str):
#     return ''.join(re.findall('(\w)\w*\W+', splitCamel(str)+' ')).upper()


# def splitCamel(str):
#     return re.sub('([a-z])([A-Z])', r'\1 \2', str)