import base64

def base64_to_bytearray(encoded_base64):
    # Decode the Base64 encoded string into bytes
    decoded_bytes = base64.b64decode(encoded_base64)
    # Convert the bytes into a bytearray for further processing
    return bytearray(decoded_bytes)

def reverse_decode(encoded_data):
    key = "FlareOn2024"
    decoded_data = bytearray()
    
    for i in range(len(encoded_data)):
        # Get the correct character from "FlareOn2024"
        key_char = ord(key[i % 11])
        # Reverse the XOR by applying XOR with the same character
        original_byte = encoded_data[i] ^ key_char
        # Append to the decoded result
        decoded_data.append(original_byte)
    
    return decoded_data

# Example usage (assuming you have the encoded_data as a byte array):
encoded_data = base64_to_bytearray("cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA==")
decoded_data = reverse_decode(encoded_data)
print(decoded_data.decode('utf-8')) 