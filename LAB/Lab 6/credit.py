def is_valid_cc_no(card_no):
    card_no = ''.join(filter(str.isdigit, card_no))
    if not 13 <= len(card_no) <= 19:
        return False

    digits = [int(digit) for digit in card_no[::-1]]
    
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)
    return total % 10 == 0

def identify_card_provider(card_no):
    provider_prefixes = {'Visa': ['4'], 'MasterCard': ['51', '52', '53', '54', '55'], 'American Express': ['34', '37']}

    card_no = ''.join(filter(str.isdigit, card_no))

    for provider, prefixes in provider_prefixes.items():
        for prefix in prefixes:
            if card_no.startswith(prefix):
                return provider
    return 'Unknown'


cc = input("Enter a credit card number😈: ")


if is_valid_cc_no(cc):
    provider = identify_card_provider(cc)
    
    if provider != 'Unknown':
        print(f"Valid {provider} card")
    else:
        print("Valid card of an unknown provider")
        
else:
    print("Invalid credit card number")





