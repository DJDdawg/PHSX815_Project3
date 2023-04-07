# PHSX815_Project3

This project discusses parameter fitting. My initial thoughts/prompts for the experiment can be seen in **PHSX 815 Project 3.pdf**.

**Gaussian Distribution**

The Gaussian Distribution is the most important distribution in statistics, and is given by the following formula.

$P(x | \alpha, \sigma) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{\frac{-1}{2 \sigma ^2} (x - \alpha)^2} $,

where $\alpha$ is the mean of the distribution, and $\sigma$ is the standard deviation of the distribution. 

Bayes' Theorem states that the likelihood, $P(\alpha | x, \sigma) \approx \prod_{i=1}^{N} P(x_{i} | \alpha, \sigma) $.

A more useful quantity is the logarithm of the likelihood, as it allows us to turn the multiplication into addition using log properties.

$ln(P(\alpha | x, \sigma)) \approx \sum_{i=1}^{N} ln(P(x_{i} | \alpha, \sigma)) = - \frac{N}{2} ln(2 \pi) - \frac{N}{2} ln(\sigma^2) - \frac{1}{2 \sigma^2} \sum_{i=1}^{N} (x_{i} - \alpha)^2 $.

One of the most common ways to fit a parameter to a distribution is to find the value of the parameter that will maximize the likelihood of the distribution (or the log likelihood), thus giving you the "most likely value of the parameter". For a Gaussian distribution, this can be done analytically by taking partial derivatives and setting them equal to 0.

Maximizing the log likelihood w.r.t. $\alpha$ yields $\alpha = \frac{1}{N} \sum_{i=1}^{N} x_{i}$, which is the mean of the distribution (as expected). 

Maximizing the log likelihood w.r.t. $\sigma^2$ yields $\sigma^2= \frac{1}{N} \sum_{i=1}^{N} (x_{i} - \alpha)^2 $, which is the variance of the distribution (as expected).

**The Code**

The file **Gaussian.py** will output a data file with numbers that are randomly distributed from a Gaussian Distribution with a mean of $\mu$ and a standard deviation $\sigma$. 

>$ python3 Gaussian.py -Mean 1 -Sigma 1 -Nmeas 1000 -Nexp 100 -output Data.txt

Where '-Mean' is the mean of the distribution, '-Sigma' is the standard deviation of the distribution, '-Nmeas' is the number of measurements in an experiment, and '-Nexp' is the number of experiments.

A normalized histogram of the data can be plotted with **GaussianPlot.py** by running the following:

> $python3 GaussianPlot.py Data.txt

The graph, **GaussianGraph.png**, is shown below. 

![GaussianGraph.png](https://github.com/DJDdawg/PHSX815_Project3/blob/main/GaussianGraph.png)

The data is analyzed using the code **GaussianAnalysis.py**. 

>$ python3 GaussianAnalysis.py -input0 Data.txt -Mean 1.0 -Sigma 1.0
>
>Number of experiments: 100
>
>Number of measurements/experiment: 1000
>
>Likelihood is maximized at x = 1.0 for the analytical solution
>
>Scipy minimization was successful: True
>
>numerical x-value found to maximize likelihood: 1.0
>
>maximal value: 0.3989422804014327

As predicted by the analytical solution, the x-value that maximizes the gaussian distribution is when $x = \mu$, the mean. 

This also produces the graph **GaussianLikelihood.png**, seen below.

![GaussianLikelihood.png](https://github.com/DJDdawg/PHSX815_Project3/blob/main/GaussianLikelihood.png)

**not yet done**
Uncertainty in the analytical and numerical parameter.

Graphing how the uncertainty decreases as N increases. 
