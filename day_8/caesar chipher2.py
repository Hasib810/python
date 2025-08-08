alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("type 'encode' to encrypt, or 'decode' to decrypt:\n").lower() 
text = input("type your messege:\n").lower()
shift = int(input("type your shift number:\n"))




def caesar(orginal_text, shift_amount, enco_or_deco):
    output_text = ""

    for letter in orginal_text:

        if enco_or_deco == 'decode':
            shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"here is the decoded result: {output_text}")

caesar(orginal_text = text, shift_amount = shift, enco_or_deco = direction)

    