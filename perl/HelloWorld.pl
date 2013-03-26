#! /usr/bin/perl 

use warnings;
print "Hello World\n";

#print <>;
#print sort<>;

if(!open LOG,">>log.log")
{
    die "Can not open file : $!";
}

if(!open PASSWD, "/etc/passwd")
{
    die "Cannot reach passwd!";
}

while(<PASSWD>)
{
    chomp;
    print LOG "$_\n";

}
