use std::collections::HashSet;


fn main() {
    let mut chars = HashSet::new();

    chars.insert('x');
    chars.insert('y');
    chars.insert('z');
    chars.insert('z');

    println!("We have {} chars", &chars.len());
}
