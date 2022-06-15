import os

XX = os.getcwd()
CLAN = str(XX)
cc =CLAN.replace('langc', '')

os.system(f'cd {cc} && cp -r langc /root')
os.system('mv langc.sh /bin/langc')

print('Done ... ')
