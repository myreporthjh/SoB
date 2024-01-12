hangul_cho = {
    "ㄱ":0,
    "ㄲ":1,
    "ㄴ":2,
    "ㄷ":3,
    "ㄸ":4,
    "ㄹ":5,
    "ㅁ":6,
    "ㅂ":7,
    "ㅃ":8,
    "ㅅ":9,
    "ㅆ":10,
    "ㅇ":11,
    "ㅈ":12,
    "ㅉ":13,
    "ㅊ":14,
    "ㅋ":15,
    "ㅌ":16,
    "ㅍ":17,
    "ㅎ":18
}

hangul_jung = {
    "ㅏ":0,
    "ㅐ":1,
    "ㅑ":2,
    "ㅒ":3,
    "ㅓ":4,
    "ㅔ":5,
    "ㅕ":6,
    "ㅖ":7,
    "ㅗ":8,
    "ㅘ":9,
    "ㅙ":10,
    "ㅚ":11,
    "ㅛ":12,
    "ㅜ":13,
    "ㅝ":14,
    "ㅞ":15,
    "ㅟ":16,
    "ㅠ":17,
    "ㅡ":18,
    "ㅢ":19,
    "ㅣ":20
}

hangul_jong = {
    " ":0,
    "ㄱ":1,
    "ㄲ":2,
    "ㄱㅅ":3,
    "ㄴ":4,
    "ㄴㅈ":5,
    "ㄴㅎ":6,
    "ㄷ":7,
    "ㄹ":8,
    "ㄹㄱ":9,
    "ㄹㅁ":10,
    "ㄹㅂ":11,
    "ㄹㅅ":12,
    "ㄹㅌ":13,
    "ㄹㅍ":14,
    "ㄹㅎ":15,
    "ㅁ":16,
    "ㅂ":17,
    "ㅂㅅ":18,
    "ㅅ":19,
    "ㅆ":20,
    "ㅇ":21,
    "ㅈ":22,
    "ㅊ":23,
    "ㅋ":24,
    "ㅌ":25,
    "ㅍ":26,
    "ㅎ":27
}

#다음 글자 모음 확인용. 모음 + 모음약자
moum_n = [
    "110001","001110","011100","100011","101001","001101",
    "101100","100101","010101","101010","111010","001110",
    "101110","001100","111001","111001","111100","111100",
    "101100","010111","100111","011111","011110","100001",
    "110011","110111","101101","111011","111111","110110",
    "111101","101011","011101","111110" 
]

#이전 모음 확인용.모음 + 가나다라 약자
moum_b = [
    "110001","001110","011100","100011","101001","001101",
    "101100","100101","010101","101010","111010","001110",
    "101110","001100","111001","111001","111100","111100",
    "101100","010111","110101","100100","010100","100010",
    "000110","111000","000101","110100","110010","100110",
    "010110" 
]

#된소리 예외
doinsori = [
    "000100","010100","000110","000001","000101"
]

excep = [
    "000111","001100","000001","001110","101100","111001",
    "111100","100100","010100","100010","000110","000101",
    "110100","110010","100110","010110"
]

numb = [
    "100000","110000","100100","100110","100010","110100","110110","110010","010100","010110"
]

koreanBrailleMap = {
    "000000":[" "],
    "000001":["ㄲ","ㄸ","ㅃ","ㅅ","ㅆ","ㅉ"],
    "000010":["ㄹ"],
    "000011":["ㅊ"],
    "000100":["ㄱ"],
    "000101":["ㅈ","ㅈㅏ"],
    "000110":["ㅂ","ㅂㅏ"],
    "000111":["ㄱㅓㅅ,"],
    "001000":["ㅅ,"],
    "001010":["ㄷ,"],
    "001011":["ㅎ,"],
    "001100":["ㅆ,","ㅖ"],
    "001101":["ㅛ"],
    "001110":["ㅑ","ㅒ"],
    "010000":["ㄹ,"],
    "010001":["ㅁ,"],
    "010010":["ㄴ,"],
    "010011":["ㅍ,"],
    "010100":["ㄷ","ㄷㅏ"],
    "010101":"ㅡ",
    "010110":["ㅎ","ㅎㅏ"],
    "010111":["ㅢ"],
    "011000":["ㅊ,"],
    "011001":["ㅌ,"],
    "011010":["ㅋ,"],
    "011011":["ㅇ,"],
    "011100":["ㅓ"],
    "011101":["ㅡㄹ,"],
    "011110":["ㅓㄹ,"],
    "011111":["ㅓㄴ,"],
    "100000":["ㄱ,"],
    "100001":["ㅕㄴ,"],
    "100010":["ㅁ","ㅁㅏ"],
    "100011":["ㅕ"],
    "100100":["ㄴ","ㄴㅏ"],
    "100101":["ㅠ"],
    "100110":["ㅍ","ㅍㅏ"],
    "100111":["ㅓㄱ,"],
    "101000":["ㅈ,"],
    "101001":["ㅗ"],
    "101010":["ㅣ"],
    "101011":["ㅡㄴ,"],
    "101100":["ㅜ","ㅟ"],
    "101101":["ㅗㄱ,"],
    "101110":["ㅔ"],
    "101111":["ㅚ"],
    "110000":["ㅂ,"],
    "110001":["ㅏ"],
    "110010":["ㅌ","ㅌㅏ"],
    "110011":["ㅕㄹ,"],
    "110100":["ㅋ","ㅋㅏ"],
    "110101":["ㄱㅏ"],
    "110110":["ㅜㄴ,"],
    "110111":["ㅕㅇ,"],
    "111000":["ㅅㅏ"],
    "111001":["ㅘ","ㅙ"],
    "111010":["ㅐ"],
    "111011":["ㅗㄴ,"],
    "111100":["ㅝ","ㅞ"],
    "111101":["ㅜㄹ,"],
    "111110":["ㅣㄴ,"],
    "111111":["ㅗㅇ,"],
}

BrailleEx = {
    "000001":["ㅅ","ㄲ","ㄸ","ㅃ","ㅆ","ㅉ"],
    "000111":["ㄱㅓㅅ,"],
    "001100":["ㅆ,","ㅖ"],
    "100100":["ㄴ","ㄴㅏ"],
    "010100":["ㄷ","ㄷㅏ"],
    "100010":["ㅁ","ㅁㅏ"],
    "000110":["ㅂ","ㅂㅏ"],
    "000101":["ㅈ","ㅈㅏ"],
    "110100":["ㅋ","ㅋㅏ"],
    "110010":["ㅌ","ㅌㅏ"],
    "100110":["ㅍ","ㅍㅏ"],
    "010110":["ㅎ","ㅎㅏ"],
    "001110":["ㅑ","ㅒ"],
    "101100":["ㅜ","ㅟ"],
    "111001":["ㅘ","ㅙ"],
    "111100":["ㅝ","ㅞ"]
}

BrailleNumber = {
    "100000":1,
    "110000":2,
    "100100":3,
    "100110":4,
    "100010":5,
    "110100":6,
    "110110":7,
    "110010":8,
    "010100":9,
    "010110":0
}

def div_exc_index(letter):
    if letter == excep[0]:
        return 1
    elif letter == excep[1]:
        return 2
    elif letter == excep[2]:
        return 3
    elif letter == excep[3] or letter == excep[4] or letter == excep[5] or letter == excep[6]:
        return 4
    elif (letter == excep[7] or letter == excep[8] or letter == excep[9] or letter == excep[10] or letter == excep[11] or
          letter == excep[12] or letter == excep[13] or letter == excep[14] or letter == excep[15]):
        return 5

def check_moum_n(letter):
    for st in moum_n:
        if letter == st:
            return 0
    return 1

def check_moum_b(letter):
    for st in moum_b:
        if letter == st:
            return 0
    return 1

def check_doinsori(letter):
    if letter == doinsori[0]:
        return 1, 0
    elif letter == doinsori[1]:
        return 2, 0
    elif letter == doinsori[2]:
        return 3, 0
    elif letter == doinsori[3]:
        return 4, 0
    elif letter == doinsori[4]:
        return 5, 0
    else:
        return 0, 1
    
def combineletter(ch1,ch2,ch3):
    a = hangul_cho[ch1]
    b = hangul_jung[ch2]
    c = hangul_jong[ch3]
    abc = 44032 + a*21*28+b*28+c
    return chr(abc)

def checknumber(letter,flag):
    for st in numb:
        if letter == st:
            return str(BrailleNumber[letter]), flag
    return "", 1