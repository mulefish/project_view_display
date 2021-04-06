
import math

gaint_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AG', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BG', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CG', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DG', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ', 'EA', 'EB', 'EC', 'ED', 'EE', 'EF', 'EG', 'EH', 'EI', 'EG', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER', 'ES', 'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ', 'FA', 'FB', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH', 'FI', 'FG', 'FK', 'FL', 'FM', 'FN', 'FO', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FU', 'FV', 'FW', 'FX', 'FY', 'FZ', 'GA', 'GB', 'GC', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GG', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GV', 'GW', 'GX', 'GY', 'GZ', 'HA', 'HB', 'HC', 'HD', 'HE', 'HF', 'HG', 'HH', 'HI', 'HG', 'HK', 'HL', 'HM', 'HN', 'HO', 'HP', 'HQ', 'HR', 'HS', 'HT', 'HU', 'HV', 'HW', 'HX', 'HY', 'HZ', 'IA', 'IB', 'IC', 'ID', 'IE', 'IF', 'IG', 'IH', 'II', 'IG', 'IK', 'IL', 'IM', 'IN', 'IO', 'IP', 'IQ', 'IR', 'IS', 'IT', 'IU', 'IV', 'IW', 'IX', 'IY', 'IZ', 'GA', 'GB', 'GC', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GG', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GV', 'GW', 'GX', 'GY', 'GZ', 'KA', 'KB', 'KC', 'KD', 'KE', 'KF', 'KG', 'KH', 'KI', 'KG', 'KK', 'KL', 'KM', 'KN', 'KO', 'KP', 'KQ', 'KR', 'KS', 'KT', 'KU', 'KV', 'KW', 'KX', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LI', 'LG', 'LK', 'LL', 'LM', 'LN', 'LO', 'LP', 'LQ', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY', 'LZ', 'MA', 'MB', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MI', 'MG', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NB', 'NC', 'ND', 'NE', 'NF', 'NG', 'NH', 'NI', 'NG', 'NK', 'NL', 'NM', 'NN', 'NO', 'NP', 'NQ', 'NR', 'NS', 'NT', 'NU', 'NV', 'NW', 'NX', 'NY', 'NZ', 'OA', 'OB', 'OC', 'OD', 'OE', 'OF', 'OG', 'OH', 'OI', 'OG', 'OK', 'OL', 'OM', 'ON', 'OO', 'OP', 'OQ', 'OR', 'OS', 'OT', 'OU', 'OV', 'OW', 'OX', 'OY', 'OZ', 'PA', 'PB', 'PC', 'PD', 'PE', 'PF', 'PG', 'PH', 'PI', 'PG', 'PK', 'PL', 'PM', 'PN', 'PO', 'PP', 'PQ', 'PR', 'PS', 'PT', 'PU', 'PV', 'PW', 'PX', 'PY', 'PZ', 'QA', 'QB', 'QC', 'QD', 'QE', 'QF', 'QG', 'QH', 'QI', 'QG', 'QK', 'QL', 'QM', 'QN', 'QO', 'QP', 'QQ', 'QR', 'QS', 'QT', 'QU', 'QV', 'QW', 'QX', 'QY', 'QZ', 'RA', 'RB', 'RC', 'RD', 'RE', 'RF', 'RG', 'RH', 'RI', 'RG', 'RK', 'RL', 'RM', 'RN', 'RO', 'RP', 'RQ', 'RR', 'RS', 'RT', 'RU', 'RV', 'RW', 'RX', 'RY', 'RZ', 'SA', 'SB', 'SC', 'SD', 'SE', 'SF', 'SG', 'SH', 'SI', 'SG', 'SK', 'SL', 'SM', 'SN', 'SO', 'SP', 'SQ', 'SR', 'SS', 'ST', 'SU', 'SV', 'SW', 'SX', 'SY', 'SZ', 'TA', 'TB', 'TC', 'TD', 'TE', 'TF', 'TG', 'TH', 'TI', 'TG', 'TK', 'TL', 'TM', 'TN', 'TO', 'TP', 'TQ', 'TR', 'TS', 'TT', 'TU', 'TV', 'TW', 'TX', 'TY', 'TZ', 'UA', 'UB', 'UC', 'UD', 'UE', 'UF', 'UG', 'UH', 'UI', 'UG', 'UK', 'UL', 'UM', 'UN', 'UO', 'UP', 'UQ', 'UR', 'US', 'UT', 'UU', 'UV', 'UW', 'UX', 'UY', 'UZ', 'VA', 'VB', 'VC', 'VD', 'VE', 'VF', 'VG', 'VH', 'VI', 'VG', 'VK', 'VL', 'VM', 'VN', 'VO', 'VP', 'VQ', 'VR', 'VS', 'VT', 'VU', 'VV', 'VW', 'VX', 'VY', 'VZ', 'WA', 'WB', 'WC', 'WD', 'WE', 'WF', 'WG', 'WH', 'WI', 'WG', 'WK', 'WL', 'WM', 'WN', 'WO', 'WP', 'WQ', 'WR', 'WS', 'WT', 'WU', 'WV', 'WW', 'WX', 'WY', 'WZ', 'XA', 'XB', 'XC', 'XD', 'XE', 'XF', 'XG', 'XH', 'XI', 'XG', 'XK', 'XL', 'XM', 'XN', 'XO', 'XP', 'XQ', 'XR', 'XS', 'XT', 'XU', 'XV', 'XW', 'XX', 'XY', 'XZ', 'YA', 'YB', 'YC', 'YD', 'YE', 'YF', 'YG', 'YH', 'YI', 'YG', 'YK', 'YL', 'YM', 'YN', 'YO', 'YP', 'YQ', 'YR', 'YS', 'YT', 'YU', 'YV', 'YW', 'YX', 'YY', 'YZ', 'ZA', 'ZB', 'ZC', 'ZD', 'ZE', 'ZF', 'ZG', 'ZH', 'ZI', 'ZG', 'ZK', 'ZL', 'ZM', 'ZN', 'ZO', 'ZP', 'ZQ', 'ZR', 'ZS', 'ZT', 'ZU', 'ZV', 'ZW', 'ZX', 'ZY', 'ZZ', 'AAA', 'AAB', 'AAC', 'AAD', 'AAE', 'AAF', 'AAG', 'AAH', 'AAI', 'AAG', 'AAK', 'AAL', 'AAM', 'AAN', 'AAO', 'AAP', 'AAQ', 'AAR', 'AAS', 'AAT', 'AAU', 'AAV', 'AAW', 'AAX', 'AAY', 'AAZ', 'ABA', 'ABB', 'ABC', 'ABD', 'ABE', 'ABF', 'ABG', 'ABH', 'ABI', 'ABG', 'ABK', 'ABL', 'ABM', 'ABN', 'ABO', 'ABP', 'ABQ', 'ABR', 'ABS', 'ABT', 'ABU', 'ABV', 'ABW', 'ABX', 'ABY', 'ABZ', 'ACA', 'ACB', 'ACC', 'ACD', 'ACE', 'ACF', 'ACG', 'ACH', 'ACI', 'ACG', 'ACK', 'ACL', 'ACM', 'ACN', 'ACO', 'ACP', 'ACQ', 'ACR', 'ACS', 'ACT', 'ACU', 'ACV', 'ACW', 'ACX', 'ACY', 'ACZ', 'ADA', 'ADB', 'ADC', 'ADD', 'ADE', 'ADF', 'ADG', 'ADH', 'ADI', 'ADG', 'ADK', 'ADL', 'ADM', 'ADN', 'ADO', 'ADP', 'ADQ', 'ADR', 'ADS', 'ADT', 'ADU', 'ADV', 'ADW', 'ADX', 'ADY', 'ADZ', 'AEA', 'AEB', 'AEC', 'AED', 'AEE', 'AEF', 'AEG', 'AEH', 'AEI', 'AEG', 'AEK', 'AEL', 'AEM', 'AEN', 'AEO', 'AEP', 'AEQ', 'AER', 'AES', 'AET', 'AEU', 'AEV', 'AEW', 'AEX', 'AEY', 'AEZ', 'AFA', 'AFB', 'AFC', 'AFD', 'AFE', 'AFF', 'AFG', 'AFH', 'AFI', 'AFG', 'AFK', 'AFL', 'AFM', 'AFN', 'AFO', 'AFP', 'AFQ', 'AFR', 'AFS', 'AFT', 'AFU', 'AFV', 'AFW', 'AFX', 'AFY', 'AFZ', 'AGA', 'AGB', 'AGC', 'AGD', 'AGE', 'AGF', 'AGG', 'AGH', 'AGI', 'AGG', 'AGK', 'AGL', 'AGM', 'AGN', 'AGO', 'AGP', 'AGQ', 'AGR', 'AGS', 'AGT', 'AGU', 'AGV', 'AGW', 'AGX', 'AGY', 'AGZ', 'AHA', 'AHB', 'AHC', 'AHD', 'AHE', 'AHF', 'AHG', 'AHH', 'AHI', 'AHG', 'AHK', 'AHL', 'AHM', 'AHN', 'AHO', 'AHP', 'AHQ', 'AHR', 'AHS', 'AHT', 'AHU', 'AHV', 'AHW', 'AHX', 'AHY', 'AHZ', 'AIA', 'AIB', 'AIC', 'AID', 'AIE', 'AIF', 'AIG', 'AIH', 'AII', 'AIG', 'AIK', 'AIL', 'AIM', 'AIN', 'AIO', 'AIP', 'AIQ', 'AIR', 'AIS', 'AIT', 'AIU', 'AIV', 'AIW', 'AIX', 'AIY', 'AIZ', 'AGA', 'AGB', 'AGC', 'AGD', 'AGE', 'AGF', 'AGG', 'AGH', 'AGI', 'AGG', 'AGK', 'AGL', 'AGM', 'AGN', 'AGO', 'AGP', 'AGQ', 'AGR', 'AGS', 'AGT', 'AGU', 'AGV', 'AGW', 'AGX', 'AGY', 'AGZ', 'AKA', 'AKB', 'AKC', 'AKD', 'AKE', 'AKF', 'AKG', 'AKH', 'AKI', 'AKG', 'AKK', 'AKL', 'AKM', 'AKN', 'AKO', 'AKP', 'AKQ', 'AKR', 'AKS', 'AKT', 'AKU', 'AKV', 'AKW', 'AKX', 'AKY', 'AKZ', 'ALA', 'ALB', 'ALC', 'ALD', 'ALE', 'ALF', 'ALG', 'ALH', 'ALI', 'ALG', 'ALK', 'ALL']



def getLetterFromNumber(n):
    if n < len(gaint_list):
        return gaint_list[n]
    else:
        return "_" + n


if __name__ == "__main__":
    # https://www.programmersought.com/article/75954623406/

    def cycle_letter(arr, level):
        tempArr = []
        letterArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        arrNum = len(arr)
        if(level == 0 or arrNum == 0):
            return letterArr
        for index in range(arrNum):
            for letter in letterArr:
                tempArr.append(arr[index]+letter)
        return tempArr

    # arr: Number of Excel column names to be generated
    def reduce_excel_col_name(num):
        tempVal = 1
        level = 1
        while(tempVal):
            tempVal = num/(math.pow(26, level))
            if(tempVal > 1):
                level += 1
            else:
                break

        excelArr = []
        tempArr = []
        for index in range(level):
            tempArr = cycle_letter(tempArr, index)
            for numIndex in range(len(tempArr)):
                if(len(excelArr) < num):
                    excelArr.append(tempArr[numIndex])
                else:
                    return excelArr

    print(reduce_excel_col_name(1000))
