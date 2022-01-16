
def goalparse(command):

    var = command.replace("()","o").replace("(al)","al")
    return var

print(goalparse("G()(al)"))