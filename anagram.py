str1 = input("Enter your string : ")
str2 = input("Enter your String : ")
str1 = str1.lower()
str2 = str2.lower()
if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if(sorted_str1 == sorted_str2):
        print(str1 +  " and " + str2 +  " are anagrams.")
    else:
        print(str1 + " and " + str2 + " are not anagrams.")

else:
    print(str1 + " and " + str2 + " are not anagrams.")
