print("1", flush = True)
from Tester import Tester
print("2")
import pandas as pd
print("3")
import matplotlib.pyplot as plt
print("4")
import os

# generazione foglio di calcolo
def spreadsheet(df):
    time_cols = [
        "Insert_BST_Seq(ms)", "Insert_BST_Rand(ms)",
        "Insert_AVL_Seq(ms)", "Insert_AVL_Rand(ms)",
        "Insert_RBT_Seq(ms)", "Insert_RBT_Rand(ms)",
        "Search_BST_Seq(ms)", "Search_BST_Rand(ms)",
        "Search_AVL_Seq(ms)", "Search_AVL_Rand(ms)",
        "Search_RBT_Seq(ms)", "Search_RBT_Rand(ms)"
    ]

    int_cols = [
        "Items(n)",
        "Height_BST_Seq(n)", "Height_BST_Rand(n)",
        "Height_AVL_Seq(n)", "Height_AVL_Rand(n)",
        "Height_RBT_Seq(n)", "Height_RBT_Rand(n)"
    ]

    # formattazione valori
    for col in int_cols:
        df[col] = df[col].astype(int)

    for col in time_cols:
        df[col] = df[col].map(lambda x: f"{x:.3f}")

    # salvataggio
    file_path = os.path.join(os.path.dirname(__file__), "exp_results.csv")
    df.to_csv(file_path, index = False)

    print("\nRisultati salvati correttamente in: exp_results.csv\n")

# generazione grafico
def graph(df, title, cols, name, y_label):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "plots")

    plt.figure(figsize = (10, 6))

    # acquisizione dati numerici
    df[cols[0]] = pd.to_numeric(df[cols[0]])
    df[cols[1]] = pd.to_numeric(df[cols[1]])
    df[cols[2]] = pd.to_numeric(df[cols[2]])

    # definizione legenda
    plt.plot(df["Items(n)"], df[cols[0]], label = "BST")
    plt.plot(df["Items(n)"], df[cols[1]], label = "AVL")
    plt.plot(df["Items(n)"], df[cols[2]], label = "RBT")

    plt.title(title)
    plt.xlabel("Elementi(n)")
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)

    # salvataggio nella cartella e chiusura
    save_path = os.path.join(output_folder, name)
    plt.savefig(save_path)
    plt.close()


# MAIN
if __name__ == "__main__":
    print("aaaaa")
    pull_size = 1000 # numero massimo di elementi da campionare
    num_test = 1 # qty test per ricavare la media
    increment = 200 # passo incrementale (definisce densità dei punti)
    max_value = 10000 # valore massimo che una chiave può avere

    tester = Tester(pull_size, num_test, increment, max_value)
    dataframe = tester.test_manager()

    # salvataggio nel foglio di calcolo
    spreadsheet(dataframe)

    # generazione grafici
    graph(dataframe, "Inserimento - Caso Sequenziale",
          ["Insert_BST_Seq(ms)", "Insert_AVL_Seq(ms)", "Insert_RBT_Seq(ms)"], "insert_seq_graph.png",
                     "Tempo(ms)")
    graph(dataframe, "Inserimento - Caso Randomizzato",
          ["Insert_BST_Rand(ms)", "Insert_AVL_Rand(ms)", "Insert_RBT_Rand(ms)"], "insert_rand_graph.png",
                     "Tempo(ms)")
    graph(dataframe, "Altezza - Caso sequenziale", ["Height_BST_Seq(n)", "Height_AVL_Seq(n)", "Height_RBT_Seq(n)"],
                     "height_seq_graph.png", "Altezza(h)")
    graph(dataframe, "Altezza - Caso Randomizzato", ["Height_BST_Rand(n)", "Height_AVL_Rand(n)", "Height_RBT_Rand(n)"],
                     "height_rand_graph.png", "Altezza(h)")

    graph(dataframe, "Ricerca - Caso Sequenziale", ["Search_BST_Seq(ms)", "Search_AVL_Seq(ms)", "Search_RBT_Seq(ms)"],
                     "search_seq_graph.png", "Tempo(ms)")
    graph(dataframe, "Ricerca - Caso Randomizzato",
          ["Search_BST_Rand(ms)", "Search_AVL_Rand(ms)", "Search_RBT_Rand(ms)"], "search_rand_graph.png",
                     "Tempo(ms)")