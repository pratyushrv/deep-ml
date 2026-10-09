import numpy as np
import math

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    if not isinstance(data,list):
        data=data.tolist()
    if isinstance (data, list):
        mean=(1/len(data))*sum(data)

        data.sort(reverse=False)
        if len(data)%2==0:
            median=0.5*(data[int((len(data)/2)-1)]+data[int(len(data)/2)])
        else:
            median=data[int(len(data)/2)]
        
        if len(data)%4==0:
            twofive=data[int(len(data)/4)-1]
            svn_five=data[int(len(data)*3/4)-1]
        else:
            if len(data)>1:
                twofive=data[max(int(math.floor(len(data)/4))-1,1)]
                svn_five=data[int(math.ceil(len(data)*3/4))-1]
            else:
                twofive=data[0]
                svn_five=data[0]
        
        iqr=svn_five-twofive

        unique_dict={}
        for k in data:
            if k in unique_dict.keys():
                unique_dict[k]+=1
            else:
                unique_dict[k]=1
        mode=max(unique_dict,key=unique_dict.get)
        sq_loss=[pow(mean-i,2) for i in data]
        variance=sum(sq_loss)/len(data)
        sd=pow(variance,0.5)


        return {
            'mean':mean,
            'median':median,
            'mode':mode,
            'variance':variance,
            'standard_deviation':sd,
            '25th_percentile':twofive,
            '50th_percentile':median,
            '75th_percentile':svn_five,
            'interquartile_range':iqr
        }

    # Your code here
    pass