# Pair Trading Using Ornstein–Uhlenbeck Process
## Introduction
This repository provides an implementation of pair trading using the Ornstein–Uhlenbeck process. Pair trading is a popular strategy that involves trading two correlated assets to take advantage of temporary price divergences. The Ornstein–Uhlenbeck process is a mean-reverting stochastic process that can model the behavior of asset prices.

## Ornstein–Uhlenbeck Process
The Ornstein–Uhlenbeck process is described by the stochastic differential equation:

$$
dX_t = \theta(\mu - X_t)dt + \sigma dW_t
$$

where 
- $X_t$ is the process at time $t$
- $\mu$ is the mean
- $\theta$ is the rate of mean reversion
- $\sigma$ is the volatiliy
- $W_t$ is a standard Brownian motion
- $X_0=x_0$ is the initial value.

The process $X_t$ is normally distributed with

$$
\mathbb{E}[X_t] = \mu + (x_0 - \mu)e^{-\theta t}
$$

and

$$
\mathrm{Var}(X_t) = \frac{\sigma^2}{2\theta}(1 - e^{-2\theta t})
$$

## Solution to Ornstein-Uhlenbeck Stochastic Differential Equation

By applying Itô's lemma to the function $f(t, X_t) = e^{\theta t}X_t$, we can derive the expression for $X_t$:

$$
de^{\theta t}X_t = \theta\mu e^{\theta t}dt + \sigma e^{\theta t}dW_t
$$

Simplifying the equation, we obtain:

$$
X_t = \mu + (X_0 - \mu)e^{-\theta t} + \sigma\int^t_0 e^{\theta (s - t)}dW_s
$$

By applying Itô's isometry, we can calculate the variance of the integral:

$$
\mathbb{E}\left[\left(\int^t_0e^{\theta (s-t)}dW_s\right)^2\right] = \frac{1}{2\theta}(1 - e^{-2\theta t})
$$

Therefore, given the initial value $X_0=x_0$, the process $X_t$ is normally distributed with the following expected value and variance:

$$
\mathbb{E}[X_t] = \mu + (x_0 - \mu)e^{-\theta t}
$$

and

$$
\mathrm{Var}(X_t) = \frac{\sigma^2}{2\theta}(1 - e^{-2\theta t})
$$

## Maximum Likelihood Estimation
To estimate the parameters $\theta$, $\mu$, and $\sigma$ of the Ornstein–Uhlenbeck process, maximum likelihood estimation is used. Given a set of $n+1$ samples $\mathbf{x}=\{x_0,x_1,...,x_n\}$ corresponding to times $t_0, t_1, ..., t_n$, the log-likelihood function is derived as:

$$
\mathcal{L}(\Theta, \mathbf{x}) = -\frac{n}{2}\log{\frac{\sigma^2(1-e^{-2\theta \Delta t})}{2\theta}} - \frac{\theta}{\sigma^2}\sum_{i=1}^{n}\frac{(x_{t_i}-\mu-(x_{t_{i-1}}-\mu)e^{-\theta\Delta t})^2}{1-e^{-2\theta\Delta t}}
$$

where $\Delta t = t_i - t_{i-1}$ for $i=1,...,n$. By solving $\frac{\partial\mathcal{L}}{\partial\mu}=\frac{\partial\mathcal{L}}{\partial\theta}=\frac{\partial\mathcal{L}}{\partial\sigma^2}=0$, we obtain:

$$
\begin{aligned}
\mu^{\*} &= \frac{{S_{b}S_{aa} - S_{a}S_{ab}}}{{n(S_{aa} - S_{ab}) + S_{a}(S_{b} - S_{a})}} \\
\theta^{\*}&=-\frac{1}{\Delta t}\log\frac{S_{ab}-\mu^{\*}(S_a+S_b)+n(\mu^*)^2}{S_{aa}-2\mu^\*S_a+n(\mu^\*)^2} \\
(\sigma^\*)^2&=\frac{2\theta^\*}{n(1-e^{-2\theta^\*\Delta t})}(S_{bb}-2e^{-\theta^\*\Delta t}S_{ab}+e^{-2\theta^\*\Delta t}S_{aa}-2\mu^\*(1-e^{-\theta^\*\Delta t})(S_b-e^{-\mu^\*\Delta t}S_a)+n(\mu^\*)^2(1-e^{-\theta^\*\Delta t})^2)
\end{aligned}
$$

where

$$
\begin{aligned}
S_{a}&=\sum^n_{i=1}x_{i-1}\\
S_{b}&=\sum^n_{i=1}x_{i}\\
S_{aa}&=\sum^n_{i=1}x_{i-1}^2\\
S_{ab}&=\sum^n_{i=1}x_{i-1}x_{i}\\
S_{bb}&=\sum^n_{i=1}x_{i}^2
\end{aligned}
$$

## Trading Strategy
The trading strategy is based on the pair $X_t=\frac{1}{S_0^1}S_t^1-\frac{k}{S_0^2}S_t^2$, where $S_t^1$ and $S_t^2$ are the prices of two underlying assets at time $t$, $k$ controls the level of mean reversion.

The strategy involves the following steps for each trading day $t$:
1. If there is no existing position:
  - Long the pairs if $X_t$ is less than $\mathbb{E}[X_t] - z\sqrt{\mathrm{Var}(X_t)}$, where $z$ is the $z$-score.
  - Short the pairs if $X_t$ is greater than $\mathbb{E}[X_t] + z\sqrt{\mathrm{Var}(X_t)}$.
  
2. If there is a long position:
  - Implement a stop loss if $X_t$ is less than $X_s - z\sqrt{\mathrm{Var}(X_t)}$, where $X_s$ represents the spread when the position was entered.
  - Unwind the position if $X_t$ is greater than or equal to $\mathbb{E}[X_t] + z\sqrt{\mathrm{Var}(X_t)}$.

3. If there is a short position:
  - Implement a stop loss if $X_t$ is greater than $X_s + z\sqrt{\mathrm{Var}(X_t)}$.
  - Unwind the position if $X_t$ is less than or equal to $\mathbb{E}[X_t] - z\sqrt{\mathrm{Var}(X_t)}$.

For more details, please refer to the code and documentation in this repository.
