foreach(@ARGV)
{
    if(!open OUT,"$_")
    {
        die "Can not open $_\n";
    }
    
    while(<OUT>)
    {
        print "$_\n";
    }
}
