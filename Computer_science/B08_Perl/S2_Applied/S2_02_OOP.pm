
#   OOP

#T# OOP stands for Object Oriented Programming

#T# define a class with package
package Section2_2;

#T# constructor subroutine with "new"
sub new
{
    my $class = shift;
    my $self = {_attr1=>shift,_attr2=>shift};

#T# relate reference to class with bless()
    bless($self,$class);

#T# return new object from the class
    return $self;
}

#T# getter from an attribute
sub getAttr1
{
    my ($self) = @_;
    return $self->{_attr1};
}

#T# setter from an attribute
sub setAttr1
{
    my ($self,$newAttr1) = @_;

#T# defined() boolean function to check for not null
    if (defined($newAttr1))
    {
        $self->{_attr1} = $newAttr1;
    }
    return $self->{_attr1};
}
1;