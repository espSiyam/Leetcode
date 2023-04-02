sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

max_num = 0

for i in range(len(sentences)):
    words = len(sentences[i].split(" "))
    if words > max_num:
        max_num = words
print(max_num)