import hgtk


file_path = "aegukga2.txt"

with open(file_path) as f:
    lines = f.read().splitlines()
    if not lines:
        pass

print(lines)
print(lines[4])
sizeOfList = len(lines)
print(sizeOfList)

jamo_str = hgtk.letter.compose('ㄹ','ㅏ','ㄺ')
print(jamo_str) #실

print(chr(44033))