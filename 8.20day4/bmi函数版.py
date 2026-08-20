def calc_bmi(height,weight):
    bmi=float(weight/height**2)
    return round(bmi,2)
def bmi_level(bmi):
    if bmi<18.5:
        return"偏瘦"
    elif bmi >=18.5 and bmi <24:
        return"正常"
    elif bmi >= 24 and bmi <28:
        return "超重"
    else :
        return "肥胖"
bmi=calc_bmi(1.75,70)
print(bmi_level(bmi))