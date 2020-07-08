#!/usr/bin/perl
#   Inheritance

package Section2_2b;

use Section2_2;

#T# inherit from class with our @ISA
our @ISA = qw(Section2_2);

#T# override subroutines, like the constructor
sub new
{
    my ($class) = @_;

#T# invoke new() from parent with SUPER::
    my $self = $class->SUPER::new($_[1],$_[2]);

#T# add other attributes
    my $self->{_attr3} = $_[3];

    bless($self,$class);
    return $self;
}

#T# add other methods
sub getAttr3
{
    my ($self) = @_;
    return $self->{_attr3};
}

#T# AUTOLOAD() is called if no subroutine is found
sub AUTOLOAD
{
    print "Can't find subroutine $AUTOLOAD in object $_[0]\n";
}

#T# garbage collector DESTROY()
sub DESTROY
{
    print "$_[0] is destroyed here\n";
    
#T# undef() frees memory from variables
    undef(@_);
}
1;