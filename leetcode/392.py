class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pass


p = list("acb")
primer = list("atttbapppcvcv")

# for c in p:
#     if c in primer:
#         primer = primer[primer.index(c) + 1:]
#     else:
#         print("False")
#         break

print(primer[primer.index("c") + 1:])