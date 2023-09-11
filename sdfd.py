
def check(a):
    b = ""
    for i in a:
        if i.isalpha():
            b+=i.lower()
    return b
print(check("NITHIN"))

