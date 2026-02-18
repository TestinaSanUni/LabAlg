import pandas as pd
import matplotlib.pyplot as plt

# generazione grafico
def graph_comparison(title, path, cols, name):
    df = pd.read_csv(path)
    plt.figure(figsize = (10, 6))

    # acquisizione dati numerici
    df[cols[0]] = pd.to_numeric(df[cols[0]])
    df[cols[1]] = pd.to_numeric(df[cols[1]])
    df[cols[2]] = pd.to_numeric(df[cols[2]])

    # definizione legenda
    plt.plot(df["Items1"], df[cols[0]], label = "BST")
    plt.plot(df["Items1"], df[cols[1]], label = "AVL")
    plt.plot(df["Items1"], df[cols[2]], label = "RBT")

    plt.title(title)
    plt.xlabel("Elementi(N)")
    plt.ylabel("Tempo(s)")
    plt.legend()
    plt.grid(True)
    plt.savefig(name)

# Esempio per confrontare i casi sequenziali
graph_comparison("Inserimento - Caso Sequenziale", "exp_results.csv", ["Insert_BST_Seq", "Insert_AVL_Seq", "Insert_RBT_Seq"], "insert_seq_graph.png")
graph_comparison("Inserimento - Caso Randomizzato", "exp_results.csv", ["Insert_BST_Rand", "Insert_AVL_Rand", "Insert_RBT_Rand"], "insert_rand_graph.png")

graph_comparison("Ricerca - Caso Sequenziale", "exp_results.csv", ["Search_BST_Seq", "Search_AVL_Seq", "Search_RBT_Seq"], "search_seq_graph.png")
graph_comparison("Ricerca - Caso Randomizzato", "exp_results.csv", ["Search_BST_Rand", "Search_AVL_Rand", "Search_RBT_Rand"], "search_rand_graph.png")

print("Grafici creati con successo")