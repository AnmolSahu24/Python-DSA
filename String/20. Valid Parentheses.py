
def ValidParent(str):

    # flag_ = False

    while('()' in str or "{}" in str or '[]' in str):
        str = str.replace('()','')
        str = str.replace('[]','')
        str = str.replace('{}','')

    if str != "":
        return False
    else:
        return True


s = "()[]{}"
print(ValidParent(s))



