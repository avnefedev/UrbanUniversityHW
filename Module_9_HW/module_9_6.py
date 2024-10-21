def all_variants(text):
    for i in range(len(text)):
        for k in range(i, len(text)):
            yield text[i:k+1]

a = all_variants("abcd")
print(a)
for i in a:
    print(i)
