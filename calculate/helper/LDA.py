__author__ = 'ict'

import random
import DAL.file


class LDA:
    def __init__(self, graph, k, alpha, beta, iteration=2000):
        self.nw = {}
        self.nd = {}
        self.nw_sum = {}
        self.nd_sum = {}
        self.z = {}
        self.link = {}
        self.k_len = k
        self.iteration = iteration
        self.alpha = alpha
        self.beta = beta
        nl = graph.nodes_link()
        for k, v in nl.items():
            self.link[k] = list(v)
        self.theta = {m: [0] * self.k_len for m in self.link}
        self.v_len = len(self.link)
        self.m_len = self.v_len
        self.phi = [{} for _ in range(self.v_len)]
        for w in self.link:
            self.nw[w] = [0] * self.k_len
            self.nd[w] = [0] * self.k_len
        self.nw_sum = [0] * self.k_len
        self.nd_sum = {}
        for m, link in self.link.items():
            n_len = len(link)
            self.z[m] = []
            for n in range(n_len):
                topic = int(random.random() * self.k_len)
                self.z[m].append(topic)
                self.nw[self.link[m][n]][topic] += 1
                self.nd[m][topic] += 1
                self.nw_sum[topic] += 1
            self.nd_sum[m] = n_len

    def gibbs_sampling(self, m, n):
        topic = self.z[m][n]
        w = self.link[m][n]
        self.nw[w][topic] -= 1
        self.nd[m][topic] -= 1
        self.nw_sum[topic] -= 1
        self.nd_sum[m] -= 1
        alpha_sum = self.alpha * self.k_len
        beta_sum = self.beta * self.v_len
        p = [0] * self.k_len
        for k in range(0, self.k_len):
            p[k] = (self.nd[m][k] + self.alpha) / (self.nd_sum[m] + alpha_sum)
            p[k] *= (self.nw[w][k] + self.beta) / (self.nw_sum[k] + beta_sum)
        for k in range(1, self.k_len):
            p[k] += p[k - 1]
        u = random.random() * p[self.k_len - 1]
        for i in range(0, self.k_len):
            if p[i] > u:
                topic = i
                break
        self.nw[w][topic] += 1
        self.nd[m][topic] += 1
        self.nw_sum[topic] += 1
        self.nd_sum[m] += 1
        return topic

    def estimate(self):
        self.compute_theta()
        self.compute_phi()
        for _ in range(self.iteration):
            for m, link in self.link.items():
                for n in range(len(link)):
                    topic = self.gibbs_sampling(m, n)
                    self.z[m][n] = topic
        self.compute_theta()
        self.compute_phi()

    def compute_theta(self):
        for m in self.link:
            for k in range(self.k_len):
                self.theta[m][k] = (self.nd[m][k] + self.alpha) / (self.nd_sum[m] + self.k_len * self.alpha)

    def compute_phi(self):
        for k in range(self.k_len):
            for w in self.link:
                self.phi[k][w] = (self.nw[w][k] + self.alpha) / (self.nw_sum[k] + self.v_len * self.beta)

    def save_theta(self, filename):
        DAL.file.save(self.theta, filename)

    def save_phi(self, filename):
        DAL.file.save(self.phi, filename)