import re

def check_password(password):
    len_password = len(password)
    if len_password < 6 :
        print('Needed more symbols than 5!')
    elif len_password > 16:
        print('Too much... need under 16!')
    elif len(re.findall('[a-m]', password)) !=0:
        if len(re.findall('[A-Z]', password)) != 0:
            if len(re.findall('[0-9]', password)) != 0:
                if len(re.findall('[£$@]', password)) != 0:
                    print('Yess...its a good password')
    else:
        print('Something wrong!')

check_password(input('Input your password'))