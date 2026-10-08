import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    def powe(x,i):
        return pow(x,i)

    g=0
    g_hash=0
    for i in range(0,len(g_coeffs)):
        g+=(powe(x,i))*g_coeffs[len(g_coeffs)-(1+i)]
        if i!=0:
            g_hash+=(powe(x,(i-1)))*i*g_coeffs[len(g_coeffs)-(1+i)]
    h=0
    h_hash=0
    for i in range(0,len(h_coeffs)):
        h+=powe(x,i)*h_coeffs[len(h_coeffs)-(1+i)]
        if i!=0:
            h_hash+=powe(x,(i-1))*i*h_coeffs[len(h_coeffs)-(1+i)]

    return (h*g_hash-g*h_hash)/powe(h,2)
    
    # Your code here
    pass