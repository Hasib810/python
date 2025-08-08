alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(orginal_text, shift_amount, enco_or_deco):
    output_text = ""

    if enco_or_deco == 'decode':
                shift_amount *= -1

    for letter in orginal_text:
        if letter not in  alphabet :
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"here is the {enco_or_deco}ded result: {output_text}")

should_continue = True

while should_continue:

    direction = input("type 'encode' to encrypt, or 'decode' to decrypt:\n").lower() 
    text = input("type your messege:\n").lower()
    shift = int(input("type your shift number:\n"))

    caesar(text, shift, direction)
    restart = input("type 'yes' if you want to go or otherwise type'no'\n").lower()
    if restart == 'no':
        should_continue == False
        print("good bye")