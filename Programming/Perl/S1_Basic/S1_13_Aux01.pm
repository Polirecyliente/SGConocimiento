package Section1_13Aux;

use Carp;

sub moduleError
{
    warn("Error in module");
}
sub scriptCarp
{
    carp("Carp (warn) in script");
}
sub scriptConfess
{
    confess("Confess (die + stack) in script");
}
sub scriptCroak
{
    croak("Croak (die) in script");
}
1;