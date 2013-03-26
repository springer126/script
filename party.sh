#! /bin/bash
# This party program-- Invatied friends from guestfile.

guest_file=/home/wh/shell/guest

if [ ! -f "$guest_file" ]
then
	echo "'$guest_file' no-existent"
	exit 1
fi

PLACE=huangshan;export PLACE
(( Time=$(date +%H)+1 ))

#food list
declare -a food=(cheese crackers shrimp drinks '"hot dogs"' sandwiches)
declare -i n=0

for person in $(cat $guest_file)
do
	if [[ $person == root ]]
	then	
		continue
	else
		echo "$person  brings ${food[$n]}"
		mail -s "Party" $person <<- FINIS
		Hi ${person}!PLease join me at $PLACE for a party!
		Meet me at $Time o'clock.
		You will bring ${food[$n]} food and anything you would like to eat!
			Hope to see you soon!
			Your pal,
			wh@$(hostname)
		FINIS
		n=n+1
		if [[ ${#food[*]} == $n  ]]
		then
			declare -a food=(cheese crackers shrimp drinks "hot dogs" sandwiches)
			n=0
		fi
	fi
done

echo "Bye"

