def reverse_word(password):
    return password[::-1]

def find(passwords, passwords_len):
    for i in range(passwords_len):
        rev_password = reverse_word(passwords[i])
        
        for j in range(i, passwords_len):
            # print(f"{rev_password} and {passwords[j]}")
            if rev_password == passwords[j]:
                rev_len = len(rev_password)
                return rev_len, rev_password[int(rev_len/2)]
    
    return -1, ""
            
        
if __name__ == "__main__":
    n = input()
    passwords = list()

    for i in range(int(n)):
        password = input()    
        passwords.append(password)
    
    password_len, pass_string = find(passwords, len(passwords))
    print(f"{password_len} {pass_string}")
            