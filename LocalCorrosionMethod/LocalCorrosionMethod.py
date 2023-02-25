from Classes.MajorClasses import DataCalculated

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



# function definition
# step 1.1 ------------------------------------------------
def f_t_nom(pipe_type, t, M_ut):
    """"
    t_nom - Nominal or furnished thickness of the component adjusted for mill undertolerance as applicable, [mm]
    """
    if pipe_type in ('Seamless', 'User defined %'):
        t_nom = t * (1 - M_ut / 100)
        text = f't_nom = t * (1 - M_ut / 100) = {t} * (1 - {M_ut} / 100) = {t_nom}'
        data = DataCalculated(t_nom, text)
    elif pipe_type in ('Welded', 'User defined mm'):
        t_nom = t - M_ut
        text = f't_nom = t - M_ut = {t} - {M_ut} = {t_nom}'
        data = DataCalculated(t_nom, text)
    return data

# для теста
t_nom = f_t_nom(pipe_type, t, M_ut).result

# step 1 ------------------------------------------------
def f_t_c(t_nom, LOSS, FCA):
    """
    t_c - Future corroded wall thickness away from the damage area, [mm]
    """
    t_c = t_nom - LOSS - FCA
    text = f't_c = t_nom - LOSS - FCA = {t_nom} - {LOSS} - {FCA} = {t_c}'
    data = DataCalculated(t_c, text)
    return data

# для теста
t_c = f_t_c(t_nom, LOSS, FCA).result

# step 2 --------------------------------------------------
def f_R_t(t_mm, FCA_ml, t_c):
    """
    R_t - Remaining thickness ratio, [-]
    """
    R_t = (t_mm - FCA_ml) / t_c
    text = f'R_t = (t_mm - FCA_ml) / t_c = ({t_mm} - {FCA_ml}) / {t_c} = {R_t}'
    data = DataCalculated(R_t, text)
    return data

# для теста
R_t = f_R_t(t_mm, FCA_ml, t_c).result

def f_D(D_0, t_nom):
    """
    D - Inside diameter of the cylinder, cone (at the location of the flaw), [mm]
    """
    D = D_0 - 2 * t_nom
    text = f'D = D_0 - 2 * t_nom = {D_0} - 2 * {t_nom} = {D}'
    data = DataCalculated(D, text)
    return data

# для теста
D = f_D(D_0, t_nom).result

def f_λ(s, D, t_c):
    """
    λ - longitudinal flaw length parameter, [-]
    """
    λ = (1.285 * s ) / ((D * t_c) ** (0.5))
    text = f'λ = 1.285 * s / ((D * t_c) ** (0.5)) = 1.285 * {s} / (({D} * {t_c}) ** (0.5)) = {λ}'
    data = DataCalculated(λ, text)
    return data

# для теста
λ = f_λ(s, D, t_c)









if __name__ == '__main__':
    print('t_nom = ', f_t_nom(pipe_type, t, M_ut))
    print('')
    print('t_c = ', f_t_c(t_nom, LOSS, FCA))
    print('')
    print('R_t = ', f_R_t(t_mm, FCA_ml, t_c))
    print('')
    print('D = ', f_D(D_0, t_nom))
    print('')
    print('λ = ', f_λ(s, D, t_c))
