use std::fs;
use std::collections::HashSet;


fn main() {
    let contents = fs::read_to_string("input.txt").expect("Failed to read file");

    println!("Part1 - Start-of-packet marker found after character {}", part1(&contents, 4));
    println!("Part2 - Start-of-message marker found after character {}", part1(&contents, 14));
}


fn part1(contents: &String, char_count: usize) -> usize{
    // let mut iter = contents.iter().peekable()
    // for char in iter {
    // }

    let mut slice: &str;
    let end_idx = contents.len() - char_count;
    for start_idx in 0..end_idx {
        slice = &contents[start_idx..(start_idx+char_count)];
        let set = slice.chars().collect::<HashSet<char>>();
        if set.len() == char_count {
            return start_idx + char_count;
        }
    }
    return 0; // TODO: learn to throw exceptions
}
