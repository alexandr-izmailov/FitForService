from Classes.MajorClasses import DataCalculated


# function definition
# step 1.1 ------------------------------------------------
def f_t_nom(pipe_type, t, M_ut):
    """"
    t_nom - Nominal or furnished thickness of the component adjusted for mill undertolerance as applicable, [mm]
    """
    if pipe_type.lower() in ('seamless %', 'user defined %'):
        t_nom = t * (1 - M_ut / 100)
        text = f't_nom = t * (1 - M_ut / 100) = {t} * (1 - {M_ut} / 100) = {t_nom}'
        data = DataCalculated(t_nom, text)
    elif pipe_type.lower() in ('welded mm', 'user defined mm'):
        t_nom = t - M_ut
        text = f't_nom = t - M_ut = {t} - {M_ut} = {t_nom}'
        data = DataCalculated(t_nom, text)
    return data


# # для теста
# t_nom = f_t_nom(pipe_type, t, M_ut).result


# step 1 ------------------------------------------------
def f_t_ml(t_nom, FCA_ml):
    """
    t_ml - Nominal thickness in the region of corrosion corrected FCA_ml, [mm]
    """
    t_ml = t_nom - FCA_ml
    text = f't_ml = t_nom - FCA_ml = {t_nom} - {FCA_ml} = {t_ml}'
    data = DataCalculated(t_ml, text)
    return data


# # для теста
# t_ml = f_t_ml(t_nom, FCA_ml).result


# step 2 ------------------------------------------------
def f_t_c(t_nom, LOSS, FCA):
    """
    t_c - Future corroded wall thickness away from the damage area, [mm]
    """
    t_c = t_nom - LOSS - FCA
    text = f't_c = t_nom - LOSS - FCA = {t_nom} - {LOSS} - {FCA} = {t_c}'
    data = DataCalculated(t_c, text)
    return data


# # для теста
# t_c = f_t_c(t_nom, LOSS, FCA).result


# step 3.1------------------------------------------------
def f_D(D_0, t_nom):
    """
    D - Inside diameter of the cylinder, cone (at the location of the flaw), [mm]
    """
    D = D_0 - 2 * t_nom
    text = f'D = D_0 - 2 * t_nom = {D_0} - 2 * {t_nom} = {D}'
    data = DataCalculated(D, text)
    return data


# # для теста
# D = f_D(D_0, t_nom).result


# step 3------------------------------------------------
def f_D_ml(type_of_wall_loss, D, FCA_ml):
    """
    D_ml - Inside diameter of the cylinder corrected for FCA_ml, [mm]
    """
    if type_of_wall_loss == 'internal':
        D_ml = D + 2 * FCA_ml
        text = f'D_ml = D + 2 * FCA_ml = {D} + 2 * {FCA_ml} = {D_ml}'
        data = DataCalculated(D_ml, text)
    elif type_of_wall_loss == 'external':
        D_ml = D
        text = f'D_ml = D = {D} = {D_ml}'
        data = DataCalculated(D_ml, text)
    return data


# # для теста
# D_ml = f_D_ml(type_of_wall_loss, D, FCA_ml).result


# step 4------------------------------------------------
def f_R_t(t_mm, FCA_ml, t_ml):
    """
    Remaining thickness ratio R_t, [-]
    """
    R_t = (t_mm - FCA_ml) / t_ml
    text = f'R_t = (t_mm - FCA_ml) / t_ml = ({t_mm} - {FCA_ml}) / {t_ml} = {R_t}'
    data = DataCalculated(R_t,text)
    return data


# # для теста
# R_t = f_R_t(t_mm, FCA_ml, t_ml).result


# step 5------------------------------------------------
def f_Q(R_t, RSF_a):
    """
    Parameter Q - Factor used to determine the length for thickness averaging based on an allowable Remaining Strength Factor
    and the remaining thickness ratio Rt. Table 4.8 [-].

    RSF_a - Allowable remaining strength factor.
    Recommended Remaining Strength Factor RSFa is 0.90
    """
    if R_t < RSF_a:
        Q = 1.123 * (((1 - R_t) / (1 - R_t / RSF_a)) ** 2 - 1) ** (0.5)
        text = f'Q = 1.123 * (((1 - R_t) / (1 - R_t  /  RSF_a))^2 - 1)^0.5 = 1.123 * (((1 - {R_t}) / (1 - {R_t}  /  {RSF_a}))^2 - 1)^0.5 = {Q}'
    elif R_t >= RSF_a:
        Q = 50
        text = f'Q = {Q}'
    data = DataCalculated(Q, text)
    return data


# # для теста
# Q = f_Q(R_t, RSF_a).result


# step 6------------------------------------------------
def f_L(Q, D_ml, t_ml):
    """
    Length for thickness averaging L, [mm]
    """
    L = Q * (D_ml * t_ml) ** 0.5
    text = f'L = Q * (D_ml * t_ml) ^ 0.5 = {Q} * ({D_ml} * {t_ml}) ^ 0.5 = {L}'
    data = DataCalculated(L, text)
    return data

# # для теста
# L = f_L(Q, D_ml, t_ml).result

# step 7------------------------------------------------
def f_t_minC(P, D_0, S, E, Y_B31, MA):
    """
    Minimum required thickness based on the
    circumferential stress, [mm]
    """
    t_minC = (P * D_0 / 10) / (2 * (S * E + P / 10 * Y_B31)) + MA
    text = f't_minC = (P * D_0) / (2 * (S * E + P * Y_B31)) + MA = ({P} * {D_0} / 10) / (2 * ({S} * {E} + {P} / 10 * {Y_B31})) + {MA} = {P}'
    data = DataCalculated(t_minC, text)
    return data


# # для теста
# t_minC = f_t_minC(P, D_0, S, E, Y_B31, MA).result


def f_t_minL(P, D_0, S, E, Y_B31, MA, t_sl):
    """
    Minimum required thickness based on the
    longitudinal stress, [mm]
    """
    t_minL = (P * D_0 / 10) / (4 * (S * E + P / 10 * Y_B31)) + t_sl + MA
    text = f't_minL = (P * D_0) / (4 * (S * E + P * Y_B31)) + t_sl + MA = ({P} * {D_0} / 10) / (4 * ({S} * {E} + {P} / 10 * {Y_B31})) + {t_minL} = {t_minL}'
    data = DataCalculated(t_minL, text)
    return data


# # для теста
# t_minL = f_t_minL(P, D_0, S, E, Y_B31, MA).result


def f_t_min(t_minC, t_minL):
    """
    Minimum required thickness , [mm]
    """
    t_min = max(t_minC, t_minL)
    text = f't_min = max(t_minC; t_minL) = max({t_minC}; {t_minL}) = {t_min}'
    data = DataCalculated(t_min, text)
    return data


# # для теста
# t_min = f_t_min(t_minC, t_minL).result


# step 8------------------------------------------------
def f_MAWP_C(S, E, t_c, MA, D_0, Y_B31):
    """
    Maximum allowable working pressure based on circumferential stress, [bar]
    """
    MAWP_C = 10 * (2 * S * E * (t_c - MA)) / (D_0 - 2 * Y_B31 * (t_c - MA))
    text = f'MAWP_C = (2 * S * E * (t_c - MA)) / (D_0 - 2 * Y_B31 * (t_c - MA)) = 10 * (2 * {S} * {E} * ({t_c} - {MA})) / ({D_0} - 2 * {Y_B31} * ({t_c} - {MA})) = {MAWP_C}'
    data = DataCalculated(MAWP_C, text,)
    return data


# # для теста
# MAWP_C = f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).result


def f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl):
    """
    Maximum allowable working pressure based on longitudinal stress, [bar]
    """
    MAWP_L = 10 * (4 * S * E * (t_c - t_sl - MA)) / (D_0 - 4 * Y_B31 * (t_c - t_sl - MA))
    text = f'MAWP_L = (4 * S * E * (t_c - t_c - t_sl - MA)) / (D_0 - 4 * Y_B31 * (t_c - t_sl - MA)) = 10 * (4 * {S} * {E} * ({t_c} - {t_sl} - {MA})) / ({D_0} - 4 * {Y_B31} * ({t_c} - {t_sl} - {MA})) = {MAWP_L}'
    data = DataCalculated(MAWP_L, text)
    return data


# # для теста
# MAWP_L = f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).result


def f_MAWP(MAWP_C, MAWP_L):
    """
    Maximum allowable working pressure, [bar]
    """
    MAWP = min(MAWP_C, MAWP_L)
    text = f'MAWP = min(MAWP_C; MAWP_L) = min({MAWP_C}; {MAWP_L}) = {MAWP}'
    data = DataCalculated(MAWP, text)
    return data

# # для теста
# MAWP = f_MAWP(MAWP_C, MAWP_L).result

# step 9------------------------------------------------
def check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC):
    """
    Average Measured Thickness from Critical Thickness Profiles based on the
    longitudinal CTP determined at the time of the inspection
    """
    if (t_amS - FCA_ml) >= t_minC:
        average_longitudinal_thickness_criteria = 'passed'
        text = f'(t_amS - FCA_ml) >= t_minL |---> ({t_amS} - {FCA_ml}) >= {t_minC} |---> Average longitudinal thickness criteria is -> {average_longitudinal_thickness_criteria}'
    elif (t_amS - FCA_ml) < t_minC:
        average_longitudinal_thickness_criteria = 'failed'
        text = f'(t_amS - FCA_ml) < t_minL |---> ({t_amS} - {FCA_ml}) < {t_minC} |---> Average longitudinal thickness criteria is -> {average_longitudinal_thickness_criteria}'
    data = DataCalculated(average_longitudinal_thickness_criteria, text)
    return data


def check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL):
    """
    Average Measured Thickness from Critical Thickness Profiles based on the
    circumferential CTP determined at the time of the inspection
    """
    if (t_amC - FCA_ml) >= t_minL:
        average_circumferential_thickness_criteria = 'passed'
        text = f'(t_amC - FCA_ml) >= t_minL |---> ({t_amC} - {FCA_ml}) >= {t_minL} |---> Average circumferential thickness criteria is -> {average_circumferential_thickness_criteria}'
    elif (t_amC - FCA_ml) < t_minL:
        average_circumferential_thickness_criteria = 'failed'
        text = f'(t_amC - FCA_ml) < t_minL |---> ({t_amC} - {FCA_ml}) < {t_minL} |---> Average circumferential thickness criteria is -> {average_circumferential_thickness_criteria}'
    data = DataCalculated(average_circumferential_thickness_criteria, text)
    return data

# step 10------------------------------------------------
def f_MAWP_rC(S, E, t_amS, FCA_ml, D_0, Y_B31):
    """
    MAWP_rC - Reduced MAWP of a conical or cylindrical shell based on the stresses in the
    circumferential or hoop direction, [bar]
    """
    MAWP_rC = 10 * (2 * S * E * (t_amS - FCA_ml)) / (D_0 - 2 * Y_B31 * (t_amS - FCA_ml))
    text = f'MAWP_rC = (2 * S * E * (t_amS - FCA_ml)) / (D_0 - 2 * Y_B31 * (t_amS - FCA_ml)) = 10 * (2 * {S} * {E} * ({t_amS} - {FCA_ml})) / ({D_0} - 2 * {Y_B31} * ({t_amS} - {FCA_ml})) = {MAWP_rC}'
    data = DataCalculated(MAWP_rC, text)
    return data

# # для теста
# MAWP_rC = f_MAWP_rC(S, E, t_amS, FCA_ml, D_0, Y_B31).result


def f_MAWP_rL(S, E, t_amC, FCA_ml, D_0, Y_B31):
    """
    MAWP_rL - Reduced MAWP of a conical or cylindrical shell based on the stresses in the
    longitudinal direction, [bar]
    """
    MAWP_rL = 10 * (4 * S * E * (t_amC - FCA_ml)) / (D_0 - 4 * Y_B31 * (t_amC - FCA_ml))
    text = f'MAWP_rL = (4 * S * E * (t_amC - FCA_ml )) / (D_0 - 4 * Y_B31 * (t_amC - FCA_ml)) = 10 * (4 * {S} * {E} * ({t_amC} - {FCA_ml})) / ({D_0} - 4 * {Y_B31} * ({t_amC} - {FCA_ml})) = {MAWP_rL}'
    data = DataCalculated(MAWP_rL, text)
    return data


# # для теста
# MAWP_rL = f_MAWP_rL(S, E, t_amC, FCA_ml, D_0, Y_B31).result


def check_MAWP_criteria(MAWP_rC, MAWP_rL, P):
    """
    MAWP criteria from Critical Thickness Profiles
    """
    if min(MAWP_rC, MAWP_rL) > P:
        MAWP_criteria = 'passed'
        text = f'min(MAWP_rC,MAWP_rL) > P |---> min({MAWP_rC},{MAWP_rL}) > {P} |---> MAWP criteria is -> {MAWP_criteria}'
    elif min(MAWP_rC, MAWP_rL) <= P:
        MAWP_criteria = 'failed'
        text = f'min(MAWP_rC,MAWP_rL) <= P |---> min({MAWP_rC},{MAWP_rL}) <= {P} |---> MAWP criteria is -> {MAWP_criteria}'
    data = DataCalculated(MAWP_criteria, text)
    return data


#  step 11------------------------------------------------
def f_t_lim(t_nom: float) -> float:
    """
    t_lim - Parameter which is needed for Minimum measured thickness criteria, [mm]
    """
    if (0.2 * t_nom) > 1.3:
        t_lim = 0.2 * t_nom
        text = f't_lim  = max(0.2  *  t_nom; 1.3) |---> t_lim = max(0.2  *  {t_nom}; 1.3) |---> t_lim = {t_lim}'
    else:
        t_lim = 1.3
        text = f't_lim  = max(0.2  *  t_nom; 1.3) |---> t_lim = max(0.2  *  {t_nom}; 1.3) |---> t_lim = {t_lim}'
    data = DataCalculated(t_lim, text)
    return data


# # для теста
# t_lim = f_t_lim(t_nom).result


def check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim):
    if (t_mm - FCA_ml) >= max((0.5 * t_min), t_lim):
        minimum_thickness_criteria = 'passed'
        text = f'(t_mm - FCA_ml) >= max((0.5 * t_min), t_lim) |---> ({t_mm} - {FCA_ml}) >= max((0.5 * {t_min}, {t_lim})) |---> ({t_mm - FCA_ml}) >= ({max((0.5 * t_min), t_lim)}) |---> Minimum thickness criteria is -> {minimum_thickness_criteria}'
    else:
        minimum_thickness_criteria = 'failed'
        text = f'(t_mm - FCA_ml) < max((0.5 * t_min), t_lim) |---> ({t_mm} - {FCA_ml}) < max((0.5 * {t_min}, {t_lim})) |---> ({t_mm - FCA_ml}) < ({max((0.5 * t_min), t_lim)}) |---> Minimum thickness criteria is -> {minimum_thickness_criteria}'
    data = DataCalculated(minimum_thickness_criteria, text)
    return data


# if __name__ == '__main__':
#     print('t_nom = ', f_t_nom(pipe_type, t, M_ut))
#     print('')
#     print('t_ml = ', f_t_ml(t_nom, FCA_ml))
#     print('')
#     print('t_c = ', f_t_c(t_nom, LOSS, FCA))
#     print('')
#     print('D = ', f_D(D_0, t_nom))
#     print('')
#     print('D_ml = ', f_D_ml(type_of_wall_loss, D, FCA_ml))
#     print('')
#     print('R_t = ', f_R_t(t_mm, FCA_ml, t_ml))
#     print('')
#     print('Q = ', f_Q(R_t, RSF_a))
#     print('')
#     print('L = ', f_L(Q, D_ml, t_ml))
#     print('')
#     print('t_minC = ', f_t_minC(P, D_0, S, E, Y_B31, MA))
#     print('')
#     print('t_minL = ', f_t_minL(P, D_0, S, E, Y_B31, MA))
#     print('')
#     print('t_min = ', f_t_min(t_minC, t_minL))
#     print('')
#     print('MAWP_C = ', f_MAWP_C(S, E, t_c, MA, D_0, Y_B31))
#     print('')
#     print('MAWP_L = ', f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl))
#     print('')
#     print('MAWP = ', f_MAWP(MAWP_C, MAWP_L))
#     print('')
#     print(
#         f'(t_amS - FCA_ml) >= t_minC |---> ({t_amS} - {FCA_ml}) >= {t_minC} |---> Average longitudinal thickness criteria is -> ',
#         check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC))
#     print('')
#     print(
#         f'(t_amC - FCA_ml) >= t_minL |---> ({t_amC} - {FCA_ml}) >= {t_minL} |---> Average circumferential thickness criteria is -> ',
#         check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL))
#     print('')
#     print(
#         f'MAWP_rC = (2 * S * E * (t_amS - FCA_ml)) / (D_0 - 2 * Y_B31 * (t_amS - FCA_ml)) = 10 * (2 * {S} * {E} * ({t_amS} - {FCA_ml})) / ({D_0} - 2 * {Y_B31} * ({t_amS} - {FCA_ml})) = ',
#         f_MAWP_rC(S, E, t_amS, FCA_ml, D_0, Y_B31))
#     print('')
#     print(
#         f'MAWP_rL = (4 * S * E * (t_amC - FCA_ml )) / (D_0 - 4 * Y_B31 * (t_amC - FCA_ml)) = 10 * (4 * {S} * {E} * ({t_amC} - {FCA_ml})) / ({D_0} - 4 * {Y_B31} * ({t_amC} - {FCA_ml})) = ',
#         f_MAWP_rL(S, E, t_amC, FCA_ml, D_0, Y_B31))
#     print('')
#     print(f'min(MAWP_rC,MAWP_rL) > P |---> min({MAWP_rC},{MAWP_rL}) > {P} |---> MAWP criteria is -> ',
#           check_MAWP_criteria(MAWP_rC, MAWP_rL, P))
#     print('')
#     print(f't_lim =  ', f_t_lim(t_nom))
#     print('')
#     print(f'minimum_thickness_criteria is ->', check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim))t_min
