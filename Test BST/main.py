import time
import random
import statistics
import numpy as np
import pandas as pd
import os

from src.BST import BST
from src.AVL import AVL
from src.RBT import RBT

# generazione sequenze numeriche
def setup_sequence(size):
    sequence = list(range(size))
    return sequence

def setup_randomized(size):
    randomized = [random.randint(1, 1000) for _ in range(size)]
    return randomized

# test inserimento
def insertion_test(sequence, randomized, tree, num_test):
    optime = np.zeros((2, num_test))
    height = np.zeros((2, num_test))

    for j in range(num_test):
        # sequence test
        start = time.perf_counter()
        for i in range(len(sequence)):
            tree.insert(sequence[i])
        end = time.perf_counter()

        optime[0][j] = end - start
        height[0][j] = tree.get_height(tree.root)
        tree.reset()

        # randomized test
        start = time.perf_counter()
        for i in range(len(randomized)):
            tree.insert(randomized[i])
        end = time.perf_counter()

        optime[1][j] = end - start
        height[1][j] = tree.get_height(tree.root)
        tree.reset()

    # approssimazione risultati
    res_seq = statistics.median(optime[0]) * 1000
    res_rand = statistics.median(optime[1]) * 1000
    height_seq = statistics.median(height[0])
    height_rand = statistics.median(height[1])
    return res_seq, res_rand, height_seq, height_rand

# test ricerca
def search_test(sequence, randomized, search_target, tree, num_test):
    optime = np.zeros((2, num_test))

    # sequence
    for i in range(len(sequence)):
        tree.insert(sequence[i])

    for j in range(num_test):
        start = time.perf_counter()
        for i in range(len(sequence)):
            tree.search(search_target[i])
        end = time.perf_counter()
        optime[0][j] = end - start
    tree.reset()

    # randomized
    for i in range(len(randomized)):
        tree.insert(randomized[i])

    for j in range(num_test):
        start = time.perf_counter()
        for i in range(len(randomized)):
            tree.search(search_target[i])
        end = time.perf_counter()
        optime[1][j] = end - start
    tree.reset()

    res_seq = statistics.median(optime[0])
    res_rand = statistics.median(optime[1])
    return res_seq, res_rand

# test manager
def test_manager(pull, tests, inc):
    bst = BST()
    avl = AVL()
    rbt = RBT()
    res1, res2, res3, res4, res5, res6 = [], [], [], [], [], []

    for items in range(inc, pull + 1, inc):
        # valori che popoleranno gli alberi per eseguire i test
        sequence = setup_sequence(items)
        randomized = setup_randomized(items)

        res1.append(insertion_test(sequence, randomized, bst, tests))
        res2.append(insertion_test(sequence, randomized, avl, tests))
        res3.append(insertion_test(sequence, randomized, rbt, tests))

        search_target = setup_randomized(items)
        res4.append(search_test(sequence, randomized, search_target, bst, tests))
        res5.append(search_test(sequence, randomized, search_target, avl, tests))
        res6.append(search_test(sequence, randomized, search_target, rbt, tests))

        print("Elementi testati: ", items, "/", pull)

    # definizione colonne
    data = {
        "Items_insert(N)": list(range(inc, pull + 1, inc)),
        "Insert_BST_Seq(ms)": [x[0] for x in res1],
        "Insert_BST_Rand(ms)": [x[1] for x in res1],
        "Height_BST_Seq(N)": [x[2] for x in res1],
        "Height_BST_Rand(N)": [x[3] for x in res1],

        "Insert_AVL_Seq(ms)": [x[0] for x in res2],
        "Insert_AVL_Rand(ms)": [x[1] for x in res2],
        "Height_AVL_Seq(N)": [x[2] for x in res2],
        "Height_AVL_Rand(N)": [x[3] for x in res2],

        "Insert_RBT_Seq(ms)": [x[0] for x in res3],
        "Insert_RBT_Rand(ms)": [x[1] for x in res3],
        "Height_RBT_Seq(N)": [x[2] for x in res3],
        "Height_RBT_Rand(N)": [x[3] for x in res3],

        "Items_research(N)": list(range(inc, pull + 1, inc)),
        "Search_BST_Seq(ms)": [x[0] for x in res4],
        "Search_BST_Rand(ms)": [x[1] for x in res4],
        "Search_AVL_Seq(ms)": [x[0] for x in res5],
        "Search_AVL_Rand(ms)": [x[1] for x in res5],
        "Search_RBT_Seq(ms)": [x[0] for x in res6],
        "Search_RBT_Rand(ms)": [x[1] for x in res6]
    }

    df = pd.DataFrame(data)

    time_cols = [
        "Insert_BST_Seq(ms)", "Insert_BST_Rand(ms)",
        "Insert_AVL_Seq(ms)", "Insert_AVL_Rand(ms)",
        "Insert_RBT_Seq(ms)", "Insert_RBT_Rand(ms)",
        "Search_BST_Seq(ms)", "Search_BST_Rand(ms)",
        "Search_AVL_Seq(ms)", "Search_AVL_Rand(ms)",
        "Search_RBT_Seq(ms)", "Search_RBT_Rand(ms)"
    ]

    int_cols = [
        "Items_insert(N)", "Items_research(N)",
        "Height_BST_Seq(N)", "Height_BST_Rand(N)",
        "Height_AVL_Seq(N)", "Height_AVL_Rand(N)",
        "Height_RBT_Seq(N)", "Height_RBT_Rand(N)"
    ]

    # formattazione valori
    for col in int_cols:
        df[col] = df[col].astype(int)

    for col in time_cols:
        df[col] = df[col].map(lambda x: f"{x:.5f}")

    # salvataggio
    file_path = os.path.join(os.path.dirname(__file__), "exp_results.csv")
    df.to_csv(file_path, index = False)

    print(f"\nRisultati salvati correttamente in: exp_results.csv\n")

# MAIN
if __name__ == "__main__":
    pull_size = 3000 # numero massimo di elementi da campionare
    num_test = 10 # qty test per ricavare la media
    increment = 100 # passo incrementale (definisce densità dei punti)

    test_manager(pull_size, num_test, increment)
