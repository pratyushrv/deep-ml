import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	grad_arr=np.array(gradient)
	magnitude=np.linalg.norm(grad_arr,ord=2)
	if magnitude>0:
		direction=[float(i/magnitude) for i in gradient]
		descent_direction=[-1*i for i in direction]
	else:
		direction=[0 for i in gradient]
		descent_direction=[0 for i in direction]

	return {'magnitude':magnitude,'direction':direction,'descent_direction':descent_direction}
	# Your code here
	pass