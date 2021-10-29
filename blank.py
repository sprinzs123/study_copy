class Solution(object):
    def interpret(self, command):
        arr = []
        for index, letter in enumerate(command):
            if letter == 'G':
                arr.append('G')
            elif letter == '(' and  command[index + 1] == ')':
                arr.append('0')
            elif letter == '(' and command[index + 1] == 'a':
                arr.append('al')
        return ''.join(arr)









x = 'G()(al)'
test = Solution()
test.interpret(x)