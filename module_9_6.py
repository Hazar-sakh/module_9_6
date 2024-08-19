def all_variants(text):
    nl = len(text)
    end = nl + 1
    for i in range(1, end):
        for j in range(end - i):
            yield text[j:j+i]


a = all_variants("abc")
for i in a:
    print(i)