# Alternating caps string converter

def wUt(text):
    alt_text = ""
    switch = 0
    for char in text:
        if char != " ":
            if switch == 0:
                alt_text += char.lower()
                switch = 1
            else:
                alt_text += char.upper()
                switch = 0
        else:
            alt_text += char
    return alt_text

if __name__ == "__main__":
    user_input = str(input("wUt dId yOu jUsT sAy tO mE: "))
    print(wUt(user_input))
