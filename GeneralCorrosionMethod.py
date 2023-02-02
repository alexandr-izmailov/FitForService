# input data
t = 3.7592
pipe_type = 'Seamless'
M_ut = 0
FCA_ml = 0.14
LOSS = 0
FCA = 0
type_of_wall_loss = 'internal'


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


# step 2 ------------------------------------------------
def f_t_c(t_nom, LOSS, FCA):
    """
    t_c - Future corroded wall thickness away from the damage area, [mm]
    """
    t_c = t_nom - LOSS - FCA
    text = f't_c = t_nom - LOSS - FCA = {t_nom} - {LOSS} - {FCA} = {t_c}'
    return t_c

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
def D_ml(type_of_wall_loss, D, FCA_ml):
    """
    D_ml - Inside diameter of the cylinder corrected for FCA_ml, [mm]
    """
    if type_of_wall_loss == 'internal':
        D_ml = D + 2 * FCA_ml
        text = f'D_ml = D + 2 * FCA_ml = {D} + 2 * {FCA_ml} = {D_ml}'
    elif type_of_wall_loss == 'external':
        D_ml = D
    return D_ml




if __name__ == '__main__':
    print('t_nom = ', f_t_nom(pipe_type, t, M_ut))
    print('')
    print('t_ml = ', f_t_ml(t_nom, FCA_ml))
    print('')
    print('t_c = ', f_t_c(t_nom, LOSS, FCA))
    print('')
    print('D = ', f_D(D_0, t_nom))
    print('')
    print('D_ml = ', D_ml(type_of_wall_loss, D, FCA_ml))