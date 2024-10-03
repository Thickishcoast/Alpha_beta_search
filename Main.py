from minimax_module import minimax

def main():
    leaf_values = list(map(int, input().split()))
    if len(leaf_values) != 12:
        print("Please enter exactly 12 numbers.")
        return

    tree = {
        0: [1, 2, 3],
        1: [4, 5],
        2: [6, 7],
        3: [8, 9],
        4: [10, 11],
        5: [12, 13],
        6: [14, 15],
        7: [16, 17],
        8: [18, 19],
        9: [20, 21],
    }

    leaf_nodes = {10 + i: leaf_values[i] for i in range(12)}
    evaluated_leaves = set()
    pruned_leaves = set()

    minimax(0, 3, float('-inf'), float('inf'), True, tree, leaf_nodes, evaluated_leaves, pruned_leaves)

    pruned_indices = sorted(leaf - 10 for leaf in pruned_leaves)
    evaluated_indices = sorted(leaf - 10 for leaf in evaluated_leaves)

    print('Pruned leaf indices:', ' '.join(map(str, pruned_indices)))
    print('Evaluated leaf indices:', ' '.join(map(str, evaluated_indices)))

if __name__ == "__main__":
    main()
