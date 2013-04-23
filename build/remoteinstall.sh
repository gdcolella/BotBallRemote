#!/bin/bash

ssh root@$1 "rm -rf /kovan/network/*;"
scp ../upload/* root@$1:/kovan/network/
ssh root@$1 "cd /kovan/network; make"
