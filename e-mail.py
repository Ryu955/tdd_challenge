import re

# normal_regex = r'[A-Za-z0-9\._+]+@[A-Za-z]+\.[A-Za-z]'

domain_pattern = re.compile(
    r'^(?!\.)(?!.*(\.\.+).*)[A-Za-z0-9\.\!#$%&\'\*\+-/=\?\^_`\{\|\}~]+(?<!\.)$'
) 
dot_atom_pattern = re.compile(
    r'^(?!\.)(?!.*(\.\.+).*)[A-Za-z0-9\.\!#$%&\'\*\+-/=\?\^_`\{\|\}~]+(?<!\.)$'
)
quated_string_pattern = re.compile(
    r'^\"([A-Za-z0-9\!#$%&\'\*\+-/=\?\^_`\{\|\}~\(\),.:;<>@\[\]]|\\\\|\\\")*\"$'
)

while(True):
    try:
        address = input()
    except EOFError:
        break
    
    if address[0] == " ": continue

    print(address)

    # logic

    ats = address.count("@")
    if ats == 0:
        dot_atom_res = quated_string_res = domain_res = None
    elif ats == 1:
        local, domain = address.split("@")
        dot_atom_res = re.match(dot_atom_pattern, local)
        quated_string_res = re.match(quated_string_pattern, local)
        domain_res = re.match(domain_pattern, domain)
    else:
        dot_atom_res = None
        divide_candidates = [m for m in re.finditer(r'\"@', address)]
        if len(divide_candidates) == 0:
            quated_string_res = domain_res = None
        else: 
            divide_point = divide_candidates[-1].span()[0]+1
            local, domain = address[0:divide_point], address[divide_point+1:len(address)+1]
            quated_string_res = re.match(quated_string_pattern, local)
            domain_res = re.match(domain_pattern, domain)

    print("ok" if (dot_atom_res or quated_string_res) and domain_res else "ng")
    
    print()