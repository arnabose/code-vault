#gcd of two number using recursion:
sub gcd{
	my $a=$_[0];
	my $b=$_[1];
	if($a==$b){
		return $a;
	}
	else{
		if($a>$b){
			return gcd($a-$b,$b);
		}
		else{
			return gcd($a,$b-$a);
		}
	}
}

print "GCD = ",gcd(5,7);