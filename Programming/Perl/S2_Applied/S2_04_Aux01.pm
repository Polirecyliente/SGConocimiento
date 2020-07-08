
#   More on packages

package Section2_4a;

#T# require makes the module export the symbols in @EXPORT
require Exporter;
@ISA = qw(Exporter);
@EXPORT = qw(useMe);

sub useMe
{
    print "sub called\n";
}

1;