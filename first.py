s = str(raw_input()).replace(" ","")
print(sum(1 for x in s if x.isupper()))