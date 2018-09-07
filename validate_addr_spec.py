import sys
import re


def check_address(inp=sys.__stdin__, outp=sys.__stdout__):
    normal_regex = r'[A-Za-z0-9\._+]+@[A-Za-z]+\.[A-Za-z]'
    regex = r'^\.[A-Za-z0-9\.＿+!#$%&\'*+-/=?^＿`{|}~]+@[A-Za-z]+\.[A-Za-z]'
    pattern = re.compile(regex)

    while(True):
        address = inp.readline()

        if address == "": return
        address = address.split("\n")[0]

        outp.write(("ok" if re.match(pattern, address) != None else "ng") + "\n")


if __name__ == "__main__":
    check_address()







