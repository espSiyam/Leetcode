command = "(al)G(al)()()G"
command = command.replace("()","o").replace("(al)","al")
print(command)



class Solution(object):
    def interpret(self, command):
        mapping = {'(al)':'al', '()': 'o', 'G':'G'}
        res = []
        tmp = []

        for data in command:
            tmp.append(data)
            tmp_str = "".join(tmp)
            if tmp_str in mapping:
                res.append(mapping[tmp_str])
                tmp = []

        return "".join(res)