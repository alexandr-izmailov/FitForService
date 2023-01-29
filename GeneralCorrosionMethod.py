# input data
t = 3.7592
pipe_type = 'Seamless'
M_ut = 0
FCA_ml = 0.14

# function definition
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
    return t_nom, text

def f_t_ml(FCA_ml):
   """
   t_ml - Nominal thickness in the region of corrosion corrected FCA_ml, [mm]
   """
   t_nom, text = f_t_nom(pipe_type, t, M_ut)
   t_ml = t_nom - FCA_ml
   text = f't_ml = t_nom - FCA_ml = {t_nom} - {FCA_ml} = {t_ml}'
   return t_ml, text

if __name__ == '__main__':
    print(f_t_nom(pipe_type, t, M_ut))
    print('')
    print(f_t_ml(FCA_ml))
