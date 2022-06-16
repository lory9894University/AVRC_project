import json
import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import EoN


def parseDataset(path):
    df = pd.read_table(path, delimiter='\t', names=['source', 'target'])
    return nx.from_pandas_edgelist(df, "source", "target")


def parseJson(path):
    with open(path) as f:
        data = json.load(f)
        return nx.node_link_graph(data)


if __name__ == '__main__':
    dataset_path = "reducer/all_datas.json"
    # G = parseDataset("dataset.txt")
    G = parseJson(dataset_path)

    tmax = 20
    iterations = 5  # run x simulations
    tau = 0.7  # transmission rate
    gamma = 1.0  # recovery rate
    rho = 0.001  # random fraction initially infected

    for counter in range(iterations):  # run simulations
        t, S, I, R = EoN.fast_SIR(G, tau, gamma, rho=rho, tmax=tmax)
        if counter == 0:
            plt.plot(t, I, color='k', alpha=0.3, label='Simulation')
        plt.plot(t, I, color='k', alpha=0.3)

    # Now compare with ODE predictions.  Read in the degree distribution of G
    # and use rho to initialize the various model equations.
    # There are versions of these functions that allow you to specify the
    # initial conditions rather than starting from a graph.

    plt.xlabel('$t$')
    plt.ylabel('Number infected')

    plt.legend()
    plt.show()
    #plt.savefig('SIR_BA_model_vs_sim.png')