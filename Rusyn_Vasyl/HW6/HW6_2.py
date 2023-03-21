data_base = {'Login':'Login'}
input_login = ''

while input_login != data_base['Login'] :
    input_login = input('Input your Login?')
else:
    print("Welcome back! {}".format(data_base['Login']))