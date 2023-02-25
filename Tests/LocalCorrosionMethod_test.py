from LocalCorrosionMethod.LocalCorrosionMethod import *

# input data
t = 5.49
pipe_type = 'Seamless'
M_ut = 12.5
LOSS = 0
FCA = 0
FCA_ml = 0
t_mm = 3.16
s = 50
D_0 = 88.9

# Calculated data
t_nom =  4.80375
t_c = 4.80375
R_t = 0.6578194119177726
D = 79.2925
λ = 3.2920534500201546


def test_t_nom():
    assert f_t_nom(pipe_type, t, M_ut).result == t_nom

def test_f_t_c():
    assert f_t_c(t_nom, LOSS, FCA).result == t_c

def test_f_R_t():
    assert f_R_t(t_mm, FCA_ml, t_c).result == R_t

def test_f_D():
    assert f_D(D_0, t_nom).result == D

def test_f_λ():
    assert f_λ(s, D, t_c).result == λ