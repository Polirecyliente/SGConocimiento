#!/usr/bin/perl
#   Download file dialog

#T# denote type of the content with text/txt
print "Content-Type:text/txt\n";

#T# denote the content's disposition as an attachment and the file's name
print "Content-Disposition:attachment;",
    "filename = \"ContentsOfDownloadFile\"\n\n";

#T# put file's contents
print "Downloaded File:\n";
open(FILEH,"</home/jul/serverPolirecyl/server/textTest.txt");
while (read(FILEH,$buffer1,100))
{
    print "$buffer1";
}

1;