import time
import random
import statistics
import numpy as np
import pandas as pd
import os

from src.BST import BST
from src.AVL import AVL
from src.RBT import RBT

# genera liste di valori in base ai casi di utilizzo
def setup_sequence(size):
    sequence = list(range(size))
    return sequence

def setup_randomized(size):
    randomized = [random.randint(1, 1000) for _ in range(size)]
    return randomized

# test inserimento
def insertion_test(sequence, randomized, tree, num_test):
    optime = np.zeros((2, num_test))

    for j in range(num_test):
        # sequence test
        start = time.perf_counter()

        for i in range(len(sequence)):
            tree.insert(sequence[i])

        end = time.perf_counter()
        optime[0][j] = end - start
        tree.reset()

        # randomized test
        start = time.perf_counter()

        for i in range(len(randomized)):
            tree.insert(randomized[i])

        end = time.perf_counter()
        optime[1][j] = end - start
        tree.reset()

    res_seq = statistics.median(optime[0])
    res_rand = statistics.median(optime[1])
    return res_seq, res_rand

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
def test_manager():
    bst = BST()
    avl = AVL()
    rbt = RBT()
    res1 = []
    res2 = []
    res3 = []
    res4 = []
    res5 = []
    res6 = []

    # aumento la dimensione dei campioni di 10 in 10 fino a 1000
    pull_size = 3000
    num_test = 10
    increment = 100

    for items in range(increment, pull_size + 1, increment):
        # valori che popoleranno gli alberi per eseguire i test
        sequence = setup_sequence(items)
        randomized = setup_randomized(items)

        res1.append(insertion_test(sequence, randomized, bst, num_test))
        res2.append(insertion_test(sequence, randomized, avl, num_test))
        res3.append(insertion_test(sequence, randomized, rbt, num_test))

        search_target = setup_randomized(items)
        res4.append(search_test(sequence, randomized, search_target, bst, num_test))
        res5.append(search_test(sequence, randomized, search_target, avl, num_test))
        res6.append(search_test(sequence, randomized, search_target, rbt, num_test))

        print("Elementi testati: ", items, "/", pull_size)

    # definizione colonne
    data = {
        "Items1": list(range(increment, pull_size + 1, increment)),
        "Insert_BST_Seq": [x[0] for x in res1],
        "Insert_BST_Rand": [x[1] for x in res1],
        "Insert_AVL_Seq": [x[0] for x in res2],
        "Insert_AVL_Rand": [x[1] for x in res2],
        "Insert_RBT_Seq": [x[0] for x in res3],
        "Insert_RBT_Rand": [x[1] for x in res3],

        "Items2": list(range(increment, pull_size + 1, increment)),
        "Search_BST_Seq": [x[0] for x in res4],
        "Search_BST_Rand": [x[1] for x in res4],
        "Search_AVL_Seq": [x[0] for x in res5],
        "Search_AVL_Rand": [x[1] for x in res5],
        "Search_RBT_Seq": [x[0] for x in res6],
        "Search_RBT_Rand": [x[1] for x in res6]
    }

    df = pd.DataFrame(data)

    # formattazione forzata a 8 cifre decimali
    cols_to_format = df.columns.drop(["Items1", "Items2"])
    for col in cols_to_format:
        df[col] = df[col].map(lambda x: f"{x:.8f}")

    file_path = os.path.join(os.path.dirname(__file__), "exp_results.csv")
    df.to_csv(file_path, index = False)

    print(f"\nRisultati salvati correttamente in: exp_results.csv\n")

test_manager()
