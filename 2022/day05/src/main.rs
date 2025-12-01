use std::fs;
use std::str::FromStr;


const LETTERS: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


#[derive(Debug, PartialEq)]
struct CraneInstruction {
    count: usize,
    source: usize,
    dest: usize,
}


impl FromStr for CraneInstruction {
    type Err = std::num::ParseIntError;

    fn from_str(instruction: &str) -> Result<Self, Self::Err> {
        // println!("Parsing line: {}", &instruction);
        let mut parts = instruction.split(" ");
        // Result<usize, _>
        let count: usize = parts.nth(1).unwrap().parse().unwrap();
        let source: usize = parts.nth(1).unwrap().parse().unwrap();
        let dest: usize = parts.nth(1).unwrap().parse().unwrap();
        // println!("Instruction: move {:?} from {:?} to {:?}", count, source, dest);
        
        // return Ok(CraneInstruction{count: 0, source: 0, dest: 0})
        return Ok(CraneInstruction{count, source, dest})
    }
    // In hindsight this was exessive, but good learning. A function returning a tuple of 3 values would have been equally readable with a lot less code.
}


fn initalize_stacks(initial_stacks: &str) -> [Vec<char>; 9] {
    let mut stacks = [
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
        Vec::new(),
    ];
    let mut iter = initial_stacks.trim_end().rsplit("\n"); // rsplit, go from the bottom up
    iter.next(); // ignore the last line - it tells us how many stacks. We've already hard-coded 9
    let mut stack_idx: usize;
    for line in iter { 
        for (idx, c) in line.chars().enumerate() {
            if !LETTERS.contains(c) {
                continue
            }
            stack_idx = (idx - 1) / 4;
            stacks[stack_idx].push(c);
        }
    }
    // println!("Loaded stacks: {:?}", &stacks);
    return stacks;
}


fn read_tops(stacks: &[Vec<char>; 9]) -> String {
    // let tops: &str = &stacks.iter().map(|s: &Vec<char>| s.last().unwrap()).collect();
    let mut tops = String::from("");
    for stack in stacks {
        tops.push(*stack.last().unwrap());
    }
    return tops;
}


fn part1(mut stacks: [Vec<char>; 9], instructions: &str) {
    for line in instructions.trim_end().split("\n") {
        let instruction = CraneInstruction::from_str(line).unwrap();
        
        // println!("{}", line);
        
        let mut letter: char; // "crate" and "box" were both reserved keywords???
        for _step in 0..(instruction.count) {
            // println!("MOVING FROM {} TO {}", instruction.source, instruction.dest);
            letter = stacks[instruction.source - 1].pop().unwrap();
            stacks[instruction.dest - 1].push(letter);
        }
        // println!("{:?}", &stacks);
    }
    println!("Part1: {}", read_tops(&stacks));
}


fn part2(mut stacks: [Vec<char>; 9], instructions: &str) {
    let mut instruction: CraneInstruction;
    let mut start_index: usize;
    let mut letters: Vec<char>;
    for line in instructions.trim_end().split("\n") {
        instruction = CraneInstruction::from_str(line).unwrap();
        
        start_index = &stacks[instruction.source - 1].len() - instruction.count;
        letters = stacks[instruction.source - 1].drain(start_index..).collect();
        stacks[instruction.dest - 1].extend(letters);
    }
    println!("Part2: {}", read_tops(&stacks));
}


fn main() {
    let contents = fs::read_to_string("input.txt").expect("Failed to read file");

    let mut parts = contents.split("\n\n");
    let initial_stacks = parts.next().unwrap();
    let instructions = parts.next().unwrap();

    let mut stacks = initalize_stacks(initial_stacks);

    part1(stacks.clone(), &instructions);
    part2(stacks.clone(), &instructions);
}
