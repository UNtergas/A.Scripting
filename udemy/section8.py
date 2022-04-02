
def sentence_maker(phrase):
    interrogate = ("How","What","Why")
    listing =[word[0].upper()+word[1:] for word in phrase.split()]
    phrase = " ".join(listing)
    if (phrase.startswith(interrogate)):
        return "{}?".format(phrase)
    return "{}".format(phrase)
#
typing=[]

while True:
    Uinput = input("type:..")
    if(Uinput != "\quit"):
        typing.append(sentence_maker(Uinput))
    else:
        break
#
print(" ".join(typing))
