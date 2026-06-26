print "Enter number of rows ";
$n=<>;
for($i=1; $i<=$n; $i++){
	for($j=1; $j<=$i; $j++){
		if($j%2==0){
			$k=$j-int($j/2);
			print "$k";
		}
		else{
			$k=$j-int(($j-1)/2);
			print "$k";
		}
	}
	print "\n";
}
