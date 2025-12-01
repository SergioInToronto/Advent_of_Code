fn main() {
    let vec: Vec<String> = Vec::new();
    vec.push(String::from("Some"));
    vec.push(String::from(" text"));
    vec.push(String::from(" in"));
    vec.push(String::from(" here"));
    vec.push(String::from("\n"));
    vec.push(String::from("but does it work?"));

    let last_count: isize = -4;
    println!("Result: {:?}", vec.drain(last_count..));
}
