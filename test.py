from main import convert, convert_string

input_arg = list(map(convert, "agar chatur_vedi muhaavara wakt san.saar kaise chaan.d an.gur rajaa_i rajai in.saan kya nikhil paanDey rajoguN abhivyakti imaan_daar kat_i khaa_ii nihaayti aa_ii".split(" ")))

output = ['अगर', 'चतुरवेदी', 'मुहावरा', 'वक्त', 'संसार', 'कैसे', 'चांद', 'अंगुर', 'रजाइ', 'रजै', 'इंसान', 'क्या', 'निखिल', 'पान्डेय', 'रजोगुण', 'अभिव्यक्ती', 'इमानदार', 'कतइ', 'खाई', 'निहाय्ती', 'आई']

for i, elem in enumerate(input_arg):
    if elem != output[i]:
        print(f"Case {i} Failed, {elem}, {output[i]}")


string = """kya kar rahe ho phine_as
kya tum thik ho

Twin.kle, Twin.kle, liTTale sTaar,"""

string_output = """क्या कर रहे हो फिनेअस
क्या तुम थिक हो

ट्विंक्ले, ट्विंक्ले, लिट्टले स्टार,"""

if convert_string(string) != string_output:
    print("***String Test Failed****")
    print(convert_string(string))
    print("---------------------")
    print(string_output)
