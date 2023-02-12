from GeneralCorrosionMethod import GeneralCorrosionMethod as g

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

method = 'general corrosion'

# algorithm
if method == 'general corrosion':
    # step 1 ----------------------------------------------------------------
    # Nominal or furnished thickness of the component adjusted for mill undertolerance as applicable, [mm]
    t_nom = g.f_t_nom(pipe_type, t, M_ut).result

    # Nominal thickness in the region of corrosion corrected FCA_ml, [mm]
    t_ml = g.f_t_ml(t_nom, FCA_ml).result

    # step 2 ----------------------------------------------------------------
    # Future corroded wall thickness away from the damage area, [mm]
    t_c = g.f_t_c(t_nom, LOSS, FCA).result

    # step 3 ----------------------------------------------------------------
    # Inside diameter of the cylinder, cone (at the location of the flaw), [mm]
    D = g.f_D(D_0, t_nom).result

    # Inside diameter of the cylinder corrected for FCA_ml, [mm]
    D_ml = g.f_D_ml(type_of_wall_loss, D, FCA_ml).result

    # step 4 ----------------------------------------------------------------
    # Remaining thickness ratio R_t, [-]
    R_t = g.f_R_t(t_mm, FCA_ml, t_ml).result

    # step 5 ----------------------------------------------------------------
    # Factor used to determine the length for thickness averaging based on an allowable Remaining Strength Factor and the remaining thickness ratio Rt, [-]
    Q = g.f_Q(R_t, RSF_a).result

    # step 6 ----------------------------------------------------------------
    #  Length for thickness averaging L, [mm]
    L = g.f_L(Q, D_ml, t_ml).result

    # step 7 ----------------------------------------------------------------
    # Minimum required thickness based on the circumferential stress, [mm]
    t_minC = g.f_t_minC(P, D_0, S, E, Y_B31, MA).result

    #  Minimum required thickness based on the longitudinal stress, [mm]
    t_minL = g.f_t_minL(P, D_0, S, E, Y_B31, MA, t_sl).result

    # Minimum required thickness , [mm]
    t_min = g.f_t_min(t_minC, t_minL).result

    # step 8 ----------------------------------------------------------------
    # Maximum allowable working pressure based on circumferential stress, [bar]
    MAWP_C = g.f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).result

    #  Maximum allowable working pressure based on longitudinal stress, [bar]
    MAWP_L = g.f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).result

    # Maximum allowable working pressure, [bar]
    MAWP = g.f_MAWP(MAWP_C, MAWP_L).result

    # step 9 ----------------------------------------------------------------
    # Average Measured Thickness from Critical Thickness Profiles based on the
    # longitudinal CTP determined at the time of the inspection
    average_longitudinal_thickness_criteria = g.check_average_longitudinal_thickness_criteria(t_amS, FCA_ml,
                                                                                              t_minC).result
    if average_longitudinal_thickness_criteria == 'failed':

        print(average_longitudinal_thickness_criteria)

    elif average_longitudinal_thickness_criteria == 'passed':

        # Average Measured Thickness from Critical Thickness Profiles based on the
        # circumferential CTP determined at the time of the inspection
        average_circumferential_thickness_criteria = g.check_average_circumferential_thickness_criteria(t_amC, FCA_ml,
                                                                                                        t_minL).result
        if average_circumferential_thickness_criteria == 'failed':

            print(average_circumferential_thickness_criteria)

        elif average_circumferential_thickness_criteria == 'passed':

            # step 10 ----------------------------------------------------------------
            # Reduced MAWP of a conical or cylindrical shell based on the stresses in the circumferential or hoop direction, [bar]
            MAWP_rC = g.f_MAWP_rC(S, E, t_amS, FCA_ml, D_0, Y_B31).result

            # Reduced MAWP of a conical or cylindrical shell based on the stresses in the longitudinal direction, [bar]
            MAWP_rL = g.f_MAWP_rL(S, E, t_amC, FCA_ml, D_0, Y_B31).result

            #  MAWP criteria from Critical Thickness Profiles
            MAWP_criteria = g.check_MAWP_criteria(MAWP_rC, MAWP_rL, P).result

            if MAWP_criteria == 'failed':

                print(MAWP_criteria)

            elif MAWP_criteria == 'passed':

                # step 11 ----------------------------------------------------------------
                # Parameter which is needed for Minimum measured thickness criteria, [mm]
                t_lim = g.f_t_lim(t_nom).result

                # Minimum measured thickness criteria
                check_minimum_thickness_criteria = g.check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).result

                if check_minimum_thickness_criteria == 'failed':

                    print(check_minimum_thickness_criteria)

                elif check_minimum_thickness_criteria == 'passed':

                    print(check_minimum_thickness_criteria)






elif method == 'local corrosion':
    pass
