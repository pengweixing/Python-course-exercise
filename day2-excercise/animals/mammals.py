#################################################
#  File Name:mammals.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Tue Mar  7 13:25:53 2023
#################################################

class Mammals:
    def __init__(self):
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
