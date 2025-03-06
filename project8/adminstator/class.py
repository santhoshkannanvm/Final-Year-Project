def upperstr(ref):
    a="ji"

    def process():
        data=ref()
        x=data.upper()
        return a

    return a

def my():
    return "hii"

result=upperstr(my)
print(type(result))
print(result.__name__)

print(result)