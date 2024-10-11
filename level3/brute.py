asd = open("aray.yara", "r").read().splitlines()

test = ""
for x in asd:
    if "hash" in x:
        test += x + "\n"

print(test)
