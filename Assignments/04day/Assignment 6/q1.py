# Question 1:
# Implement ROT-13 encoder/decoder using given dictionary key.

key = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v',
'j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f',
't':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m',
'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V',
'J':'W','K':'X','L':'Y','M':'Z','N':'A','O':'B','P':'C','Q':'D','R':'E',
'S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}

def rot13(text):
    result = ""
    for char in text:
        if char in key:
            result += key[char]
        else:
            result += char
    return result

message = input("Enter text to encode/decode: ")
print("Result:", rot13(message))

# Secret Message Decode
secret = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
print("Decoded Secret:", rot13(secret))
