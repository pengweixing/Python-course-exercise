#################################################
#  File Name:test_simple_math.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Thu Mar  9 13:15:13 2023
#################################################

import simple_math

def test_simple_add():
    assert simple_math.simple_add(2,2) == 4

def test_simple_sub():
    assert simple_math.simple_sub(2,2) == 0

def test_simple_mult():
    assert simple_math.simple_mult(2,2) == 4

def test_simple_div():
    assert simple_math.simple_div(2,2) == 1

def test_poly_first():
    assert simple_math.poly_first(2,2,1) == 4   

def test_poly_second():
    assert simple_math.poly_second(2,2,1,1) == 8