from  LocalCorrosionMethod.LocalCorrosionMethod import LocalCorrosionClass
from Document.DocumentProccess import adjust_document, save_new_report_file

def lc_algorithm(lc_input):
    lc = LocalCorrosionClass()

    document = adjust_document()

    passing_text_line = 'Fitness for Service Level 1 criteria passed'
    failing_text_line = "Fitness for Service Level 1 criteria failed"
    short_report_list = list()

    # # input data
    # t = 5.49
    # pipe_type = 'seamless %'
    # M_ut = 12.5
    # LOSS = 0
    # FCA = 0
    # FCA_ml = 0
    # t_mm = 3.16
    # s = 50
    # S = 138
    # D_0 = 88.9
    # L_msd = 1000
    # g_r = 0
    # E = 1
    # MA = 0
    # Y_B31 = 0.4
    # t_sl = 0
    # RSF_a = 0.9
    # c = 50
    # EL = 1
    # EC = 1
    # P = 16.5
    # defect_type = 'Local metal loss'

    # input data
    asset = lc_input.asset
    line_number = lc_input.line_number
    monitoring_location = lc_input.monitoring_location
    material = lc_input.material
    steel_type = lc_input.steel_type
    temperature = lc_input.temperature
    S = lc_input.stress
    nominal_pipe_size = lc_input.nominal_pipe_size
    D_0 = lc_input.outside_diameter
    schedule = lc_input.schedule
    t = lc_input.thickness
    pipe_type = lc_input.pipe_type
    M_ut = lc_input.mill_under_tolerance
    P = lc_input.P
    Y_B31 = lc_input.Y_B31
    E = lc_input.E
    EC = lc_input.EC
    EL = lc_input.EL
    RSF_a = lc_input.RSF_a
    MA = lc_input.MA
    t_sl = lc_input.t_sl
    LOSS = lc_input.LOSS
    FCA = lc_input.FCA
    FCA_ml = lc_input.FCA_ml
    NDE_type = lc_input.NDE_type
    t_mm = lc_input.t_mm
    defect_type = lc_input.defect_type
    g_r = lc_input.g_r
    s = lc_input.s
    c = lc_input.c
    L_msd = lc_input.L_msd

    input_data_text = f""" Input Data:
Asset: {asset}
Line number: {line_number}
Corrosion Monitoring Location: {monitoring_location}
Material: {material}
steel_type: {steel_type}
temperature: {temperature} [°C]
S: {S} [MPa]
nominal_pipe_size: {nominal_pipe_size}
D_0: {D_0} [mm]
schedule: {schedule}
Wall thickness, t: {t} [mm]
pipe_type: {pipe_type}
M_ut: {M_ut}
Internal design pressure, P: {P} [bar]
Y_B31: {Y_B31}
E: {E}
EC: {EC}
EL: {EL}
RSF_a: {RSF_a}
MA: {MA} [mm]
t_sl: {t_sl} [mm]
LOSS: {LOSS} [mm]
FCA: {FCA} [mm]
FCA_ml: {FCA_ml} [mm]
NDE_type: {NDE_type}
t_mm: {t_mm} [mm]
defect type = {defect_type}
g_r = {g_r} [mm]
s = {s} [mm]
c = {c} [mm]
L_msd = {L_msd} [mm]
    """

    document.add_paragraph(input_data_text)

    # algorithm
    # step 1.1 ------------------------------------------------
    document.add_paragraph('STEP 1')
    # Nominal or furnished thickness of the component adjusted for mill undertolerance as applicable, [mm]
    t_nom = lc.f_t_nom(pipe_type, t, M_ut).result
    document.add_paragraph(lc.f_t_nom(pipe_type, t, M_ut).text)

    # Future corroded wall thickness away from the damage area, [mm]
    t_c = lc.f_t_c(t_nom, LOSS, FCA).result
    document.add_paragraph(lc.f_t_c(t_nom, LOSS, FCA).text)

    # step 2 --------------------------------------------------
    document.add_paragraph('STEP 2')
    # Inside diameter of the cylinder, cone (at the location of the flaw), [mm]
    D = lc.f_D(D_0, t_nom).result
    document.add_paragraph(lc.f_D(D_0, t_nom).text)

    # longitudinal flaw length parameter, [-]
    λ = lc.f_λ(s, D, t_c).result
    document.add_paragraph(lc.f_λ(s, D, t_c).text)

    # step 2 --------------------------------------------------
    document.add_paragraph('STEP 3')
    # Remaining thickness ratio, [-]
    R_t = lc.f_R_t(t_mm, FCA_ml, t_c).result
    document.add_paragraph(lc.f_R_t(t_mm, FCA_ml, t_c).text)

    if lc.check_R_t(R_t).result == 'failed':

        document.add_paragraph(lc.check_R_t(R_t).text)
        short_report_list.append(lc.check_R_t(R_t).text)

        document.add_paragraph(failing_text_line)
        short_report_list.append(failing_text_line)

    else:

        document.add_paragraph(lc.check_R_t(R_t).text)
        short_report_list.append(lc.check_R_t(R_t).text)

        if lc.check_thickness(t_mm, FCA_ml).result == 'failed':

            document.add_paragraph(lc.check_thickness(t_mm, FCA_ml).text)
            short_report_list.append(lc.check_thickness(t_mm, FCA_ml).text)

            document.add_paragraph(failing_text_line)
            short_report_list.append(failing_text_line)

        else:

            document.add_paragraph(lc.check_thickness(t_mm, FCA_ml).text)
            short_report_list.append(lc.check_thickness(t_mm, FCA_ml).text)

            if lc.check_L_msd_criteria(L_msd, D, t_c).result == 'failed':

                document.add_paragraph(lc.check_L_msd_criteria(L_msd, D, t_c).text)
                short_report_list.append(lc.check_L_msd_criteria(L_msd, D, t_c).text)

                document.add_paragraph(failing_text_line)
                short_report_list.append(failing_text_line)

            else:

                document.add_paragraph(lc.check_L_msd_criteria(L_msd, D, t_c).text)
                short_report_list.append(lc.check_L_msd_criteria(L_msd, D, t_c).text)

                # step 4 --------------------------------------------------
                document.add_paragraph('STEP 4')

                if defect_type.lower() == 'groove' and lc.check_Groove_flaw_criteria(g_r, R_t, t_c).result == 'failed':

                    document.add_paragraph(lc.check_Groove_flaw_criteria(g_r, R_t, t_c).text)
                    short_report_list.append(lc.check_Groove_flaw_criteria(g_r, R_t, t_c).text)

                    document.add_paragraph(failing_text_line)
                    short_report_list.append(failing_text_line)

                elif (defect_type.lower() == 'groove' and lc.check_Groove_flaw_criteria(g_r, R_t, t_c).result == 'passed') \
                                            or (defect_type.lower() == 'local metal loss'):
                    if defect_type.lower() == 'groove' and lc.check_Groove_flaw_criteria(g_r, R_t, t_c).result == 'passed':
                        document.add_paragraph(lc.check_Groove_flaw_criteria(g_r, R_t, t_c).text)
                        short_report_list.append(lc.check_Groove_flaw_criteria(g_r, R_t, t_c).text)

                    # Maximum allowable working pressure based on circumferential stress, [bar]
                    MAWP_C = lc.f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).result
                    document.add_paragraph(lc.f_MAWP_C(S, E, t_c, MA, D_0, Y_B31).text)

                    # Maximum allowable working pressure based on longitudinal stress, [bar]
                    MAWP_L = lc.f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).result
                    document.add_paragraph(lc.f_MAWP_L(S, E, t_c, MA, D_0, Y_B31, t_sl).text)

                    MAWP = lc.f_MAWP(MAWP_C, MAWP_L).result
                    document.add_paragraph(lc.f_MAWP(MAWP_C, MAWP_L).text)

                    # step 6 --------------------------------------------------
                    document.add_paragraph('STEP 6')

                    # Folias factor based on the longitudinal extent of the LTA for a through-wall flaw, [-]
                    M_t = lc.f_M_t(λ).result
                    document.add_paragraph(lc.f_M_t(λ).text)

                    # !!!!!-- if not acceptable then additional calculation ow MAWPr is needed ---!!!!
                    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    if lc.check_screening_criteria(λ, R_t, RSF_a, M_t).result == 'NOT acceptable':

                        document.add_paragraph(lc.check_screening_criteria(λ, R_t, RSF_a, M_t).text)
                        short_report_list.append(lc.check_screening_criteria(λ, R_t, RSF_a, M_t).text)

                        # Computed remaining strength factor based on the meridional extent of the LTA, [-]
                        RSF = lc.f_RSF(R_t, M_t).result
                        document.add_paragraph(lc.f_RSF(R_t, M_t).text)

                        # Reduced maximum allowable working pressure of the damaged component, [bar]
                        MAWPr = lc.f_MAWPr(MAWP, RSF, RSF_a).result
                        document.add_paragraph(lc.f_MAWPr(MAWP, RSF, RSF_a).text)
                        short_report_list.append(lc.f_MAWPr(MAWP, RSF, RSF_a).text)

                    else:
                        MAWPr = P
                        document.add_paragraph(f'As λ and R_t are acceptable MAWPr = P')
                        short_report_list.append(f'As λ and R_t are acceptable MAWPr = P')

                    # step 7 --------------------------------------------------
                    document.add_paragraph('STEP 7')

                    if lc.check_circumferential_extent_criteria(c, s, EL, EC).result == 'passed':

                        document.add_paragraph(lc.check_circumferential_extent_criteria(c, s, EL, EC).text)
                        short_report_list.append(lc.check_circumferential_extent_criteria(c, s, EL, EC).text)

                        document.add_paragraph(passing_text_line)
                        short_report_list.append(passing_text_line)

                    else:

                        document.add_paragraph(lc.check_circumferential_extent_criteria(c, s, EL, EC).text)
                        short_report_list.append(lc.check_circumferential_extent_criteria(c, s, EL, EC).text)

                        #  Minimum required thickness for the component based on equipment design pressure or
                        #  equipment MAWP for longitudinal stresses
                        t_minL = lc.f_t_minL(MAWPr, D_0, S, E, P, Y_B31, t_sl, MA).result
                        document.add_paragraph(lc.f_t_minL(MAWPr, D_0, S, E, P, Y_B31, t_sl, MA).text)

                        if lc.check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml).result == 'failed':

                            document.add_paragraph(lc.check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml).text)
                            short_report_list.append(lc.check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml).text)

                            MAWPr_new = lc.f_MAWPr_new(MAWPr, t_mm, FCA_ml, t_minL).result
                            document.add_paragraph(lc.f_MAWPr_new(MAWPr, t_mm, FCA_ml, t_minL).text)
                            short_report_list.append(lc.f_MAWPr_new(MAWPr, t_mm, FCA_ml, t_minL).text)

                        else:

                            document.add_paragraph(lc.check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml).text)
                            short_report_list.append(lc.check_minimum_thickness_required_criteria(t_minL, t_mm, FCA_ml).text)
                            print('all steps are passed')

    short_report_text = '\n'.join(short_report_list)

    return short_report_text, document

# Save the document
# document.save(os.path.join(directory, "test_report_LC.docx"))

if __name__ == '__main__':
    directory = r"..\reports"

    short_report_text, document = lc_algorithm()
    save_new_report_file(directory, document, gc_or_lc='lC')
    print(short_report_text)


