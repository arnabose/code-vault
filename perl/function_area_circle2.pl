#area of circle using perl (without using return):
sub area{
	$r=$_[0];
	$t=3.14*$r*$r;
	print "$t";
}
area(7);