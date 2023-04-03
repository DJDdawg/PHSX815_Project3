# PHSX815_Project3

This project discusses parameter fitting. 

**Gaussian Distribution**

$P(x | \alpha, \sigma) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{\frac{-1}{2 \sigma ^2} (x - \alpha)^2} $


The likelihood $P(\alpha | x, \sigma) \approx \prod_{i=1}^{N} P(x_{i} | \alpha, \sigma) $

Taking the logarithm allows us to turn the multiplication into addition using log properties.

$ln(P(\alpha | x, \sigma)) \approx \sum_{i=1}^{N} ln(P(x_{i} | \alpha, \sigma)) = - \frac{N}{2} ln(2 \pi) - frac{N}{2} ln(\sigma^2) - frac{1}{2 \sigma^2} \sum_{i=1}^{N} (x_{i} - \alpha)^2 $
