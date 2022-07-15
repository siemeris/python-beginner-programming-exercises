# Your code here!!
def sing():
    cancion=""
    for index in range(11):
        if index==4:
            cancion += "whisper words of wisdom, "
        elif index==10:
            cancion += "there will be an answer, let it be"
        else:
            cancion += "let it be, "
    return cancion  

print(sing())
