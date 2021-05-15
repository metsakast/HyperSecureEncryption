import tkinter


#Encoding

rows = ['qwertzuiopü', 'asdfghjklöä', 'yxcvbnm']

def shiftKeyboard(letter,shift):
    isUpper = letter.isupper()
    for l in rows:
        index = l.find(letter.lower())
        if(index == -1): continue
        decryptedIndex = (index+shift)%len(l)
        if(isUpper):
            return l[decryptedIndex].upper()
        return l[decryptedIndex]
    return letter

def encodeString(string):
    encoded = ""
    for i in range(0,len(string)):
        encoded += shiftKeyboard(string[i],1)
    return encoded

def decodeString(string):
    decoded = ""
    for i in range(0,len(string)):
        decoded += shiftKeyboard(string[i],-1)
    return decoded

def decodeChanged(text):
    sve.set(decodeString(svd.get()))

def encodeChanged(text):
    svd.set(encodeString(sve.get()))

#Window

window = tkinter.Tk()
window.title("HyperSecureEncryption")
window.geometry("570x255")
window.configure(bg='gray11')


tkinter.Label(window, text = "Encode", font='15').place(x=5, y=52)
sve = tkinter.StringVar()
sve.trace("w", lambda name, index, mode, sve=sve: encodeChanged(sve))
encodeBox = tkinter.Entry(window, textvariable=sve, font='15')
encodeBox.place(x = 70,
        y = 50,
        width=450,
        height=30)

tkinter.Label(window, text = "Decode", font='15').place(x=5, y=152)
svd = tkinter.StringVar()
svd.trace("w", lambda name, index, mode, svd=svd: decodeChanged(svd))
decodeBox = tkinter.Entry(window, textvariable=svd, font='15')
decodeBox.place(x = 70,
        y = 150,
        width=450,
        height=30)

window.mainloop()
