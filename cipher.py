alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s''t','u','v','w','x','y','z']
def both(plane_text,shift_ammount,direction):
    end_text=""
    if direction=="decode":
        shift_ammount*= -1
    for letter in plane_text:
        if letter in alphabet:
            possion=alphabet.index(letter)
            end_text+=alphabet[possion+shift_ammount]
        else:
            end_text+=letter
    print(f"the {direction}d is {end_text}")
repeat= True
while(repeat):
    directions=input("type 'encode' to encrypt and 'decode'for decrypt :\n")
    text=input("enter message\n").lower()
    shift=int(input("enter shift number:\n"))
    shift=shift % 26
    both(plane_text=text,shift_ammount=shift,direction=directions)
    contin=input("if you want to continue press'yes' for stop press 'no'\n ")
    if contin== 'no':
        repeat= False
        print("good bye")



'''
def encode(soft_text,shift_ammount):
    final=""
    for letter in soft_text:
        possion=alphabet.index(letter)
        new_letter=alphabet[possion+shift]
        final+=new_letter
    print(f"encoded text is {final}")
def decode(text,shift):
    final=""
    for letter in text:
        possion=alphabet.index(letter)
        new_letter=alphabet[possion-shift]
        final+=new_letter
    print(f"decoded text is {final}")
if(direction == "encode"):
    encode(soft_text=text,shift_ammount=shift)
elif(direction=="decode"):
    decode(text,shift)
'''