# encryption technique that consists of add 13 to letters and change current letter for the correspondent letter
def decrypt_ROT13(encrypted_flag):
    flag = ""
    for letter in encrypted_flag:
        ascii_nr = ord(letter)
        if ascii_nr >= 65 and ascii_nr <= 90:
            flag += chr(((ascii_nr-65) + 13) % 26 +65)
        elif ascii_nr >= 97 and ascii_nr <= 122:
            flag += chr(((ascii_nr-97) + 13) % 26 +97)
        else:
            flag += letter
    return flag

flag = decrypt_ROT13(encrypted_flag = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}")
print(flag)
