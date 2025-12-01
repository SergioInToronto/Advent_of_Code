fn main() {
    let tup = (32, 64, 12.8, 'z', "This is sparta");
    dbg!(tup);
    
    println!("-------");
    // let mut words = "some string here".to_string().split(" ");
    let mut words = tup.4.split(" ");

    dbg!(&words);
    // dbg!(words); // Doesn't work, because ownership is transfered to dbg! so we couldn't use it later
    dbg!(words.clone());
    
    for word in words {
        println!("Word: {}", word);
    }

    // if let Some(first) = words.next() {
    //     if let Some(second) = words.next() {
    //         println!("First: {}", first);
    //         println!("Second: {}", second);
    //     }
    // }

    println!("-------");
    let str1 = String::from("this");
    let str2: &str = "this";
    if str1 == str2 {
        println!("They are equal.");
    } else {
        println!("They are NOT equal!");
    }
    
}
