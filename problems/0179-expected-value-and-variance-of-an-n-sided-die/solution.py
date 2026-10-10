def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	e=0
	e_2=0
	for i in range(n):
		e+=(i+1)*(1/n)
	for i in range(n):
		e_2+=pow(i+1,2)*(1/n)

	var=float(e_2-pow(e,2))
	return (e,var)
	# Your code here
	pass