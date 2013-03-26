#! /usr/bin/perl
use Sys::Syslog;
openlog("adminscript","cons,pid","user");
syslog("warning","This is just FAKE warning message,don't worry");
closelog();
