#!/usr/bin/python

import time
import os
import random

# print(random.choice(foo))

function_list = [ "org.apache.pulsar.functions.api.examples.LoggingFunction" ]

command_states = [ "create" , "scaleup", "scaledown", "delete" ]


starttime=time.time()
while True:
  command = random.choice(command_states)


  print "sleep for 2 mins"
  time.sleep(120.0 - ((time.time() - starttime) % 120.0))




# /streamlio/pulsar/bin/pulsar-admi

# ./bin/pulsar-admin --admin-url $ADMIN_URL functions create --name log --jar examples/api-examples.jar --classname org.apache.pulsar.functions.api.examples.LoggingFunction --inputs log-in --output log-out --ram 128000000 &&

        # ./bin/pulsar-admin --admin-url $ADMIN_URL functions create --name log --jar examples/api-examples.jar --classname org.apache.pulsar.functions.api.examples.LoggingFunction --inputs log-in --output log-out --ram 128000000 &&
        # while true; 
        # do sleep 30; 
        # i=$((RANDOM % 10 + 1));
        # echo "scaling function to $i instances";
        # ./bin/pulsar-admin --admin-url $ADMIN_URL functions update --name log --jar examples/api-examples.jar --classname org.apache.pulsar.functions.api.examples.LoggingFunction --inputs log-in --output log-out --ram 128000000 --parallelism $i;
        # done
