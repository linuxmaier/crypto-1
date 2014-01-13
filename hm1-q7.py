dusk_hex = "61747461636b206174206475736b"
dawn_hex = "61747461636b206174206461776e"
cipher_hex = "6c73d5240a948c86981bc294814d"

def hex_to_bin(hex):
    hex_val = hex
    hex_len = len(hex) * 4
    bin_val = bin(int(hex_val, 16))[2:].zfill(hex_len)
    return bin_val

def bin_to_hex(bin):
    bin_len = int(len(bin) / 4)
    
    return hex(int(bin, 2))[2:].zfill(bin_len)


def xor_bin(bin1, bin2):
    xor_result = ''

    if len(bin1) != len(bin2):
        print("The values are not the same length.")
        return null

    i = 0
    while i < len(bin1):
        if bin1[i] == bin2[i]:
            xor_result += '0'
        else:
            xor_result += '1'
        i += 1
    return xor_result

def xor_hex(hex1, hex2):
    bin1 = hex_to_bin(hex1)
    bin2 = hex_to_bin(hex2)

    bin_result = xor_bin(bin1, bin2)
    if bin_result = null:
        return null
    return bin_to_hex(bin_result)

key = xor_hex(dawn_hex, cipher_hex)

print(xor_hex(dusk_hex, key))
