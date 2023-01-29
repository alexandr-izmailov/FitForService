# input data
t = 3.7592
pipe_type = 'Seamless'
M_ut = 0


def f_t_nom(pipe_type, t, M_ut):
    """"
    t_nom - nominal or furnished thickness of the component adjusted for mill undertolerance as applicable, [mm]
    """
    t_nom = 0.00000
    text = ''
    if pipe_type == 'Seamless' or pipe_type == 'User defined %':
        t_nom = t * (1 - M_ut)
        text = f't_nom = t * (1 - M_ut) = {t} * (1 - {M_ut}) = {t_nom}'
    elif pipe_type == 'Welded' or pipe_type == 'User defined mm':
        t_nom = t - M_ut
        text = f't_nom = t - M_ut = {t} - {M_ut} = {t_nom}'
    return t_nom, text
def t_ml():
    pass


if __name__ == '__main__':
    print(f_t_nom(pipe_type, t, M_ut))
