classify_person = int(input("how old are you?"))

if 0 <= classify_person <= 12:
   print("child")
elif 13 <= classify_person <= 17:
    print("teenager")
elif 18 <= classify_person <= 64:
    print("adult")
else:
    print("senior")