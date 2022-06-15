#!/bin/bash

#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root/W_MAP && sudo python3 langc.py

else

echo 'you must be root ! '
echo 'use sudo'

fi
