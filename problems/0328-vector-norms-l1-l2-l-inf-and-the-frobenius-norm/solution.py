import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str):
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if arr.ndim==1:
        arr_abs_list=np.abs(arr).tolist()
        arr_abs=[float(i) for i in arr_abs_list]
        arr_abs_sq=[float(pow(i,2)) for i in arr_abs_list]
        if norm_type=='l1':
            ans=sum(arr_abs)
            return ans
        if norm_type=='l2':
            ans=pow(sum(arr_abs_sq),0.5)
            return ans
        if norm_type=='linf':
            ans=max(arr_abs)
            return ans
    else:
        arr_abs_list=np.abs(arr).flatten().tolist()
        arr_abs=[float(i) for i in arr_abs_list]
        arr_abs_sq=[float(pow(i,2)) for i in arr_abs_list]
        if norm_type=='l1':
            ans=sum(arr_abs)
            return ans
        if norm_type=='l2':
            ans=pow(sum(arr_abs_sq),0.5)
            return ans
        if norm_type=='linf':
            ans=max(arr_abs)
            return ans

    if norm_type=='frobenius':
        if arr.ndim==1:
            raise ValueError
        else:
            n_arr=arr.flatten().tolist()
            n_arr=[pow(i,2) for i in n_arr]
            n_arr=float(pow(sum(n_arr),0.5))
            return n_arr
