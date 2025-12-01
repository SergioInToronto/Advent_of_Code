use std::fs;


fn elf_sections(range: &str) -> Vec<usize> {
    let mut iter = range.split("-");
    let start: usize = iter.next().unwrap().parse::<usize>().unwrap();
    let end: usize = iter.next().unwrap().parse::<usize>().unwrap();
    return (start..=end).collect::<Vec<usize>>();
}


fn part1(contents: &String) {
    let mut count = 0;
    for line in contents.trim_end().split("\n") {
        // I haven't yet figured out nice line splitting. Nice according to me lol.
        // let (elf1, elf2): (&str, &str) = line.split(",").collect::<Vec<&str>>();

        let mut iter = line.split(",");
        let elf1 = iter.next().unwrap();
        let elf2 = iter.next().unwrap();
        println!("Elfs: {:?}, {:?}", &elf1, &elf2);
        let sections1 = elf_sections(&elf1);
        let sections2 = elf_sections(&elf2);

        if sections1.iter().all(|&x| sections2.contains(&x)) || sections2.iter().all(|&x| sections1.contains(&x)) {
            count = count + 1;
        }
    }

    println!("count: {}", count); // part2 is simply changing .all() to .any() above.
}


fn main() {
    // println!("testing stuff: {:?}, {}", (0..4).collect::<Vec<usize>>(), (0..4).contains(&2));

    let contents = fs::read_to_string("input.txt").expect("Failed to read file");

    part1(&contents);
}
