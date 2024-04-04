import numpy as np


class Ornstein_Uhlenbeck:
    def __init__(self, St1, St2):
        self.St1 = St1  # first pair
        self.St2 = St2  # second pair
        self.dt = 1 / 252
        self.n = self.St1.shape[0] - 1
        self.lb = np.zeros_like(0)
        self.ub = 1
        self.trial = 1000  # number of k to be tested
        self.alpha = 1 / self.St1[0]
        self.k, self.X, self.mu, self.theta, self.sigma2 = self.get_best_parameters()
        self.beta = self.k / self.St2[0]

    def get_best_parameters(self):
        k_list = np.linspace(self.lb, self.ub, self.trial)
        best_l = - np.inf
        best_k, best_X, best_mu, best_theta, best_sigma2 = [None] * 5
        for k in k_list:
            beta = k / self.St2[0]
            X = self.alpha * self.St1 - beta * self.St2
            Xa = X[: -1]
            Xb = X[1:]
            Sa = np.sum(Xa)
            Sb = np.sum(Xb)
            Saa = np.sum(Xa * Xa)
            Sbb = np.sum(Xb * Xb)
            Sab = np.sum(Xa * Xb)
            mu = (Sb * Saa - Sa * Sab) / (self.n * (Saa - Sab) + Sa * (Sb - Sa))
            theta = - np.log(
                (Sab - mu * (Sa + Sb) + self.n * mu * mu) / (Saa - 2 * mu * Sa + self.n * mu * mu)) / self.dt
            gamma = np.exp(- theta * self.dt)
            sigma2 = 2 * theta * (
                        Sbb - 2 * gamma * Sab + gamma ** 2 * Saa - 2 * mu * (1 - gamma) * (Sb - gamma * Sa) + self.n * (
                            mu * (1 - gamma)) ** 2) / (self.n * (1 - gamma ** 2))
            if theta <= 0:
                continue
            l = - 0.5 * self.n * np.log(sigma2 / (2 * theta)) - 0.5 * self.n * np.log(1 - gamma ** 2) - theta * (
                        Sbb - 2 * mu * Sb + self.n * mu ** 2 - 2 * gamma * Sab + 2 * gamma * mu * (
                            Sa + Sb - self.n * mu) + gamma ** 2 * (Saa - 2 * mu * Sa + self.n * mu ** 2)) / (
                            sigma2 * (1 - gamma ** 2))
            if l > best_l:
                best_l = l
                best_k, best_X, best_mu, best_theta, best_sigma2 = k, X, mu, theta, sigma2
        return best_k, best_X, best_mu, best_theta, best_sigma2