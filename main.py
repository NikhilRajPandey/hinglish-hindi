#!/bin/python3
import sys

keys = ['k', 'kh', 'g', 'gh', 'ch', 'Ch', 'j', 'z', 'jh', 'T', 'Th', 'D', 'D.', 'Dh', 'Dh.', 'N', 't', 'th', 'd', 'dh', 'n', 'p', 'f', 'ph', 'b', 'm', 'bh', 'y', 'r', 'l', 'v', 'w', 'sh', 'Sh', 's', 'h', 'x', 'tr', 'gy', 'n.', 'n)']

values = ['क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'ज़', 'झ', 'ट', 'ठ', 'ड', 'ड़', 'ढ', 'ढ़', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'फ', 'ब', 'म','भ', 'य', 'र', 'ल', 'व', 'व', 'श', 'ष', 'स', 'ह', 'क्ष','त्र','ज्ञ', 'ं', 'ँ']

kv = dict(zip(keys, values)) # kv stands for key value

vowel_keys = ['a', 'aa', 'i', 'ii', 'u', 'uu', 'e', 'ai', 'o', 'au']
vowel_values = ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']

vowel_kv = dict(zip(vowel_keys, vowel_values)) # kv stands for key value

matra_keys = ['a', 'aa', 'ii', 'i', 'uu', 'u', 'e', 'ai', 'o', 'au', 'a']
matra_values = ['', 'ा', 'ी', 'ि', 'ू', 'ु', 'े', 'ै', 'ो', 'ौ', '']

matra_kv = dict(zip(matra_keys, matra_values))


def give_letter(arr, arr_dict, word):
    """
    It is used give the starting english word to hindi and the english letter length
    Exp: abhi => [अ , 1]
    Exp: gyaan => [ज्ञ, 2 ] Since gy have 2 length
    """

    for letter in arr:
        if letter == word[:len(letter)]:
            # print(arr, letter, word[:len(letter)])
            return [arr_dict[letter], len(letter)]
            
    return ['\0', 0]

def convert_util(word):
    sk = sorted(keys, key=len, reverse=True) # sorted_keys
    svk = sorted(vowel_keys, key=len, reverse=True) # sorted_vowel_keys
    smk = sorted(matra_keys, key=len, reverse=True) # sorted_matra_keys
    half_sign = '्'

    result = ""
    i = 0

    while i < len(word):
        if i == 0:
            matched_vowel = give_letter(svk, vowel_kv, word[i:])

            if matched_vowel[0] != '\0':
                i += matched_vowel[1]
                result += matched_vowel[0]
                continue
                
        matched_consonant = give_letter(sk, kv, word[i:])

        if matched_consonant[0] != '\0':
            i += matched_consonant[1]
            result += matched_consonant[0]

            if i == len(word) - 1 and word[-1] == 'a':
                result += 'ा'
                break
            
            matched_matra = give_letter(smk, matra_kv, word[i:])

            if matched_matra[0] != '\0':
                i += matched_matra[1]
                result += matched_matra[0]

            else:
                # Truness word[i-1].isalpha() is used since we don't have to apply this rule for n. and n)
                if i < len(word) and word[i-1].isalpha() : result += half_sign

        else: return result + word[i:]
                
    return result

def convert(word):
    result = ''
    for sub_word in word.split('_'): result += convert_util(sub_word)

    return result

def convert_string(string):
    result = ''

    current_phrase = ''

    for letter in string:
        if letter.isalpha() or letter in ['_', '.', ')'] : current_phrase += letter
        else:
            result += convert(current_phrase)
            result += letter
            current_phrase = ''

    return result + convert(current_phrase)

# print(list(map(convert, "agar chatur_vedii muhaavara wakt san.saar kaise chaan.d an.gur rajaa_i rajai in.saan kya nikhil paanDey rajoguN abhivyaktii imaan_daar kat_i khaa_ii nihaaytii aa_ii".split(" "))))

# print(convert("waqt"))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: hinglish [input-file]")
        print("Usage: hinglish -s STRING")
    else:
        if sys.argv[1] == '-s':
            print(convert_string(sys.argv[2]))
        else:
            filename = sys.argv[1]
                
            with open(filename) as file:
                print(convert_string(file.read()))
