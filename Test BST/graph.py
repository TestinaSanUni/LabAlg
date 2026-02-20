import pandas as pd
import matplotlib.pyplot as plt
import os

# generazione percorso di destinazione dei plots
script_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(script_dir, "plots")

# generazione grafico
def graph_comparison(title, cols, name, y_label):
    df = pd.read_csv("exp_results.csv")
    plt.figure(figsize = (10, 6))

    # acquisizione dati numerici
    df[cols[0]] = pd.to_numeric(df[cols[0]])
    df[cols[1]] = pd.to_numeric(df[cols[1]])
    df[cols[2]] = pd.to_numeric(df[cols[2]])

    # definizione legenda
    plt.plot(df["Items_insert(N)"], df[cols[0]], label = "BST")
    plt.plot(df["Items_insert(N)"], df[cols[1]], label = "AVL")
    plt.plot(df["Items_insert(N)"], df[cols[2]], label = "RBT")

    plt.title(title)
    plt.xlabel("Elementi(N)")
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)

    # salvataggio nella cartella e chiusura
    save_path = os.path.join(output_folder, name)
    plt.savefig(save_path)
    plt.close()

# Esempio per confrontare i casi sequenziali
# Esempio per confrontare i casi sequenziali
graph_comparison("Inserimento - Caso Sequenziale", ["Insert_BST_Seq(ms)", "Insert_AVL_Seq(ms)", "Insert_RBT_Seq(ms)"], "insert_seq_graph.png", "Tempo(ms)")
graph_comparison("Inserimento - Caso Randomizzato", ["Insert_BST_Rand(ms)", "Insert_AVL_Rand(ms)", "Insert_RBT_Rand(ms)"], "insert_rand_graph.png", "Tempo(ms)")
graph_comparison("Altezza - Caso sequenziale", ["Height_BST_Seq(N)", "Height_AVL_Seq(N)", "Height_RBT_Seq(N)"], "height_seq_graph.png", "Altezza(h)")
graph_comparison("Altezza - Caso Randomizzato", ["Height_BST_Rand(N)", "Height_AVL_Rand(N)", "Height_RBT_Rand(N)"], "height_rand_graph.png", "Altezza(h)")

graph_comparison("Ricerca - Caso Sequenziale", ["Search_BST_Seq(ms)", "Search_AVL_Seq(ms)", "Search_RBT_Seq(ms)"], "search_seq_graph.png", "Tempo(ms)")
graph_comparison("Ricerca - Caso Randomizzato", ["Search_BST_Rand(ms)", "Search_AVL_Rand(ms)", "Search_RBT_Rand(ms)"], "search_rand_graph.png", "Tempo(ms)")

print("Grafici creati con successo")