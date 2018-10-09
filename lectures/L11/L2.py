import numpy as np

def L2(v, *args):
    """Returns the L2 norm of a vector v. A second argument, if provided, will be interpreted as a vector of weights.
    
    INPUTS
    =======
    v: list of numbers, required
       vector
    w: list of numbers, optional, fed into *args
       vector of weights
    
    RETURNS
    ========
    sqrt(s): a number representing the l2 norm of the vector v
       unless length of w is not equal to length of v
       in which case ValueError is raised

    NOTES
    =====
    PRE: 
         - v is a list of numbers
    POST:
         - v and w (optional) are not changed by this function
         - raises a ValueError exception if len(w) != len(v)
         - returns a number

    EXAMPLES
    =========
    >>> L2([1.0, 1.0, 1.0], [3.0, 4.0, 5.0])
    7.0710678118654755
    """
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)