import hanguldata

# binary 파일 불러오기
######파일 형식을 aegukga2.txt처럼 해둘 것
######줄 하나당 바이너리 코드 6글자씩
def get_bin_data():
    file_path = "word.txt"
    with open(file_path) as f:
        lines = f.read().splitlines()
        if not lines:
            pass
    return lines

def add_sts(letter,letter_n,letter_b,f):
    sts = ""
    flag = f
    if len(hanguldata.koreanBrailleMap[letter])>1:
        index, i = 0, 0
        index = hanguldata.div_exc_index(letter)
        if index == 1:
           sts = hanguldata.BrailleEx[letter][0]
           flag = 0
        if index == 2:
            i = hanguldata.check_moum_b(letter_b)
            sts = hanguldata.BrailleEx[letter][i]
        if index == 3:
            i, flag = hanguldata.check_doinsori(letter_n)
            sts = hanguldata.BrailleEx[letter][i]
        if index == 4:
            if letter_n == "111010":
                sts = hanguldata.BrailleEx[letter][1]
                flag = 0
            else:
                sts = hanguldata.BrailleEx[letter][0]
        if index == 5:
            i = hanguldata.check_moum_n(letter_n)
            sts = hanguldata.BrailleEx[letter][i]
    else:
        sts = hanguldata.koreanBrailleMap[letter][0]
    return sts, flag
    
def binary_to_sentence(binary_data):
    flag = 1
    letter_b = ""
    sentence = ""
    for i in range(len(binary_data)):
        result = binary_data[i]
        result2 = ''
        if i != len(binary_data)-1:
            result2 = binary_data[i+1]
        letter = result
        letter_n = result2
        
        #숫자 표시
        if letter == "001111":
            flag = 2
            continue
        if flag == 2: 
            if letter == "000000":
                flag = 1
                continue
            sts, flag = hanguldata.checknumber(letter,flag)
            
        if flag == 1:
            sts, flag = add_sts(letter, letter_n, letter_b, flag)
        elif flag == 0:
            flag = 1
        letter_b = letter
        sentence += sts
    return sentence

def combine(sentence):
    sentence+="    "
    result =""
    aaa = []
    i = 1
    for ch in sentence:
        i+=1
        if ch != ' ' and ch != ',':
            aaa.append(ch)
            if ch in '1234567890':
                result += ch
                aaa=[]
            if len(aaa)==1 and ch in 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ':
                aaa = ['ㅇ']+aaa
            if len(aaa)==2 and sentence[i]!=',':
                result+=hanguldata.combineletter(aaa[0],aaa[1]," ")
                aaa = []
            if len(aaa)==3 and sentence[i+1]!=',':
                result+=hanguldata.combineletter(aaa[0],aaa[1],aaa[2])
                aaa = []
            if len(aaa)==4:
                aaa[2]+=aaa[3]
                result+=hanguldata.combineletter(aaa[0],aaa[1],aaa[2])
                aaa = []
        elif ch == ' ':
            result += ' '
    return result     

#메인 함수 ****result안의 문장만 꺼내오면 됨****  @@@@@@@@@@@@@@@@@@@@@@@@@@@@              
def convert():
    temp_binary_data = get_bin_data()
    binary_data = list(filter(lambda x: x in hanguldata.koreanBrailleMap, temp_binary_data))
    sentence = binary_to_sentence(binary_data)
    print(sentence)
    result = combine(sentence)
    print(result)
    ###result.txt 파일에 저장한다
    with open('result.txt','w') as file:
        file.write(result)
