use std::fs;

fn main() {
    // let instructions = fs::read_to_string("test_input.txt").expect("Failed to read file");
    let instructions = fs::read_to_string("input.txt").expect("Failed to read file");

    part1(&instructions);
    part2(&instructions);
}

fn part1(instructions: &String) {
    let mut register_x: isize = 1;
    let mut program_counter: isize = 0;
    let mut interesting_signals: Vec<isize> = Vec::new();
    for instruction in instructions.trim_end().split("\n") {
        program_counter = program_counter + 1;
        if (program_counter + 20) % 40 == 0 {
            let signal_strength = program_counter * register_x; // We're just throwing around tech words at this point
            println!(
                "Interesting signal at cycle count {} - {}",
                program_counter, &signal_strength
            );
            interesting_signals.push(signal_strength);
        }
        if instruction == "noop" {
            continue;
        }
        let delta = instruction.split(" ").nth(1).unwrap();
        program_counter = program_counter + 1;
        println!("addx {}", &delta);
        if (program_counter + 20) % 40 == 0 {
            let signal_strength = program_counter * register_x; // We're just throwing around tech words at this point
            println!(
                "Interesting signal at cycle count {} - {}",
                program_counter, &signal_strength
            );
            interesting_signals.push(signal_strength);
        }
        register_x = register_x + delta.parse::<isize>().unwrap();
    }

    let total: isize = interesting_signals.iter().sum();
    println!("Part1 - {}", total); // GOTEM first try!
}

fn part2(instructions: &String) {
    // This display draws left-to-right, row-by-row.
    // It draws a pixel per cycle.
    // There's a "video buffer" containing a "sprite" 3 pixels wide
    // register_x moves the MIDDLE of the sprite
    // eg: register_x=1 means the sprite spans indexes 0..=2
    // As we draw, if the video buffer contains the sprite, render bright. Else render dark.

    // const display_width = 40;
    // const display_height = 6;

    let mut register_x: isize = 1;
    let mut output = String::from("");
    let mut program_counter: isize = 0;

    // Some instructions take 2 cycles, so they draw 2 pixels
    for instruction in instructions.trim_end().split("\n") {
        draw((&mut output), program_counter, register_x);
        program_counter = program_counter + 1;
        if instruction == "noop" {
            continue;
        }
        draw((&mut output), program_counter, register_x);
        program_counter = program_counter + 1;

        let delta = instruction.split(" ").nth(1).unwrap();
        println!("addx {}", &delta);
        register_x = register_x + delta.parse::<isize>().unwrap();
    }

    println!("{output}"); // PHLHJGZA
    println!("Part2 - what's it look like Jim?");
}

fn draw(output: &mut String, pc: isize, reg_x: isize) {
    let h_pos = (pc % 40);
    if (h_pos == reg_x) || (h_pos - 1 == reg_x) || (h_pos + 1 == reg_x) {
        output.push('#');
    } else {
        output.push(' ');
    }
    if (pc + 1) % 40 == 0 {
        output.push('\n');
    }
}
