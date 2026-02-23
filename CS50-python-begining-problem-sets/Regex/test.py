import re

ip="8.3.8.8."
ip2="87.85.24.16."
ip3="255.255.2.255."


if matches2 := re.search(r"^([1-9]\.+){4}",ip):
    print("1",matches2)

if matches3 := re.search(r"^([1-9][0-9]\.){4}",ip2):
    print("2",matches3)

if matches5 := re.search(r"^([1-9]\.+){4}|^([1-9][0-9]\.){4}",ip):
    print("3",matches5)

if matches4 := re.search(r"^(([1-9]\.+)|([1-9][0-9]\.)){4}",ip2):
    print("4",matches4)
    
if matches6 := re.search(r"^(([1-9]\.)|([1-9][0-9]\.)|([1-2][0-5][0-5]\.)){4}",ip3):
    print("6",matches6)

if matches := re.search(r"((^[1-9]\.+)|(^[1-9][0-9]\.+)|(^[1-2][0-5][0-5]\.+)){4}","255.255.255.255."):
    print("5",matches)



ip4="255.255.2.255"
ip4 = ip4 + "."
if matches6 := re.search(r"^(([1-9]\.)|([1-9][0-9]\.)|([1-2][0-5][0-5]\.)){4}",ip3):
    print("6",matches6)