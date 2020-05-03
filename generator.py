from random import randint
import sys
strings_a = "abcdefghijklmnopqrstuvwxyz"
strings_n = "0123456789"
strings_s = "-|@.,?/!~#%^&*()[]\=*"


def pass_gen(pw_length):
    pw = []
    if pw_length > 8:
        for i in range(0, pw_length):
            v = randint(0,2)
            if(v == 0):
                x = randint(0,25)
                pw.append(strings_a[x])
                #alphabet
            elif(v == 1):
                x = randint(0,9)
                pw.append(strings_n[x])
                #numeric
            elif(v == 2):
                x = randint(0,20)
                pw.append(strings_s[x])
                #symbol
    else:
        print("Password Length Must be Greater than 8")
    return ''.join(pw)



if __name__ == "__main__":
    length_pw = sys.argv[1]
    print(pass_gen(int(length_pw)))



            