

s = "Python"
print(s.upper())

print(s)
# Since the string is immutable, it will not change its value unless it is reassigned.

s = "PYTHON"
print(s.lower())
# Method changing -> as long as the method you use in the string returns abother string
# you can use other strings methods
print(s.lower().upper())    # s will be printed in all upper case since it is the last method
print(s.upper().lower())    # s will be printed in all lower case since it is the last method


s = "TeChtorial"
print(s.swapcase()) # This method will swap the letters between each other, makes lower to upper and back


s = "techtorail"
print(s.capitalize()) # This method will makes first letter capital










