u_input=input("Input: ")
k=["a","e","i","o","u","A","E","I","O","U"]
f_output=""
for _ in range (len(u_input)):
    if u_input[_] not in k:
        f_output=f_output+u_input[_]
    else:
        continue
print("Output: "+f_output)
