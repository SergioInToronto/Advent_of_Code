use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Failed to read file");

    let forest = initialize(&contents);

    part1(&forest);
    part2(&forest);
}

fn part1(forest: &Vec<Vec<usize>>) {
    let mut trees_visible_outside = 0;

    for (row_idx, row) in forest.iter().enumerate() {
        for (col_idx, _tree) in row.iter().enumerate() {
            let x: usize = row_idx.try_into().unwrap();
            let y: usize = col_idx.try_into().unwrap();
            if visible_from_outside(forest, x, y) {
                trees_visible_outside = trees_visible_outside + 1;
            }
        }
    }
    println!("Part1 - trees visible from outside: {trees_visible_outside}");
}

fn part2(forest: &Vec<Vec<usize>>) {
    let mut top_scenic_score = 0;
    let mut scenic_score: usize;
    for (row_idx, row) in forest.iter().enumerate() {
        for (col_idx, _tree) in row.iter().enumerate() {
            let x: usize = row_idx.try_into().unwrap();
            let y: usize = col_idx.try_into().unwrap();
            scenic_score = calc_scenic_score(&forest, x, y);
            if scenic_score > top_scenic_score {
                top_scenic_score = scenic_score;
            }
        }
    }
    println!("Part2 - best scenic score in the forest: {}", top_scenic_score);
}

fn calc_scenic_score(forest: &Vec<Vec<usize>>, x: usize, y: usize) -> usize {
    let height = forest[x][y];
    let column: Vec<_> = forest.iter().map(|r| r.iter().nth(y).unwrap()).collect();

    // I'm sure there is a better way...
    return calc_score(height, forest[x][..y].iter().rev().map(|&v| v).collect::<Vec<_>>().as_slice()) // notice .rev()
        * calc_score(height, forest[x][(y + 1)..].as_ref())
        * calc_score(height, column[..x].iter().rev().map(|&v| *v).collect::<Vec<_>>().as_slice()) // notice .rev()
        * calc_score(height, column[(x + 1)..].iter().map(|&v| *v).collect::<Vec<_>>().as_slice());
}

fn calc_score(height: usize, trees: &[usize]) -> usize {
    let mut score = 0;
    for tree in trees {
        score = score + 1;
        if *tree >= height {
            break;
        }
    }
    return score;
}

fn visible_from_outside(forest: &Vec<Vec<usize>>, x: usize, y: usize) -> bool {
    let height = forest[x][y];
    // println!("Testing ({x}, {y}) - {height}");

    let max_left = forest[x][..y].iter().max();
    let max_right = forest[x][(y + 1)..].iter().max();
    if max_left == None || max_right == None {
        return true;
    }
    let column: Vec<_> = forest.iter().map(|r| r.iter().nth(y).unwrap()).collect();
    let max_above = column[..x].iter().max();
    let max_below = column[(x + 1)..].iter().max();
    if max_above == None || max_below == None {
        return true;
    }
    return (height > *max_left.unwrap())
        || (height > *max_right.unwrap())
        || (height > **max_above.unwrap())
        || (height > **max_below.unwrap());
    // If it doesn't compile the first time, add more stars!
}

fn initialize(contents: &String) -> Vec<Vec<usize>> {
    let mut forest: Vec<Vec<usize>> = Vec::new();

    let mut tree_height: usize;
    let mut newest_row: &mut Vec<usize>;
    for row in contents.trim_end().split("\n") {
        forest.push(Vec::new());
        newest_row = forest.last_mut().unwrap();
        for c in row.chars() {
            tree_height = usize::try_from(c.to_digit(10).unwrap()).unwrap();
            newest_row.push(tree_height);
        }
    }
    return forest;
}
