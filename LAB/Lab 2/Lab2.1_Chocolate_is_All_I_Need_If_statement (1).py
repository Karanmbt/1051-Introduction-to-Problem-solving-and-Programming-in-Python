m_or_f = str(input("Do you want to calculate the BMR for Man or Woman?"))


if m_or_f == 'Man':
# Woman's basal metabolic rate
    FW = int(input ("What is your Weight?"))
    FH = int(input ("What is your Height?"))
    FA = int(input ("What is your Age?"))
    F_BMR = 655.1 + (4.35 * FW) + (4.7 * FH) - (4.7 * FA)
    print ("The Calories needed for a woman to maintain her weight is ", F_BMR, '.', sep='')

elif m_or_f == "Woman":
# Man's basal metabolic rate
    MW=int(input ("What is your Weight?"))
    MH=int(input ("What is your Height?"))
    MA=int(input ("What is your Age?"))

M_BMR = 66 + (6.2 * MW) + (12.7 * MH) - (6.76 * MA)
print ("The Calories needed for a man to maintain his weight is ", M_BMR, ".", sep='')
