from GeneralCorrosionMethod import GeneralCorrosionMethod as g
from Document.DocumentProccess import adjust_document, save_new_report_file

# Set the directory where the file should be saved
directory = r"..\reports"

def gc_algorithm():
    document = adjust_document()

    passing_text_line = 'Fitness for Service Level 1 criteria passed'
    failing_text_line = "Fitness for Service Level 1 criteria failed"

    # input data
    t = 3.7592
    pipe_type = 'user defined %'
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

    input_data_text = ""
    short_report_text = ""
    short_report_list = list()

    document.add_paragraph(input_data_text)

    # algorithm

    # step 1 ----------------------------------------------------------------
    document.add_paragraph('STEP 1')

    # Nominal or furnished thickness of the component adjusted for mill undertolerance as applicable, [mm]
    t_nom = g.f_t_nom(pipe_type, t, M_ut).result
    document.add_paragraph(g.f_t_nom(pipe_type, t, M_ut).text)

    # Nominal thickness in the region of corrosion corrected FCA_ml, [mm]
    t_ml = g.f_t_ml(t_nom, FCA_ml).result
    document.add_paragraph(g.f_t_ml(t_nom, FCA_ml).text)

    # step 2 ----------------------------------------------------------------
    document.add_paragraph('STEP 2')

    # Future corroded wall thickness away from the damage area, [mm]
    t_c = g.f_t_c(t_nom, LOSS, FCA).result
    document.add_paragraph(g.f_t_c(t_nom, LOSS, FCA).text)


    # step 3 ----------------------------------------------------------------
    document.add_paragraph('STEP 3')

    # Inside diameter of the cylinder, cone (at the location of the flaw), [mm]
    D = g.f_D(D_0, t_nom).result
    document.add_paragraph(g.f_D(D_0, t_nom).text)

    # Inside diameter of the cylinder corrected for FCA_ml, [mm]
    D_ml = g.f_D_ml(type_of_wall_loss, D, FCA_ml).result
    document.add_paragraph(g.f_D_ml(type_of_wall_loss, D, FCA_ml).text)

    # step 4 ----------------------------------------------------------------
    document.add_paragraph('STEP 4')

    # Remaining thickness ratio R_t, [-]
    R_t = g.f_R_t(t_mm, FCA_ml, t_ml).result
    document.add_paragraph(g.f_R_t(t_mm, FCA_ml, t_ml).text)

    # step 5 ----------------------------------------------------------------
    document.add_paragraph('STEP 5')

    # Factor used to determine the length for thickness averaging based on an allowable Remaining Strength Factor and the remaining thickness ratio Rt, [-]
    Q = g.f_Q(R_t, RSF_a).result
    document.add_paragraph(g.f_Q(R_t, RSF_a).text)

    # step 6 ----------------------------------------------------------------
    document.add_paragraph('STEP 6')

    #  Length for thickness averaging L, [mm]
    L = g.f_L(Q, D_ml, t_ml).result
    document.add_paragraph(g.f_L(Q, D_ml, t_ml).text)

    # step 7 ----------------------------------------------------------------
    document.add_paragraph('STEP 7')

    # Minimum required thickness based on the circumferential stress, [mm]
    t_minC = g.f_t_minC(P, D_0, S, E, Y_B31, MA).result
    document.add_paragraph(g.f_t_minC(P, D_0, S, E, Y_B31, MA).text)

    #  Minimum required thickness based on the longitudinal stress, [mm]
    t_minL = g.f_t_minL(P, D_0, S, E, Y_B31, MA, t_sl).result
    document.add_paragraph(g.f_t_minL(P, D_0, S, E, Y_B31, MA, t_sl).text)

    # Minimum required thickness , [mm]
    t_min = g.f_t_min(t_minC, t_minL).result
    document.add_paragraph( g.f_t_min(t_minC, t_minL).text)

    # step 8 ----------------------------------------------------------------
    document.add_paragraph('STEP 8')

    # Maximum allowable working pressure based on circumferential stress, [bar]
    MAWP_C = g.f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).result
    document.add_paragraph(g.f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).text)

    #  Maximum allowable working pressure based on longitudinal stress, [bar]
    MAWP_L = g.f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).result
    document.add_paragraph(g.f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).text)

    # Maximum allowable working pressure, [bar]
    MAWP = g.f_MAWP(MAWP_C, MAWP_L).result
    document.add_paragraph(g.f_MAWP(MAWP_C, MAWP_L).text)

    # step 9 ----------------------------------------------------------------
    document.add_paragraph('STEP 9')

    # Average Measured Thickness from Critical Thickness Profiles based on the
    # longitudinal CTP determined at the time of the inspection
    if g.check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC).result == 'failed':

        document.add_paragraph(g.check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC).text)
        short_report_list.append(g.check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC).text)

        document.add_paragraph(failing_text_line)
        short_report_list.append(failing_text_line)

    elif g.check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC).result == 'passed':

        document.add_paragraph(g.check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC).text)
        short_report_list.append(g.check_average_longitudinal_thickness_criteria(t_amS, FCA_ml, t_minC).text)

        # Average Measured Thickness from Critical Thickness Profiles based on the
        # circumferential CTP determined at the time of the inspection
        if g.check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL).result == 'failed':

            document.add_paragraph(g.check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL).text)
            short_report_list.append(g.check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL).text)

            document.add_paragraph(failing_text_line)
            short_report_list.append(failing_text_line)

        elif g.check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL).result == 'passed':

            document.add_paragraph(g.check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL).text)
            short_report_list.append(g.check_average_circumferential_thickness_criteria(t_amC, FCA_ml, t_minL).text)

            # step 10 ----------------------------------------------------------------
            document.add_paragraph('STEP 10')

            # Reduced MAWP of a conical or cylindrical shell based on the stresses in the circumferential or hoop direction, [bar]
            MAWP_rC = g.f_MAWP_rC(S, E, t_amS, FCA_ml, D_0, Y_B31).result
            document.add_paragraph(g.f_MAWP_rC(S, E, t_amS, FCA_ml, D_0, Y_B31).text)

            # Reduced MAWP of a conical or cylindrical shell based on the stresses in the longitudinal direction, [bar]
            MAWP_rL = g.f_MAWP_rL(S, E, t_amC, FCA_ml, D_0, Y_B31).result
            document.add_paragraph(g.f_MAWP_rL(S, E, t_amC, FCA_ml, D_0, Y_B31).text)

            #  MAWP criteria from Critical Thickness Profiles
            if g.check_MAWP_criteria(MAWP_rC, MAWP_rL, P).result == 'failed':

                document.add_paragraph(g.check_MAWP_criteria(MAWP_rC, MAWP_rL, P).text)
                short_report_list.append(g.check_MAWP_criteria(MAWP_rC, MAWP_rL, P).text)

                document.add_paragraph(failing_text_line)
                short_report_list.append(failing_text_line)

            elif g.check_MAWP_criteria(MAWP_rC, MAWP_rL, P).result == 'passed':

                document.add_paragraph(g.check_MAWP_criteria(MAWP_rC, MAWP_rL, P).text)
                short_report_list.append(g.check_MAWP_criteria(MAWP_rC, MAWP_rL, P).text)

                # step 11 ----------------------------------------------------------------
                document.add_paragraph('STEP 11')

                # Parameter which is needed for Minimum measured thickness criteria, [mm]
                t_lim = g.f_t_lim(t_nom).result
                document.add_paragraph(g.f_t_lim(t_nom).text)

                # Minimum measured thickness criteria
                if g.check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).result == 'failed':

                    document.add_paragraph(g.check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).text)
                    short_report_list.append(g.check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).text)

                    document.add_paragraph(failing_text_line)
                    short_report_list.append(failing_text_line)

                elif g.check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).result == 'passed':

                    document.add_paragraph(g.check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).text)
                    short_report_list.append(g.check_minimum_thickness_criteria(t_mm, FCA_ml, t_min, t_lim).text)

                    document.add_paragraph(passing_text_line)
                    short_report_list.append(passing_text_line)

    short_report_text = '\n'.join(short_report_list)

    return short_report_text, document

if __name__ == '__main__':
    short_report_text, document = gc_algorithm()
    save_new_report_file(directory, document, gc_or_lc = 'GC')
    print(short_report_text)