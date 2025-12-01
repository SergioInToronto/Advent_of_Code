use std::fs;


const LETTERS: &str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";


fn find_common_item(items1: &str, items2: &str) -> char {
    for x in items1.chars() {
        if items2.contains(x) {
            // println!("Common item: {}", &x);
            return x.clone();
        }
    }
    return '_';
}

fn find_common_item_of_3(items1: &str, items2: &str, items3: &str) -> char {
    for x in items1.chars() {
        if items2.contains(x) && items3.contains(x) {
            // println!("Common item: {}", &x);
            return x.clone();
        }
    }
    return '_';
}


fn part1(contents: &String) {
    let mut total_priorities = 0;
    for row in contents.trim_end().split("\n") {
        let midpoint: usize = &row.len() / 2;
        // println!("Midpoint: {} Items: {}", midpoint, &row.len());
        let items1 = &row[..midpoint];
        let items2 = &row[midpoint..];
        
        let common_item = find_common_item(&items1, &items2);
        let item_priority = LETTERS.find(common_item).unwrap() + 1;
        // println!("Priority: {}", &item_priority);
        total_priorities = total_priorities + item_priority;
        
        // println!("Items1: {}, items2: {}", &items1, &items2);
    }

    println!("Part1 - Total priorities: {}", total_priorities);
}


fn part2(contents: &String) {
    // let line_count = contents.trim_end().split("\n").collect().len();
    // dbg!(line_count);
    let mut total_priorities = 0;
    let mut bags_iter = contents.trim_end().split_whitespace();
    loop { // TODO: use .iter().step_by(3) instead ??
        let bag1 = bags_iter.next();
        let bag2 = bags_iter.next();
        let bag3 = bags_iter.next();
        if bag1 == None || bag2 == None || bag3 == None {
            break
        }
        let badge = find_common_item_of_3(&bag1.unwrap(), &bag2.unwrap(), &bag3.unwrap());
        let priority = LETTERS.find(badge).unwrap() + 1;
        total_priorities = total_priorities + priority;
        // println!("Group Badge: {}", &badge);
    }

    println!("Part2 - Total badge priorities: {}", total_priorities);
}


fn main() {
    let contents = fs::read_to_string("input.txt").expect("Failed to read file");

    part1(&contents);

    part2(&contents);
}
