#! /bin/sh -x
#awk -F: '{print $1}' passwd
#awk -F: 'BEGIN {print "name\tgroup\n----------------------"} {print $1"\t"$5} END {print "-------------------------\nend of report"}' passwd
awk -F: 'BEGIN {print "name\tgroup\n----------------------"}
		 {if ($1~/[Gg].*/) print $1"\t"$5} 
	 	 END {print "-------------------------\nend of report"}' passwd
awk -F: 'BEGIN {print "name\tgroup\n----------------------"}
		 {if ($1~/(bin|mysql)/ && $5~/(bin|mysql)/) print $1"\t"$5} 
	 	 END {print "-------------------------\nend of report"}' passwd
		 

awk -F: '{print NF,NR,$0} END {print FILENAME}' passwd

echo $PWD | awk -F/ '{print $NF}'

awk -F: 'BEGIN {BASELINE=10} {if ($3>BASELINE) print $1,$3*10}' passwd

awk -F: '{if ($3!=$4) {$10=$3+$4; print $1,$3,$4,$10}}' passwd

ls -l | awk '/^[^d]/ {tot+=$5;print $9,$5} END{print "Total KB:"tot}'

#***********attention printf diff print************
echo "65" | awk '{printf "%c\n",$0}'
