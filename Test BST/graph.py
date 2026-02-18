import pandas as pd
import matplotlib.pyplot as plt

# generazione grafico
def graph_time_comparison(title, cols, name):
    df = pd.read_csv("exp_results.csv")
    plt.figure(figsize = (10, 6))

    # acquisizione dati numerici
    df[cols[0]] = pd.to_numeric(df[cols[0]])
    df[cols[1]] = pd.to_numeric(df[cols[1]])
    df[cols[2]] = pd.to_numeric(df[cols[2]])

    # definizione legenda
    plt.plot(df["Items_insert"], df[cols[0]], label = "BST")
    plt.plot(df["Items_insert"], df[cols[1]], label = "AVL")
    plt.plot(df["Items_insert"], df[cols[2]], label = "RBT")

    plt.title(title)
    plt.xlabel("Elementi(N)")
    plt.ylabel("Tempo(s)")
    plt.legend()
    plt.grid(True)
    plt.savefig(name)

def graph_height_comparison(title, cols, name):
    df = pd.read_csv("exp_results.csv")
    plt.figure(figsize = (10, 6))

    # acquisizione dati numerici
    df[cols[0]] = pd.to_numeric(df[cols[0]])
    df[cols[1]] = pd.to_numeric(df[cols[1]])
    df[cols[2]] = pd.to_numeric(df[cols[2]])

    # definizione legenda
    plt.plot(df["Items_insert"], df[cols[0]], label = "BST")
    plt.plot(df["Items_insert"], df[cols[1]], label = "AVL")
    plt.plot(df["Items_insert"], df[cols[2]], label = "RBT")

    plt.title(title)
    plt.xlabel("Elementi(N)")
    plt.ylabel("Altezza(h)")
    plt.legend()
    plt.grid(True)
    plt.savefig(name)

# Esempio per confrontare i casi sequenziali
graph_time_comparison("Inserimento - Caso Sequenziale", ["Insert_BST_Seq", "Insert_AVL_Seq", "Insert_RBT_Seq"], "insert_seq_graph.png")
graph_time_comparison("Inserimento - Caso Randomizzato", ["Insert_BST_Rand", "Insert_AVL_Rand", "Insert_RBT_Rand"], "insert_rand_graph.png")
graph_height_comparison("Altezza - Caso sequenziale", ["Height_BST_Seq", "Height_AVL_Seq", "Height_RBT_Seq"], "height_seq_graph.png")
graph_height_comparison("Altezza - Caso Randomizzato", ["Height_BST_Rand", "Height_AVL_Rand", "Height_RBT_Rand"], "height_rand_graph.png")

graph_time_comparison("Ricerca - Caso Sequenziale", ["Search_BST_Seq", "Search_AVL_Seq", "Search_RBT_Seq"], "search_seq_graph.png")
graph_time_comparison("Ricerca - Caso Randomizzato", ["Search_BST_Rand", "Search_AVL_Rand", "Search_RBT_Rand"], "search_rand_graph.png")

print("Grafici creati con successo")