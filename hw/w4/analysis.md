# Q1: does SMO do better than the random baselines (see prints 1,2,4)?

# Q2: how many y row evaluations are required for print 3?
The number of y row evaluations needed for print 3 would be (the number of y columns) * (the number of rows in the dataset itself - 1), since that is what would be needed to go through the entire dataset, calculate the lowest d2h for each y value, and then compare them with each datapoint to determine the top value in the dataset.

# Q3: how does SMO do compared to absolute best (print 3)