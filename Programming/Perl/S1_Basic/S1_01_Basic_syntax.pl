#!/usr/bin/perl
#   Basic syntax

#T# variable declaration and initialization, identifiers
$var1 = 5;

#T# function call, print to the terminal
print "Hello, world. Var: $var1\n";

#T# Double quotes interpolate its content, single quotes do not
print 'Var: $var1\n';

#T# plain old documentation (pod)
=begin comment
    This multi line comment begins with =begin and ends with =end.
    The pod section ends with =cut
=end comment
=head1 First header
    Text here is under the header 1. Headers can be made up to =head4
=over 4
=item item in list, ends with =back
=item second item
=item third item
=back
=cut

#T# here documents
$text1 = <<"EOF";
    FirstLine
    SecondLine Word3
    Line with var, $var1
EOF
print("\nWholeText:\n$text1");