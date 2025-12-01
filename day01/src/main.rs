use std::fs;


fn part1and2(contents: String) {
    let mut max_calories: i32 = 0;
    let mut top_calories: [i32; 3] = [0, 0, 0];
    let mut total: i32 = 0;

    let mut min_top_3: i32 = 0;
    let mut position: usize;
    for (i, inventory) in contents.trim_end().to_string().split("\n\n").enumerate() {
        // dbg!(inventory);
        print!("Inspecting self {}... ", i);
        total = 0;
        
        for item in inventory.split("\n") {
            let item_calories = item.parse::<i32>().unwrap();
            total = total + item_calories;
        }
        print!("{} calories", total);
        if total > max_calories {
            max_calories = total;
        }
        
        min_top_3 = *top_calories.iter().min().unwrap();
        if min_top_3 < total {
            print!(" - New higest! (prev max: {})", min_top_3);
            position = top_calories.iter().position(|&r| r == min_top_3).unwrap();
            top_calories[position] = total;
        }
        println!("");
    }
    println!("\nPart1: Elf carring the most calories: {}", max_calories);
    let sum_top_3 = top_calories.iter().sum::<i32>();
    println!("Part2: Top 3 most calories: {:?}. Total: {}", top_calories, sum_top_3);
}


fn main() {
    // let args: Vec<String> = env::args().collect();
    // dbg!(args);

    let filename = "input.txt";
    println!("Reading file {}...", filename);
    let contents = fs::read_to_string(filename)
        .expect("Should have been able to read file");
    println!("Loaded contents with length: {}", contents.len());

    part1and2(contents);

}
