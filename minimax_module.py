def minimax(node, depth, alpha, beta, maximizingPlayer, tree, leaf_nodes, evaluated_leaves, pruned_leaves):
    if depth == 0 or node not in tree:
        if node in leaf_nodes:
            evaluated_leaves.add(node)
            return leaf_nodes[node]
        else:
            return 0

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in tree[node]:
            eval = minimax(child, depth - 1, alpha, beta, False, tree, leaf_nodes, evaluated_leaves, pruned_leaves)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                prune_siblings(tree[node], child, tree, leaf_nodes, pruned_leaves)
                break
        return maxEval
    else:
        minEval = float('inf')
        for child in tree[node]:
            eval = minimax(child, depth - 1, alpha, beta, True, tree, leaf_nodes, evaluated_leaves, pruned_leaves)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                prune_siblings(tree[node], child, tree, leaf_nodes, pruned_leaves)
                break
        return minEval

def prune_siblings(siblings, current_child, tree, leaf_nodes, pruned_leaves):
    index = siblings.index(current_child)
    for sibling in siblings[index + 1:]:
        mark_pruned(sibling, tree, leaf_nodes, pruned_leaves)

def mark_pruned(node, tree, leaf_nodes, pruned_leaves):
    if node in leaf_nodes:
        pruned_leaves.add(node)
    elif node in tree:
        for child in tree[node]:
            mark_pruned(child, tree, leaf_nodes, pruned_leaves)
