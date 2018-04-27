import os

fct = raw_input('To modify the dns type M , to clear the dns type E , to view the dns type V\n:')
if fct == 'M':
    dns = raw_input('Type the DNS here(x.x.x.x):')
    cmd = 'networksetup -setdnsservers Wi-Fi ' + dns  # command in MacOS
    y = os.system(cmd)
    if y == 1024:  # IP address is not correct
        print('Please type a valid IP address')
        print('\nNow the DNS is:')
        x = os.system('networksetup -getdnsservers Wi-Fi')
    else:
        print('Successfully modified')
elif fct == 'E':
    cmd = 'networksetup -setdnsservers Wi-Fi empty'
    os.system(cmd)
    print('Successfully cleared')
elif fct == 'V':
    cmd = 'networksetup -getdnsservers Wi-Fi'
    os.system(cmd)
else:
    print('Please type a valid letter')
