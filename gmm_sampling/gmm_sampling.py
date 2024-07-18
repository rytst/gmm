import numpy as np
import matplotlib.pyplot as plt


# === trained parameters =======
mus = np.array([[2.0, 54.50],
                [4.3, 80.0]])


covs = np.array([[[0.07, 0.44],
                  [0.44, 33.7]],

                 [[0.17, 0.94],
                  [0.94, 36.00]]])


phis = np.array([0.35, 0.65])
# ==============================


def sample():
    z = np.random.choice(2, p=phis) # determine the distribution
    mu, cov = mus[z], covs[z]
    x = np.random.multivariate_normal(mu, cov)
    return x



N = 500

gen_data = np.zeros((N, 2))



for i in range(N):
    gen_data[i] = sample()



plt.scatter(gen_data[:, 0], gen_data[:, 1], alpha=0.7)
plt.xlabel('x')
plt.ylabel('y')
plt.title('N = 500')
plt.savefig('gmm_sampling.png')
