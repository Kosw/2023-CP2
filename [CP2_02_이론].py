# def remove_dups(L1, L2):
#     for e in L1:
#         if e in L2:
#             L1.remove(e)
#
# def remove_dups(L1, L2):
#     L1_copy = L1[:]
#     for e in L1_copy:
#         if e in L2:
#             L1.remove(e)
#
#
# L1 = [1,2,3,4]
# L2 = [1,2,5,6]
# remove_dups(L1, L2)
# print(L1)

def lyrics_to_frequencies (lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

s = "row row row your boat"
l = s.split(" ")
d = lyrics_to_frequencies(l)
print(d)