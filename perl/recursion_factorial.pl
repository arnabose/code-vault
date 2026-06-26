#factorial of a number using recursion
sub factorial{
	my $x=$_[0];			#my is used as static
	if($x==0 || $x==1){
		return (1);
	}
	else{
		return $x*factorial($x-1);
	}
}
$f=factorial(5);
print "Factorial is $f\n";