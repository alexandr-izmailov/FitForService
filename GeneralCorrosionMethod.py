# input data
t = 3.7592
pipe_type = 'Seamless'
M_ut = 0
FCA_ml = 0.14
LOSS = 0
FCA = 0
type_of_wall_loss = 'external'
t_mm = 3.13
RSF_a = 0.9


P = 30
S = 137.9
D_0 = 150
E = 1
Y_B31 = 0.4
MA = 0
t_sl = 0
t_amS = 3.13
t_amC = 3.13



# function definition
# step 1.1 ------------------------------------------------
def f_t_nom(pipe_type, t, M_ut):
    """"
    t_nom - nominal or furnished thickness of the component adjusted for mill undertolerance as applicable, [mm]
    """
    if pipe_type in ('Seamless', 'User defined %'):
        t_nom = t * (1 - M_ut)
        text = f't_nom = t * (1 - M_ut) = {t} * (1 - {M_ut}) = {t_nom}'
    elif pipe_type in ('Welded', 'User defined mm'):
        t_nom = t - M_ut
        text = f't_nom = t - M_ut = {t} - {M_ut} = {t_nom}'
    return t_nom

# для теста
t_nom = f_t_nom(pipe_type, t, M_ut)

# step 1 ------------------------------------------------
def f_t_ml(t_nom, FCA_ml):
   """
   t_ml - Nominal thickness in the region of corrosion corrected FCA_ml, [mm]
   """
   t_ml = t_nom - FCA_ml
   text = f't_ml = t_nom - FCA_ml = {t_nom} - {FCA_ml} = {t_ml}'
   return t_ml

# для теста
t_ml = f_t_ml(t_nom, FCA_ml)

# step 2 ------------------------------------------------
def f_t_c(t_nom, LOSS, FCA):
    """
    t_c - Future corroded wall thickness away from the damage area, [mm]
    """
    t_c = t_nom - LOSS - FCA
    text = f't_c = t_nom - LOSS - FCA = {t_nom} - {LOSS} - {FCA} = {t_c}'
    return t_c

# для теста
t_c = f_t_c(t_nom, LOSS, FCA)

# step 3.1------------------------------------------------
def f_D(D_0, t_nom):
    """
    D - Inside diameter of the cylinder, cone (at the location of the flaw), [mm]
    """
    D = D_0 - 2 * t_nom
    text = f'D = D_0 - 2 * t_nom = {D_0} - 2 * {t_nom} = {D}'
    return D

# для теста
D = f_D(D_0, t_nom)

# step 3------------------------------------------------
def f_D_ml(type_of_wall_loss, D, FCA_ml):
    """
    D_ml - Inside diameter of the cylinder corrected for FCA_ml, [mm]
    """
    if type_of_wall_loss == 'internal':
        D_ml = D + 2 * FCA_ml
        text = f'D_ml = D + 2 * FCA_ml = {D} + 2 * {FCA_ml} = {D_ml}'
    elif type_of_wall_loss == 'external':
        D_ml = D
    return D_ml

# для теста
D_ml = f_D_ml(type_of_wall_loss, D, FCA_ml)

# step 4------------------------------------------------
def f_R_t(t_mm, FCA_ml,  t_ml):
    """
    Remaining thickness ratio R_t, [-]
    """
    R_t = (t_mm - FCA_ml) / t_ml
    text = f'R_t = (t_mm - FCA_ml) / t_ml = {t_mm} - {FCA_ml} / {t_ml} = {R_t}'
    return R_t

# для теста
R_t = f_R_t(t_mm, FCA_ml, t_ml)

# step 5------------------------------------------------
def f_Q(R_t, RSF_a):
    """
    Parameter Q - Factor used to determine the length for thickness averaging based on an allowable Remaining Strength Factor
    and the remaining thickness ratio Rt. Table 4.8 [-].

    RSF_a - Allowable remaining strength factor.
    Recommended Remaining Strength Factor RSFa is 0.90
    """
    if R_t < RSF_a:
        Q = 1.123 * (((1 - R_t) / (1 - R_t  /  RSF_a))**2 - 1)**(0.5)
        text = f'Q = 1.123 * (((1 - R_t) / (1 - R_t  /  RSF_a))^2 - 1)^0.5 = 1.123 * (((1 - {R_t}) / (1 - {R_t}  /  {RSF_a}))^2 - 1)^0.5 = {Q}'
    elif R_t >= RSF_a:
        Q = 50
        text = f'Q = 50'
    return Q

# для теста
Q = f_Q(R_t, RSF_a)

# step 6------------------------------------------------
def f_L(Q, D_ml, t_ml):
    """
    Length for thickness averaging L, [mm]
    """
    L = Q * (D_ml * t_ml) ** 0.5
    text = f'L = Q * (D_ml * t_ml) ^ 0.5 = {Q} * ({D_ml} * {t_ml}) ^ 0.5 = {L}'
    return L

# step 7------------------------------------------------
def f_t_minC(P, D_0, S, E, Y_B31, MA):
    """
    Minimum required thickness based on the
    circumferential stress, [mm]
    """
    t_minC = (P * D_0 / 10) / (2 * (S * E + P / 10 * Y_B31)) + MA
    text = f't_minC = (P * D_0) / (2 * (S * E + P * Y_B31)) + MA = ({P} * {D_0} / 10) / (2 * ({S} * {E} + {P} / 10 * {Y_B31})) + {MA} = {P}'
    return t_minC

# для теста
t_minC = f_t_minC(P, D_0, S, E, Y_B31, MA)

def f_t_minL(P, D_0, S, E, Y_B31, MA):
    """
    Minimum required thickness based on the
    longitudinal stress, [mm]
    """
    t_minL = (P * D_0 / 10) / (4 * (S * E + P / 10 * Y_B31)) + t_sl + MA
    text = f't_minL = (P * D_0) / (4 * (S * E + P * Y_B31)) + t_sl + MA = ({P} * {D_0} / 10) / (4 * ({S} * {E} + {P} / 10 * {Y_B31})) + {t_minL}'
    return t_minL

# для теста
t_minL = f_t_minL(P, D_0, S, E, Y_B31, MA)

def f_t_min(t_minC, t_minL):
    """
    minimum required thickness , [mm]
    """
    t_min = max(t_minC, t_minL)
    text = f't_min = max(t_minC; t_minL) = max({t_minC}; {t_minL}) = {t_min}'
    return t_min

# step 8------------------------------------------------
def f_MAWP_C(S, E, t_c, MA, D_0, Y_B31):
    """
    maximum allowable working pressure based on circumferential stress, [bar]
    """
    MAWP_C = 10 * (2 * S * E * (t_c - MA)) / (D_0 - 2 * Y_B31 * (t_c - MA))
    text = f'MAWP_C = (2 * S * E * (t_c - MA)) / (D_0 - 2 * Y_B31 * (t_c - MA)) = 10 * (2 * {S} * {E} * ({t_c} - {MA})) / ({D_0} - 2 * {Y_B31} * ({t_c} - {MA})) = {MAWP_C}'
    return MAWP_C

# для теста
MAWP_C = f_MAWP_C(S, E, t_c, MA, D_0, Y_B31)

def f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl):
    """
    maximum allowable working pressure based on longitudinal stress, [bar]
    """
    MAWP_L = 10 * (4 * S * E * (t_c - t_sl - MA)) / (D_0 - 4 * Y_B31 * (t_c - t_sl - MA))
    text = f'MAWP_L = (4 * S * E * (t_c - t_c - t_sl - MA)) / (D_0 - 4 * Y_B31 * (t_c - t_sl - MA)) = 10 * (4 * {S} * {E} * ({t_c} - {t_sl} - {MA})) / ({D_0} - 4 * {Y_B31} * ({t_c} - {t_sl} - {MA})) = {MAWP_L}'
    return MAWP_L

# для теста
MAWP_L = f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl)

def f_MAWP(MAWP_C, MAWP_L):
    """
    maximum allowable working pressure, [bar]
    """
    MAWP = min(MAWP_C, MAWP_L)
    text = f'MAWP = min(MAWP_C; MAWP_L) = min({MAWP_C}; {MAWP_L}) = {MAWP}'
    return MAWP

# step 9------------------------------------------------
def check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minL):
    """
    Average Measured Thickness from Critical Thickness Profiles based on the
    longitudinal CTP determined at the time of the inspection
    """
    if (t_amS - FCA_ml) >= t_minL:
        average_longitudinal_thickness_criteria = 'passed'
        text = f'(t_amS - FCA_ml) >= t_minL |---> ({t_amS} - {FCA_ml}) >= {t_minL} |---> Average longitudinal thickness criteria is -> {average_longitudinal_thickness_criteria} <-'
    elif (t_amS - FCA_ml) < t_minL:
        average_longitudinal_thickness_criteria = 'failed'
        text = f'(t_amS - FCA_ml) < t_minL |---> ({t_amS} - {FCA_ml}) < {t_minL} |---> Average longitudinal thickness criteria is -> {average_longitudinal_thickness_criteria} <-'
    return average_longitudinal_thickness_criteria

def check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minC):
    """
    Average Measured Thickness from Critical Thickness Profiles based on the
    circumferential CTP determined at the time of the inspection
    """
    if (t_amC - FCA_ml) >= t_minC:
        average_circumferential_thickness_criteria = 'passed'
        text = f'(t_amC - FCA_ml) >= t_minC |---> ({t_amC} - {FCA_ml}) >= {t_minC} |---> Average circumferential thickness criteria is -> {average_circumferential_thickness_criteria} <-'
    elif (t_amC - FCA_ml) < t_minC:
        average_circumferential_thickness_criteria = 'failed'
        text =  f'(t_amC - FCA_ml) < t_minC |---> ({t_amC} - {FCA_ml}) < {t_minC} |---> Average circumferential thickness criteria is -> {average_circumferential_thickness_criteria} <-'
    return average_circumferential_thickness_criteria


if __name__ == '__main__':
    print('t_nom = ', f_t_nom(pipe_type, t, M_ut))
    print('')
    print('t_ml = ', f_t_ml(t_nom, FCA_ml))
    print('')
    print('t_c = ', f_t_c(t_nom, LOSS, FCA))
    print('')
    print('D = ', f_D(D_0, t_nom))
    print('')
    print('D_ml = ', f_D_ml(type_of_wall_loss, D, FCA_ml))
    print('')
    print('R_t = ', f_R_t(t_mm, FCA_ml, t_ml))
    print('')
    print('Q = ', f_Q(R_t, RSF_a))
    print('')
    print('L = ',  f_L(Q, D_ml, t_ml))
    print('')
    print('t_minC = ', f_t_minC(P, D_0, S, E, Y_B31, MA))
    print('')
    print('t_minL = ', f_t_minL(P, D_0, S, E, Y_B31, MA))
    print('')
    print('t_min = ', f_t_min(t_minC, t_minL))
    print('')
    print('MAWP_C = ', f_MAWP_C(S, E, t_c, MA, D_0, Y_B31))
    print('')
    print('MAWP_L = ', f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl))
    print('')
    print('MAWP = ', f_MAWP(MAWP_C, MAWP_L))
    print('')
    print(f'(t_amC - FCA_ml) >= t_minC |---> ({t_amC} - {FCA_ml}) >= {t_minC} |---> Average circumferential thickness criteria is -> ', check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minL))
    print('')
    print(f'(t_amC - FCA_ml) >= t_minC |---> ({t_amC} - {FCA_ml}) >= {t_minC} |---> Average circumferential thickness criteria is -> ',check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minC))
    print('')
