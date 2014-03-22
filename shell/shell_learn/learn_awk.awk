#! /bin/awk -f
#awk -F: '{print $1}' passwd
#awk -F: 'BEGIN {print "name\tgroup\n----------------------"} {print $1"\t"$5} END {print "-------------------------\nend of report"}' passwd


BEGIN{
print "name\tgroup\n----------------------"
FS=":"
}

{
tot+=$3;
if ($1~/[Gg].*/) {print $1"\t"$3}
}

END{
print tot"\n-------------------------\nend of report"
} 
