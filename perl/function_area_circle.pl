#area of circle using perl (using return):
sub area{
	$r=$_[0];		#here $r takes the value passed by function 
	$t=3.14*$r*$r;
	return ($t);
}
$p=area(7);   	
print "$p";