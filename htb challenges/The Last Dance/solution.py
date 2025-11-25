# Recovering FLAG from ChaCha20 nonce-reuse vulnerability

file = open("out.txt", "r")
iv = file.readline()  # not used in this task
enc_msg_hex = file.readline()
enc_flag_hex = file.readline()

# plaintext message from the original script
message = (
    b"Our counter agencies have intercepted your messages and a lot "
    b"of your agent's identities have been exposed. In a matter of "
    b"days all of them will be captured"
)

# Convert from hex
enc_msg = bytes.fromhex(enc_msg_hex)
enc_flag = bytes.fromhex(enc_flag_hex)

# keystream = enc_msg XOR message (for the bytes where message exists)
keystream = bytes(a ^ b for a, b in zip(enc_msg, message))

# cutting keystream corresponding to the flag length
keystream_flag = keystream[:len(enc_flag)]

# FLAG = enc_flag XOR keystream_part
flag = bytes(a ^ b for a, b in zip(enc_flag, keystream_flag))

print(flag.decode())
