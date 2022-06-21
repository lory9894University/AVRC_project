import json
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import numpy as np
import EoN


def parseDataset(path):
    df = pd.read_table(path, delimiter='\t', names=['source', 'target'])
    return nx.from_pandas_edgelist(df, "source", "target")


def parseJson(path):
    with open(path) as f:
        data = json.load(f)
        return nx.node_link_graph(data)


if __name__ == '__main__':
    dataset_path = "data_files/all_datas.json"
    G = parseDataset("data_files/dataset.txt")
    # G = parseJson(dataset_path)

    best_spreader = [d[0] for d in sorted(G.degree(), key=lambda x: x[1], reverse=True)]
    # list of nodes with highest degree, best spreader
    iterations = 5  # run x simulations
    tau = 0.056  # transmission rate
    gamma = 0.045  # recovery rate
    rho = 0.01  # random fraction initially infected
    print(best_spreader)

    #for counter in range(iterations):  # run simulations
    #    t, S, I, R = EoN.fast_SIR(G, tau, gamma, rho=rho, tmax=561)
    #    plt.plot(t, I, color=np.random.rand(3,) , alpha=0.9, label=f'{counter} run')

    t, S, I, R = EoN.fast_SIR(G, tau, gamma, rho=rho, tmax=561)
    plt.plot(t, I, color='red' , alpha=0.9, label=f'infected')
    plt.plot(t, S, color='grey' , alpha=0.9, label=f'susceptible')
    plt.plot(t, R, color='green' , alpha=0.9, label=f'recovered')
    # Now compare with ODE predictions.  Read in the degree distribution of G
    # and use rho to initialize the various model equations.
    # There are versions of these functions that allow you to specify the
    # initial conditions rather than starting from a graph.

    plt.xlabel('$t$')
    plt.ylabel('Number infected')

    plt.legend()
    plt.show()
    # plt.savefig('SIR_BA_model_vs_sim.png')
