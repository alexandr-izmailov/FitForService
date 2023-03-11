from LocalCorrosionMethod.LocalCorrosionMethod import *

# input data
t = 5.49
pipe_type = 'seamless %'
M_ut = 12.5
LOSS = 0
FCA = 0
FCA_ml = 0
t_mm = 3.16
s = 50
S = 138
D_0 = 88.9
L_msd = 1000
g_r = 0
E = 1
MA = 0
Y_B31 = 0.4
t_sl = 0
RSF_a = 0.9
c = 50
EL = 1
EC = 1
P = 16.5


# Calculated data
t_nom =  4.80375
t_c = 4.80375
R_t = 0.6578194119177726
D = 79.2925
λ = 3.2920534500201546
M_t = 2.247816928282341
MAWP_C = 155.87605958357338
MAWP_L =  326.5040510256852
MAWP =  155.87605958357338
RSF = 0.7759390281706254
MAWPr = 134.3892424314938
t_minL = 2.154046526063717
MAWPr_new = 197.14987626546682

def test_t_nom():
    assert f_t_nom(pipe_type, t, M_ut).result == t_nom

def test_f_t_c():
    assert f_t_c(t_nom, LOSS, FCA).result == t_c

def test_f_D():
    assert f_D(D_0, t_nom).result == D

def test_f_λ():
    assert f_λ(s, D, t_c).result == λ

def test_f_R_t():
    assert f_R_t(t_mm, FCA_ml, t_c).result == R_t

def test_check_R_t():
    assert  check_R_t(R_t).result == 'passed'

def test_check_thickness():
    assert  check_thickness(t_mm, FCA_ml).result == 'passed'

def test_check_check_L_msd_criteria():
    assert check_L_msd_criteria(L_msd, D, t_c).result == 'passed'

def test_check_Groove_flaw_criteria():
    assert check_Groove_flaw_criteria(g_r, R_t, t_c).result == 'failed'

def test_f_MAWP_C():
    assert f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).result == MAWP_C

def test_f_MAWP_L():
    assert  f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).result == MAWP_L

def test_f_MAWP():
    assert f_MAWP(MAWP_C, MAWP_L).result == MAWP

def test_f_M_t():
    assert f_M_t(λ).result == M_t

def test_check_screening_criteria():
    assert check_screening_criteria(λ, R_t, RSF_a, M_t).result == 'NOT acceptable'

def test_f_RSF():
    assert f_RSF(R_t, M_t).result == RSF

def test_f_MAWPr():
    assert  f_MAWPr(MAWP, RSF, RSF_a).result == MAWPr

def test_check_circumferential_extent_criteria():
    assert check_circumferential_extent_criteria(c, s, EL, EC).result == 'passed'

def test_f_t_minL():
    assert  f_t_minL(MAWPr, D_0, S, E, P, Y_B31, t_sl, MA).result == t_minL

def test_check_minimum_thickness_required_criteria():
    assert check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml).result == 'passed'

def test_f_MAWPr_new():
    assert f_MAWPr_new(MAWPr, t_mm, FCA_ml, t_minL).result == MAWPr_new