print("Enter a number ");
$n=<>,$s=0;
while($n!=0){
	$a=$n%10;
	$n=int($n/10);			#we must have to declare int... else it will take pointer values
	$s=$s*10+$a;
}
print("Reverse is $s\n");