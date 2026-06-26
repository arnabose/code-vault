print("enter no. of rows ");
$n=<>,$s=0;
for($i=1; $i<=$n; $i=$i+1){
	$s=$s+1;
	if($s<2){
		for($j=1; $j<=$i; $j++){
			print("$j");
		}	
	}
	$s=0;
	print("\n");
}