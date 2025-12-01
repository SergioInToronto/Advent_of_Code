

lines = open('input.txt').read().strip().split('\n')

# -X
# ^
# | 2024120
# | 1416332
# | 3375241
# |--------> Y
# 
# part1: how many trees are visible from the outside?

forest = []
for line in lines:
    forest.append([int(c) for c in line])
print(f"Finished loading")
# print(f"Forest is {len(forest)} rows each containing {len(forest[0])} trees")
# total Trees: 9801


def visible_above_or_below(height, x, y):
    column = [row[y] for row in forest]
    trees_above = column[:x]
    trees_below = column[x+1:]
    # if not trees_above or not trees_below: # tree is at the edge
    #     return True
    return (max(trees_above) < height) or (max(trees_below) < height)


def visible_left_or_right(height, x, y):
    trees_left = forest[x][:y]
    trees_right = forest[x][y+1:]
    # if not trees_left or not trees_right: # tree is at the edge
    #     return True
    return ((max(trees_left) < height) or (max(trees_right) < height))


visible_outside_count = 0
for row_idx, row in enumerate(forest):
    for col_idx, tree in enumerate(row):
        # if row_idx == 1 and col_idx == 4:
        #     breakpoint()
        if (
            row_idx == 0 or row_idx == len(forest) - 1 or
            col_idx == 0 or col_idx == len(row) - 1 or
            visible_above_or_below(tree, row_idx, col_idx) or
            visible_left_or_right(tree, row_idx, col_idx)
        ):
            visible_outside_count += 1

print(f"Trees visible from outside the forest: {visible_outside_count}")
# 2140 is too high. I had a logic bug in visible_above_or_below() - used x instead of y

# --- part2 ---
def calc_score(height, trees):
    score = 0
    for tree in trees:
        score += 1
        if tree >= height:
            break
    return score

tree_scores = []
for x, row in enumerate(forest):
    for y, tree in enumerate(row):
        column = [row[y] for row in forest]
        trees_above = column[:x]
        trees_above.reverse() # inspect trees from bottom to top
        trees_below = column[x+1:]
        trees_left = forest[x][:y]
        trees_left.reverse() # inspect trees from right to left
        trees_right = forest[x][y+1:]
        up_score = calc_score(tree, trees_above)
        down_score = calc_score(tree, trees_below)
        left_score = calc_score(tree, trees_left)
        right_score = calc_score(tree, trees_right)
        total_score = up_score * down_score * left_score * right_score
        if x == 20 and y == 6:
            print(left_score, right_score, up_score, down_score)
            # breakpoint()
        tree_scores.append(total_score)

print(f"Best tree score: {max(tree_scores)}")
# 1920996 is too high. I was missing .reverse() to inspect trees in the correct order