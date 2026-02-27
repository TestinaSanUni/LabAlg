import time
import random
import statistics
import pandas as pd

from src.BST import BST
from src.AVL import AVL
from src.RBT import RBT

# generazione sequenze numeriche
def setup_sequence(size):
    sequence = list(range(size))
    return sequence

def setup_randomized(size, max):
    randomized = [random.randint(1, max) for _ in range(size)]
    return randomized


class Tester:
    # costruttore
    def __init__(self, pull_size, num_tests, increment, max_value):
        self.pull = pull_size
        self.tests = num_tests
        self.inc = increment
        self.max = max_value

    # test inserimento
    def insertion_test(self, tree, seq):
        optime, height = [], []

        for j in range(self.tests):
            start = time.perf_counter()
            for i in range(len(seq)):
                tree.insert(seq[i])
            end = time.perf_counter()

            optime.append(end - start)
            height.append(tree.get_height(tree.root))
            tree.reset()

        # approssimazione risultati
        res_seq = statistics.median(optime) * 1000
        height_seq = statistics.median(height)
        return res_seq, height_seq

    # test ricerca
    def search_test(self, tree, seq, search_target):
        optime = []

        # sequence
        for i in range(len(seq)):
            tree.insert(seq[i])

        for j in range(self.tests):
            start = time.perf_counter()
            for i in range(len(seq)):
                tree.search(search_target[i])
            end = time.perf_counter()
            optime.append(end - start)
        tree.reset()

        res_seq = statistics.median(optime)
        return res_seq

    # test manager
    def test_manager(self):
        bst = BST()
        avl = AVL()
        rbt = RBT()
        results = []

        for items in range(self.inc, self.pull + 1, self.inc):
            # setup
            row = {"Items(n)": items}
            seq = setup_sequence(items)
            rand = setup_randomized(items, self.max)
            target = setup_randomized(items, self.max)

            bst_insert_seq, bst_height_seq = self.insertion_test(bst, seq)
            bst_insert_rand, bst_height_rand = self.insertion_test(bst, rand)
            bst_search_seq = self.search_test(bst, seq, target)
            bst_search_rand = self.search_test(bst, rand, target)

            row.update({
                "Insert_BST_Seq(ms)": bst_insert_seq, "Insert_BST_Rand(ms)": bst_insert_rand,
                "Height_BST_Seq(n)": bst_height_seq, "Height_BST_Rand(n)": bst_height_rand,
                "Search_BST_Seq(ms)": bst_search_seq, "Search_BST_Rand(ms)": bst_search_rand
            })

            avl_insert_seq, avl_height_seq = self.insertion_test(avl, seq)
            avl_insert_rand, avl_height_rand = self.insertion_test(avl, rand)
            avl_search_seq = self.search_test(avl, seq, target)
            avl_search_rand = self.search_test(avl, rand, target)

            row.update({
                "Insert_AVL_Seq(ms)": avl_insert_seq, "Insert_AVL_Rand(ms)": avl_insert_rand,
                "Height_AVL_Seq(n)": avl_height_seq, "Height_AVL_Rand(n)": avl_height_rand,
                "Search_AVL_Seq(ms)": avl_search_seq, "Search_AVL_Rand(ms)": avl_search_rand
            })

            rbt_insert_seq, rbt_height_seq = self.insertion_test(rbt, seq)
            rbt_insert_rand, rbt_height_rand = self.insertion_test(rbt, rand)
            rbt_search_seq = self.search_test(rbt, seq, target)
            rbt_search_rand = self.search_test(rbt, rand, target)

            row.update({
                "Insert_RBT_Seq(ms)": rbt_insert_seq, "Insert_RBT_Rand(ms)": rbt_insert_rand,
                "Height_RBT_Seq(n)": rbt_height_seq, "Height_RBT_Rand(n)": rbt_height_rand,
                "Search_RBT_Seq(ms)": rbt_search_seq, "Search_RBT_Rand(ms)": rbt_search_rand
            })

            results.append(row)
            print("Elementi testati: ", items, "/", self.pull)

        dataframe = pd.DataFrame(results)
        return dataframe
