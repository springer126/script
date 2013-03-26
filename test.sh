#! /bin/bash

guest_file=/home/wh/shell/guest

for person in $(cat $guest_file)
do
    if [[ $person == root ]]
    then
	continue
    else
	echo $person
    fi
done
