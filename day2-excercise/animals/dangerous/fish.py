#################################################
#  File Name:mammals.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Tue Mar  7 13:29:54 2023
#################################################

class Fish:
    def __init__(self):
        self.members = ['Candiru','Puffer','Tiger Fish']

    def printMembers(self):
        print('Printing members of the dangerous fish class')
        for member in self.members:
            print('\t%s ' % member)
