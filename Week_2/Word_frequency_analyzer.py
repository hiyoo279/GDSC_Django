
def inputPar(str):
    str = input()

def spliteWord(text):
    text = input()
    return text.split()

def feqCalculator(text):
    dict = {}
    for word in text:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict
x = feqCalculator()
print(x)