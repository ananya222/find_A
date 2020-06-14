def find_A(sentence):
    count_A=0
    for i in range(0,len(sentence)-1):
        if(sentence[i]=="a" or sentence[i]=="A"):
            count_A=count_A+1
    return count_A

sentence="Ananya is a smarter human than Albert Einsein."
count_A=find_A(sentence)
print(count_A)
