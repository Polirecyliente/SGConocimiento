
#   Process management

#T# backticks operator or system()
$var1 = `ls -l`;
$var2 = system("echo \$HOME");

#T# fork()
$pid1 = fork();
if ($pid1 == 0)
{
    print "In child, PID $pid1\n";
}
elsif ($pid1 != 0)
{
    print "In parent, PID $pid1\n";
}

#T# waitpid() starts the execution of child at fork() line
$retV1 = waitpid($pid1,0);

if ($pid1 != 0)
{
    print "Still in parent\n";

#T# kill() child after waitpid() to avoid memory leaks
    kill('TERM',$pid1);
}
elsif ($pid1 == 0)
{
    print "Still in child\n";
}

1;