a = '\u25A0'
b = '  '
bb = ' '
ps = '\n'

# numeral "0"
num_0 = [
    (b + bb + a*4 + bb), (b + a + b + b + a), (b + a + b + b + a), (b + a + b + b + a), \
        (b + a + b + b + a), (b + bb + a*4 + bb)
]
zero_1st_str = (num_0[0])
zero_2nd_str = (num_0[1])
zero_3rd_str = (num_0[2])
zero_4th_str = (num_0[3])
zero_5th_str = (num_0[4])
zero_6th_str = (num_0[5])
zero = zero_1st_str + ps + zero_2nd_str + ps + zero_3rd_str + ps +\
     zero_4th_str + ps + zero_5th_str + ps + zero_6th_str + ps

# numeral "1"
num_1 = [
    (b + bb + b + b + a), (b + bb + b + a + bb + a), (b + bb + a + b  + bb + a), \
        (b + bb + b + b + a), (b + bb + b + b + a), (b + bb + b + b + a)
]
one_1st_str = (num_1[0])
one_2nd_str = (num_1[1])
one_3rd_str = (num_1[2])
one_4th_str = (num_1[3])
one_5th_str = (num_1[4])
one_6th_str = (num_1[5])
one = one_1st_str + ps + one_2nd_str + ps + one_3rd_str + ps + \
    one_4th_str + ps + one_5th_str + ps + one_6th_str + ps

# numeral "2"
num_2 = [
    (b + bb+ a*5), (b + b + b + bb + a), (b + b + b + bb + a), (b + a*6), (b + a + a + b + b + bb), ((b + a*6))
]
two_1st_str = (num_2[0])
two_2nd_str = (num_2[1])
two_3rd_str = (num_2[2])
two_4th_str = (num_2[3])
two_5th_str = (num_2[4])
two_6th_str = (num_2[5])
two = two_1st_str + ps + two_2nd_str + ps + two_3rd_str + ps + two_4th_str + ps + two_5th_str + ps + two_6th_str

# numeral "3"
num_3 = [(b + a*6), (b + b + b + a + a), (b + b + b + a + a), (b + bb + a*5), (b + b + b  + a + a), (b + a*6)]
three_1st_str = (num_3[0])
three_2nd_str = (num_3[1])
three_3rd_str = (num_3[2])
three_4th_str = (num_3[3])
three_5th_str = (num_3[4])
three_6th_str = (num_3[5])
three = three_1st_str + ps + three_2nd_str + ps + three_3rd_str + ps +\
     three_4th_str + ps + three_5th_str + ps + three_6th_str

# numeral "4"
num_4 = [(b + a + b + b + a), (b + a + b + b + a),(b + a + b + b + a), (b + a*6), (b + b + b + bb + a), (b + b + b + bb + a)]
four_1st_str = (num_4[0])
four_2nd_str = (num_4[1])
four_3rd_str = (num_4[2])
four_4th_str = (num_4[3])
four_5th_str = (num_4[4])
four_6th_str = (num_4[5])
four = four_1st_str + ps + four_2nd_str + ps + four_3rd_str\
     + ps + four_4th_str + ps + four_5th_str + ps + four_6th_str

# numeral "5"
num_5 = [
    (b + a*6), (b + a + bb + b + b), (b + a + bb + b + b), (b + a*6), (b + b + b + a + a), (b + a*6)
]
five_1st_str = (num_5[0])
five_2nd_str = (num_5[1])
five_3rd_str = (num_5[2])
five_4th_str = (num_5[3])
five_5th_str = (num_5[4])
five_6th_str = (num_5[5])
five = five_1st_str + ps + five_2nd_str + ps + five_3rd_str\
     + ps + five_4th_str + ps + five_5th_str + ps + five_6th_str

# numeral "6"
num_6 = [
    (b + a*6), (b + a + bb + b + b), (b + a*5 + bb), (b + a + b + b + a), (b + a + b + b + a), (b + a*5 + bb)
]
six_1st_str = (num_6[0])
six_2nd_str = (num_6[1])
six_3rd_str = (num_6[2])
six_4th_str = (num_6[3])
six_5th_str = (num_6[4])
six_6th_str = (num_6[5])
six = six_1st_str + ps + six_2nd_str + ps + six_3rd_str + ps + \
    six_4th_str + ps + six_5th_str + ps + six_6th_str

# numeral "7"
num_7 = [
    (b + a*6), (b + b + b + bb + a), (b + b + b + bb + a), (b + b + bb + a*3), (b + b + b + bb + a), (b + b + b + bb + a)
]
seven_1st_str = (num_7[0])
seven_2nd_str = (num_7[1])
seven_3rd_str = (num_7[2])
seven_4th_str = (num_7[3])
seven_5th_str = (num_7[4])
seven_6th_str = (num_7[5])
seven = seven_1st_str + ps + seven_2nd_str + ps + seven_3rd_str + ps +\
    seven_4th_str + ps + seven_5th_str + ps + seven_6th_str

# numeral "8"
num_8 = [
    (b + a*6), (b + a + a + b + a + a), \
        (b + bb + a*4 + bb),  (b + a + a + b + a + a), (b + a + a + b + a + a), (b + a*6)
]
eight_1st_str = (num_8[0])
eight_2nd_str = (num_8[1])
eight_3rd_str = (num_8[2])
eight_4th_str = (num_8[3])
eight_5th_str = (num_8[4])
eight_6th_str = (num_8[5])
eight = eight_1st_str + ps + eight_2nd_str + ps + eight_3rd_str + ps + \
    eight_4th_str + ps + eight_5th_str + ps +eight_6th_str

# numeral "9"
num_9 = [
    (b + bb + a*4 + bb), (b + a + b + b + a), (b + a + b + b + a), (b + bb + a*4 + bb), (b + b + b + bb + a), (b + bb + a*4 + bb)
]
nine_1st_str = (num_9[0])
nine_2nd_str = (num_9[1])
nine_3rd_str = (num_9[2])
nine_4th_str = (num_9[3])
nine_5th_str = (num_9[4])
nine_6th_str = (num_9[5])
nine = nine_1st_str + ps + nine_2nd_str + ps + nine_3rd_str + ps + \
    nine_4th_str + ps + nine_5th_str + ps + nine_6th_str
print(nine)