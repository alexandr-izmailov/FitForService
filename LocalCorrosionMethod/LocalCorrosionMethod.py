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

# step 2 --------------------------------------------------
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

def f_λ(s, D, t_c):
    """
    λ - longitudinal flaw length parameter, [-]
    """
    λ = (1.285 * s ) / ((D * t_c) ** (0.5))
    text = f'λ = 1.285 * s / ((D * t_c) ** (0.5)) = 1.285 * {s} / (({D} * {t_c})^(0.5)) = {λ}'
    data = DataCalculated(λ, text)
    return data

# # для теста
# λ = f_λ(s, D, t_c).result

# step 3 --------------------------------------------------
def f_R_t(t_mm, FCA_ml, t_c):
    """
    R_t - Remaining thickness ratio, [-]
    """
    R_t = (t_mm - FCA_ml) / t_c
    text = f'R_t = (t_mm - FCA_ml) / t_c = ({t_mm} - {FCA_ml}) / {t_c} = {R_t}'
    data = DataCalculated(R_t, text)
    return data

# # для теста
# R_t = f_R_t(t_mm, FCA_ml, t_c).result

def check_R_t(R_t):
    if R_t >= 0.2:
        check_R_t = 'passed'
        text = f'As R_t >= 0.2 \n{R_t} >= 0.2 |---> R_t check is -> {check_R_t}'
    else:
        check_R_t = 'failed'
        text = f'As R_t < 0.2 \n{R_t} < 0.2 |---> R_t check is -> {check_R_t}'
    data = DataCalculated(check_R_t, text)
    return data

def check_thickness(t_mm, FCA_ml):
    if t_mm - FCA_ml >= 1.3:
        check_thickness = 'passed'
        text = f'As t_mm - FCA_ml >= 1.3 ---> {t_mm} - {FCA_ml} >= 1.3 \n{t_mm - FCA_ml} >= 1.3  |---> Thickness check is -> {check_thickness}'
    else:
        check_thickness = 'failed'
        text = f'As t_mm - FCA_ml < 1.3 ---> {t_mm} - {FCA_ml} < 1.3 \n{t_mm - FCA_ml} < 1.3  |---> Thickness check is -> {check_thickness}'
    data = DataCalculated(check_thickness, text)
    return data

def check_L_msd_criteria(L_msd, D, t_c):
    if L_msd >= 1.8 * (D * t_c)**(0.5):
        L_msd_criteria = 'passed'
        text = f'As L_msd >= 1.8 * (D * t_c)^(0.5) ---> {L_msd} >= 1.8 * ({D} * {t_c})**(0.5) \n {L_msd} >= {1.8 * (D * t_c)**(0.5)} |---> L_msd criteria is -> {L_msd_criteria}'
    else:
        L_msd_criteria = 'failed'
        text = f' As L_msd < 1.8 * (D * t_c)^(0.5) ---> {L_msd} < 1.8 * ({D} * {t_c})**(0.5) \n {L_msd} < {1.8 * (D * t_c) ** (0.5)} |---> L_msd criteria is -> {L_msd_criteria}'
    data = DataCalculated(L_msd_criteria, text)
    return data

# step 4 --------------------------------------------------
def check_Groove_flaw_criteria(g_r, R_t, t_c):
    if g_r / ((1 - R_t) * t_c) >= 0.5:
        groove_flaw_criteria = 'passed'
        text = f'As g_r / ((1 - R_t) * t_c) >= 0.5 ---> {g_r} / ((1 - {R_t}) * {t_c}) >= 0.5 \n{g_r / ((1 - R_t) * t_c)} >= 0.5 |---> Level 1 is {groove_flaw_criteria}'
    else:
        groove_flaw_criteria = 'failed'
        text = f'As g_r / ((1 - R_t) * t_c) < 0.5 ---> {g_r} / ((1 - {R_t}) * {t_c}) < 0.5 \n{g_r / ((1 - R_t) * t_c)} < 0.5 |---> Level 1 is {groove_flaw_criteria}'
    data = DataCalculated(groove_flaw_criteria, text)
    return data

# step 5 --------------------------------------------------
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

# step 6 --------------------------------------------------
def f_M_t(λ):
    """
    Folias factor based on the longitudinal extent of the LTA for a through-wall flaw, [-]
    """
    M_t = 1.0010 - 0.014195 * λ + 0.29090 * λ**2 - 0.096420 * λ**3 + 0.020890 * λ**4 - 0.0030540 * λ**5 + 2.9570 * 10**(-4) * λ**6 - 1.8462 * 10**(-5) * λ**7 + 7.1553 * 10**(-7) * λ**8 - 1.5631 * 10**(-8) * λ**9 + 1.4656 * 10**(-10) * λ**10
    text = f'M_t = 1.0010 - 0.014195 * λ + 0.29090 * λ**2 - 0.096420 * λ**3 + 0.020890 * λ**4 - 0.0030540 * λ**5 + 2.957 * 10**(-4) * λ**6 - 1.8462 * 10**(-5) * λ**7 + 7.1553 * 10**(-7) * λ**8 - 1.5631 * 10**(-8) * λ**9 + 1.4656 * 10**(-10) * λ**10 = {M_t}'
    data = DataCalculated(M_t, text)
    return data

# # для теста
# M_t = f_M_t(λ).result

def check_screening_criteria(λ, R_t, RSF_a, M_t):
    """
    Level 1 - Screening criteria for Local Metal Loss in a cylindrical shell
    """
    if λ <= 0.354:
        if R_t > 0.2:
            screening_criteria = 'acceptable'
            text = f'As λ <= 0.354 and R_t > 0.2 |---> Screening criteria for Local Metal Loss in a cylindrical shell is -> {screening_criteria}'
        else:
            screening_criteria = 'NOT acceptable'
            text = f'As λ <= 0.354 but R_t <= 0.2 |---> Screening criteria for Local Metal Loss in a cylindrical shell is -> {screening_criteria}'
    elif 0.354 < λ and λ < 20:
        R_t_curve = (RSF_a - RSF_a / M_t) * (1.0 - RSF_a / M_t) ** (-1)
        if R_t > R_t_curve:
            screening_criteria = 'acceptable'
            text = f'As 0.354 < λ < 20 and R_t > (RSF_a - RSF_a / M_t) * (1.0 - RSF_a / M_t)^(-1) ---> {R_t} > ({RSF_a} - {RSF_a} / {M_t}) * (1.0 - {RSF_a} / {M_t})^(-1) \n{R_t} > {R_t_curve} |---> Screening criteria for Local Metal Loss in a cylindrical shell is -> {screening_criteria}'
        else:
            screening_criteria = 'NOT acceptable'
            text = f'As 0.354 < λ < 20 and R_t <= (RSF_a - RSF_a / M_t) * (1.0 - RSF_a / M_t)^(-1) ---> {R_t} <= ({RSF_a} - {RSF_a} / {M_t}) * (1.0 - {RSF_a} / {M_t})^(-1) \n{R_t} <= {R_t_curve} |---> Screening criteria for Local Metal Loss in a cylindrical shell is -> {screening_criteria}'
    elif λ >= 20:
        if R_t > 0.9:
            screening_criteria = 'acceptable'
            text = f'As λ >= 20 and R_t > 0.9 |---> Screening criteria for Local Metal Loss in a cylindrical shell is -> {screening_criteria}'
        else:
            screening_criteria = 'NOT acceptable'
            text = f'As λ >= 20 and R_t <= 0.9 |---> Screening criteria for Local Metal Loss in a cylindrical shell is -> {screening_criteria}'
    data = DataCalculated(screening_criteria, text)
    return data

def f_RSF(R_t, M_t):
    """
    Computed remaining strength factor based on the meridional extent of the LTA, [-]
    """
    RSF = R_t / (1 - (1 / M_t) * (1 - R_t))
    text = f'RSF = R_t / (1 - (1 / M_t) * (1 - R_t)) = {R_t} / (1 - (1 / {M_t}) * (1 - {R_t})) = {RSF}'
    data = DataCalculated(RSF, text)
    return data

# # для теста
# RSF = f_RSF(R_t, M_t).result

def f_MAWPr(MAWP, RSF, RSF_a):
    """
    MAWPr -  Reduced maximum allowable working pressure of the damaged component, [bar]
    """
    if RSF < RSF_a:
        MAWPr = MAWP * (RSF / RSF_a)
        text = f'As RSF < RSF_a ---> {RSF} < {RSF_a} |---> MAWPr = MAWP * (RSF / RSF_a) =  {MAWP} * ({RSF} / {RSF_a}) = {MAWPr}'
    elif RSF >= RSF_a:
        MAWPr = MAWP
        text = f'As RSF >= RSF_a ---> {RSF} >= {RSF_a} |---> MAWPr = MAWP = {MAWPr}'
    data = DataCalculated(MAWPr, text)
    return data

# # для теста
# MAWPr = f_MAWPr(MAWP, RSF, RSF_a).result


# step 7 --------------------------------------------------
def check_circumferential_extent_criteria(c, s, EL, EC):
    """
    Circumferential extent of the flaw criteria
    """
    if c <= 2 * s * (EL / EC):
        circumferential_extent_criteria = 'passed'
        text = f'As c <= 2 * s * (EL / EC) ---> {c} <= 2 * {s} * ({EL} / {EC}) \n{c} <= {2 * s* (EL / EC)} |---> Circumferential extent of the flaw criteria is -> {circumferential_extent_criteria}'
    else:
        circumferential_extent_criteria = 'failed'
        text = f'As c > 2 * s * (EL / EC) ---> {c} > 2 * {s} * ({EL} / {EC}) \n{c} > {2 * s * (EL / EC)} |---> Circumferential extent of the flaw criteria is -> {circumferential_extent_criteria}'
    data = DataCalculated(circumferential_extent_criteria, text)
    return data

def f_t_minL(MAWPr, D_0, S, E, P, Y_B31, t_sl, MA):
    """
    Minimum required thickness for the component based on equipment design pressure or
    equipment MAWP for longitudinal stresses
    """
    t_minL = MAWPr * (D_0/10) / (4 * (S * E + P * (Y_B31/10))) + t_sl + MA
    text = f't_minL = MAWPr * D_0 / (4 * (S * E + P * Y_B31)) + t_sl + MA = {MAWPr} * ({D_0}/10) / (4 * ({S} * {E} + {P} * ({Y_B31}/10))) + {t_sl} + {MA} = {t_minL}'
    data = DataCalculated(t_minL, text)
    return data

# # для теста
# t_minL = f_t_minL(MAWPr, D_0, S, E, P, Y_B31, t_sl, MA).result

def check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml):
    """
    Minimum thickness required for longitudinal stresses criteria
    """
    if t_minL <= t_mm - FCA_ml:
        minimum_thickness_required_criteria = 'passed'
        text = f'As t_minL <= t_mm - FCA_ml --> {t_minL} <= {t_mm} - {FCA_ml} \n{t_minL} <= {t_mm - FCA_ml} |--->  Minimum thickness required for longitudinal stresses criteria is -> {minimum_thickness_required_criteria}'
    else:
        minimum_thickness_required_criteria = 'failed'
        text = f'As t_minL > t_mm - FCA_ml --> {t_minL} > {t_mm} - {FCA_ml} \n{t_minL} > {t_mm - FCA_ml} |--->  Minimum thickness required for longitudinal stresses criteria is -> {minimum_thickness_required_criteria}'
    data = DataCalculated(minimum_thickness_required_criteria, text)
    return data

def f_MAWPr_new(MAWPr, t_mm, FCA_ml, t_minL):
    """
    MAWRr reduction, [bar]
    """
    MAWPr_new = MAWPr * (t_mm - FCA_ml) / t_minL
    text = f'MAWPr_new = MAWPr * (t_mm - FCA_ml) / t_minL = {MAWPr} * ({t_mm} - {FCA_ml}) / {t_minL} = {MAWPr_new}'
    data = DataCalculated(MAWPr_new, text)
    return data

# if __name__ == '__main__':
#     print('t_nom = ', f_t_nom(pipe_type, t, M_ut))
#     print('')
#     print('t_c = ', f_t_c(t_nom, LOSS, FCA))
#     print('')
#     print('R_t = ', f_R_t(t_mm, FCA_ml, t_c))
#     print('')
#     print('D = ', f_D(D_0, t_nom))
#     print('')
#     print('λ = ', f_λ(s, D, t_c))
#     print('')
#     print('check_R_t = ', check_R_t(R_t))
#     print('')
#     print('thickness check is', check_thickness(t_mm, FCA_ml))
#     print('')
#     print('L_msd_criteria is ', check_L_msd_criteria(L_msd, D, t_c))
#     print('')
#     print('Groove like flaw criteria is ', check_Groove_flaw_criteria(g_r, R_t, t_c))
#     print('')
#     print('MAWP_C = ', f_MAWP_C(S, E, t_c, MA, D_0, Y_B31))
#     print('')
#     print('MAWP_L = ', f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl))
#     print('')
#     print('MAWP = ', f_MAWP(MAWP_C, MAWP_L))
#     print('')
#     print('M_t = ', f_M_t(λ))
#     print('')
#     print('check_screening_criteria ', check_screening_criteria(λ, R_t, RSF_a, M_t))
#     print('')
#     print('RSF = ', f_RSF(R_t, M_t))
#     print('')
#     print('MAWPr =', f_MAWPr(MAWP, RSF, RSF_a))
#     print('')
#     print('circumferential_extent_criteria = ',  check_circumferential_extent_criteria(c, s, EL, EC))
#     print('')
#     print('t_minL = ', f_t_minL(MAWPr, D_0, S, E, P, Y_B31, t_sl, MA))
#     print('')
#     print('minimum_thickness_required_criteria = )', check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml))
#     print('')
#     print(' MAWPr_new ',  f_MAWPr_new(MAWPr, t_mm, FCA_ml, t_minL))