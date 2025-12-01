use std::{fs, result};
use std::collections::HashMap;


fn main() {
    let instructions = fs::read_to_string("input.txt").expect("Failed to read file");

    let mut sizes: HashMap<String, isize> = HashMap::new();
    sizes.insert(String::from("/"), -1); // directories are -1 until we compute their size

    sizes = parse_instructions(&instructions, sizes);
    sizes = compute_directory_sizes(sizes);
    part1(&sizes);
    part2(&sizes);
}


fn part1(sizes: &HashMap<String, isize>) {
    let size_at_most = 100000;
    let sum_of_small_directories: isize = sizes.iter().filter(|(k, &v)| k.ends_with(("/")) && v < size_at_most).map(|(_, &v)| v).sum();
    println!("part1 - Sum of small directories: {}", sum_of_small_directories);
}


fn part2(sizes: &HashMap<String, isize>) {
    let disk_space: isize = 70_000_000;
    let used_space = sizes["/"];
    let free_space = disk_space - used_space;
    let additional_needed_space = 30_000_000 - free_space;
    // Find 1 directory to delete which would free up enough space. Return the directory's size 
    let result: isize = sizes.iter().filter(|(k, &v)| k.ends_with(("/")) && v >= additional_needed_space).map(|(_, &v)| v).min().unwrap();
    println!("part2 - smallest directory size that would free up enough space if deleted: {result}");
}


fn parse_instructions(instructions: &String, mut sizes: HashMap<String, isize>) -> HashMap<String, isize> {
    let mut current_path: Vec<&str> = Vec::new();
    current_path.push("");
    
    for instruction in instructions.trim_end().split("\n") {
        // println!("Handling: {}", &instruction);
        if ["$ ls", "$ cd /"].contains(&instruction) {
            // No useful information here. Continue.
        } else if instruction == "$ cd .." {
            current_path.pop();
        } else if &instruction[0..5] == "$ cd " {
            // let dir_name = &instruction[6..]; // THIS WAS THE BUG. Should have been [5..]
            let dir_name = &instruction[5..];
            current_path.push(dir_name);
            continue;
        } else {
            let mut parts = instruction.split(" ");
            let size_or_dir = parts.next().unwrap();
            let is_dir = size_or_dir == "dir";
            let size: isize = if is_dir { -1 } else { size_or_dir.parse::<isize>().unwrap() };
            let filename = parts.next().unwrap();
            let path = current_path.join("/") + "/" + filename + (if is_dir { "/"} else { "" });
            // let path = current_path.join("/") + "/" + filename;
            let key = path.to_string();
            sizes.insert(key, size);
        }
    }
    return sizes;
}


fn compute_directory_sizes(mut sizes: HashMap<String, isize>) -> HashMap<String, isize> {
    let sizes_copy = &sizes.clone(); // We'll read this copy while writing to the other
    let mut total: isize;
    // This is O(n^2). If performance mattered we'd revisit this code first
    for (d_path, d_size) in sizes_copy {
        if *d_size != -1 {
            continue;
        }
        // println!("Computing directory size for {} ...", d_path);
        total = 0;
        for (path, size) in sizes_copy {
            if !path.starts_with(d_path) || path.ends_with("/") {
                continue;
            }
            total = total + size;
        }
        // sizes.insert(d_path.to_owned() + "/", total);
        if let Some(entry) = sizes.get_mut(d_path) {
            *entry = total;
        }
    }
    return sizes;
}
