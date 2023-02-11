import pytest
from GeneralCorrosionMethod.GeneralCorrosionMethod import *



def test_f_t_nom():
    assert f_t_nom(pipe_type, t, M_ut).result == 3.7592

def test_f_t_ml():
    assert f_t_ml(t_nom, FCA_ml).result == 3.6191999999999998

def test_f_t_c():
    assert f_t_c(t_nom, LOSS, FCA).result == 3.7592

def test_f_D():
    assert f_D(D_0, t_nom).result == 142.48160000000001

def test_f_D_ml():
    assert f_D_ml(type_of_wall_loss, D, FCA_ml).result == 142.48160000000001

def test_f_R_t():
    assert f_R_t(t_mm, FCA_ml, t_ml).result == 0.8261494252873564

def test_f_Q():
    assert f_Q(R_t, RSF_a).result == 2.097574142996543

def test_f_L():
    assert f_L(Q, D_ml, t_ml).result == 47.632459197714674

def test_f_t_minC():
    assert f_t_minC(P, D_0, S, E, Y_B31, MA).result == 1.6175413371675054

def test_f_t_minL():
    assert f_t_minL(P, D_0, S, E, Y_B31, MA).result == 0.8087706685837527

def test_f_t_min():
    assert f_t_min(t_minC, t_minL).result == 1.6175413371675054

def test_f_MAWP_C():
    assert f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).result == 70.53328384332713

def test_f_MAWP_L():
    assert f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).result == 144.01296576983427

def test_f_MAWP():
    assert f_MAWP(MAWP_C, MAWP_L).result == 70.53328384332713

def test_check_average_longitudinal_thickness_criteria():
    assert check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC).result == 'passed'

def test_check_average_circumferential_thickness_criteria():
    assert check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL).result == 'passed'

def test_f_MAWP_rC():
    assert f_MAWP_rC(S, E, t_amS, FCA_ml, D_0, Y_B31).result == 55.86702617744296

def test_f_MAWP_rL():
    assert f_MAWP_rL(S, E, t_amC, FCA_ml, D_0, Y_B31).result ==113.57453724107536

def test_check_MAWP_criteria():
    assert check_MAWP_criteria(MAWP_rC, MAWP_rL, P).result == 'passed'

def test_f_t_lim():
    assert f_t_lim(t_nom).result == 1.3

def test_check_minimum_thickness_criteria():
    assert check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).result == 'passed'

if __name__ == '__main__':
    pytest.main()