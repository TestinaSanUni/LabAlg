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
    plt.plot(df["Items_insert"], df[cols[0]], label = "BST")
    plt.plot(df["Items_insert"], df[cols[1]], label = "AVL")
    plt.plot(df["Items_insert"], df[cols[2]], label = "RBT")

    plt.title(title)
    plt.xlabel("Elementi(N)")
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
    plt.savefig(name)

    # salvataggio nella cartella e chiusura
    save_path = os.path.join(output_folder, name)
    plt.savefig(save_path)
    plt.close()

# Esempio per confrontare i casi sequenziali
graph_comparison("Inserimento - Caso Sequenziale", ["Insert_BST_Seq", "Insert_AVL_Seq", "Insert_RBT_Seq"], "insert_seq_graph.png", "Tempo(s)")
graph_comparison("Inserimento - Caso Randomizzato", ["Insert_BST_Rand", "Insert_AVL_Rand", "Insert_RBT_Rand"], "insert_rand_graph.png", "Tempo(s)")
graph_comparison("Altezza - Caso sequenziale", ["Height_BST_Seq", "Height_AVL_Seq", "Height_RBT_Seq"], "height_seq_graph.png", "Altezza(h)")
graph_comparison("Altezza - Caso Randomizzato", ["Height_BST_Rand", "Height_AVL_Rand", "Height_RBT_Rand"], "height_rand_graph.png", "Altezza(h)")

graph_comparison("Ricerca - Caso Sequenziale", ["Search_BST_Seq", "Search_AVL_Seq", "Search_RBT_Seq"], "search_seq_graph.png", "Tempo(s)")
graph_comparison("Ricerca - Caso Randomizzato", ["Search_BST_Rand", "Search_AVL_Rand", "Search_RBT_Rand"], "search_rand_graph.png", "Tempo(s)")

print("Grafici creati con successo")