#!/usr/bin/perl
#   CGI

#T# CGI stands for Common Gateway Interface

#T# HTTP headers Field:contentVal

#T# Location header to redirect to another URL
# print "Location:https://localhost/info.php\r\n\r\n";

#T# Expires header to signal date when the cache should be remade
print "Expires:09 Sep 2029 10:30:00 GMT\r\n";

#T# Last-modified header to signal date of last modification
print "Last-modified:27 Aug 2019 09:14:00 GMT\r\n";

#T# Content-length header to signal the size in Bytes of the content served
print "Content-length:5\r\n";

#T# Set-Cookie header to send cookies to user agent, standard values are Expires, Domain, Path, and Secure
print "Set-Cookie:user = admin1;\n";
print "Set-Cookie:passw = cookiePass1;\n";
print "Set-Cookie:Expires = \"Sun, 20-Jun-2021 13:26:00 GMT\";\n";
print "Set-Cookie:Domain = localhost;\n";
print "Set-Cookie:Path = /cgi-bin;\n";
print "Set-Cookie:Secure;\n";

#T# MIME type of the file with Content-type:cat/ext
print "Content-type:text/html\r\n\r\n";

#T# html tags and content to be rendered by the CGI file
print '<html>';
print '<body>';
print '<h2>Header 2: CGI generated file</h2>';

#T# GET request method with the env var QUERY_STRING
if ($ENV{'REQUEST_METHOD'} eq "GET")
{
    $queryStr = $ENV{'QUERY_STRING'};
    print "<p>The query string is $queryStr</p>";
    @keyvalPairs = split("&",$queryStr);
    foreach $pair (@keyvalPairs)
    {
        ($keyTmp,$valTmp) = split("=",$pair);
        print "<p>$valTmp is $keyTmp</p>";
    }
}

#T# POST request method reading from STDIN
if ($ENV{'REQUEST_METHOD'} eq "POST")
{
    read(STDIN,$strFromStdin,$ENV{'CONTENT_LENGTH'});
    print "<p>The read string from STDIN is $strFromStdin</p>";
    @keyvalPairs = split("&",$strFromStdin);
    foreach $pair (@keyvalPairs)
    {
        ($keyTmp,$valTmp) = split("=",$pair);
        print "<p>$valTmp equals $keyTmp</p>";
    }
}

#T# print cookies current values
$cookies1 = $ENV{'HTTP_COOKIE'};
print "<p>Cookies are $cookies1</p>";

#T# CGI environment variables
print "<p>The CGI environment variables are:</p>";
foreach $key (sort keys(%ENV))
{
    print "<p>$key = $ENV{$key}</p>\n";
}

print '</body>';
print '</html>';

1;