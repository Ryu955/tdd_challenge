import sys
import re


# 方針：適切な@で区切れば必要な正規表現が単純になる
def check_address(inp=sys.__stdin__, outp=sys.__stdout__):
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
        address = inp.readline()

        if address == "": return
        
        address = address.split("\n")[0]

        ats = address.count("@")
    
        # @が一つもないときは問答無用で ng
        if ats == 0:
            dot_atom_res = quated_string_res = domain_res = None
        
        # @がただ1つあるときは，ローカル部がドットアトムでもクォーテッドストリングでもありえる．さらにドメイン部を判定
        elif ats == 1:
            local, domain = address.split("@")
            dot_atom_res = re.match(dot_atom_pattern, local)
            quated_string_res = re.match(quated_string_pattern, local)
            domain_res = re.match(domain_pattern, domain)
        
        # @が2つ以上あるときは，ローカル部はクォーテッドストリングになることでしか ok を出せない．さらにドメイン部を判定
        else:
            
            # @が2つ以上あるとき，正しいクォーテッドストリングは "@ を少なくとも1つ含む．
            dot_atom_res = None
            divide_candidates = [m for m in re.finditer(r'\"@', address)]

            # 含まなければ問答無用で ng にする．
            if len(divide_candidates) == 0:
                quated_string_res = domain_res = None
            
            # 含んでいれば最後の "@ の @ で分割し，それぞれ判定する．
            else: 
                divide_point = divide_candidates[-1].span()[0]+1
                local, domain = address[0:divide_point], address[divide_point+1:len(address)+1]
                quated_string_res = re.match(quated_string_pattern, local)
                domain_res = re.match(domain_pattern, domain)

        # 最終的に，ドットアトム部かクォーテッドストリングが正しく，かつドメイン部が正しいものが ok となる．
        outp.write(("ok" if (dot_atom_res or quated_string_res) and domain_res else "ng") + "\n")


if __name__ == "__main__":
    check_address()
