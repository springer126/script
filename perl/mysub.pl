#! /usr/bin/perl
use strict;
use warnings;

sub hyphenate {
	my $word = shift @_;
	$word = join "-",map{substr $word,$_,1}(0 .. (length $word) -1);
	return $word;
}


sub left_pad
{
	my $oldStr = shift @_;
	my $width = shift @_;
	my $padchar = shift @_;
	if((length $oldStr)>=$width)
	{
		print "Invalid Width Argument!\n";
		return $oldStr;
	}
	if((length $padchar)!=1)
	{	
		print "Invalid Padchar Argument!\n";
		return $oldStr;
	}

	my $newStr = ($padchar x ($width - (length $oldStr))).$oldStr;
	return $newStr;
}

my $world = hyphenate("helloworld");
my $leftpad = left_pad("hello,word",20,"+");
print $world."\n";
print $leftpad,"\n";
