from pprint import pprint

# this function counts the frequency of letters in the cypher
'''
On this particular case it's useless to have this function here
but I kept it to remember that in long ciphers knowing the
frequency of a certain letter can be a fast way to solve the problem,
or, at least, eliminate a lot of shift candidates.  
'''
def count_frequency(encrypted_flag):
    freq = {}
    for letter in encrypted_flag:
        if letter not in freq:
            freq[letter] = 1
        else:
            freq[letter]+=1
    return freq

encrypted_flag = "gvswwmrkxlivyfmgsrhnrisegl"
char_freq = count_frequency(encrypted_flag=encrypted_flag)
pprint(char_freq)

'''
# gvswwmrkxlivyfmgsrhnrisegl
#    ||
# suspicious: guesses -> d, e, f, g, l, m, n, o, p, r, s, t, z
'''
suspect_cases = 'defglmnoprstz'
suspect_letter = 'w'

def caesar_cipher(encrypted_flag, suspect_cases, suspect_letter):
    results = []
    suspect_letter_nr = ord(suspect_letter) -97

    for guess in suspect_cases: 
        res = ""
        guess_nr = ord(guess) -97
        shift = abs((suspect_letter_nr - guess_nr)%26 -26)
        
        for letter in encrypted_flag:
            letter_nr = ord(letter) -97
            decrypted_letter = chr((letter_nr + shift) % 26 +97)

            res += decrypted_letter

        results.append((guess, shift, res))
    return results

decrypted_results = caesar_cipher(encrypted_flag, suspect_cases, suspect_letter)
pprint(decrypted_results)

# flag -> # picoCTF{crossingtherubicondjneoach} 
# the flag was encrypted with a shift 22 technique