use std::io;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=9);
    
    let mut guess = String::new();
    println!("Give us a guess:");
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
    guess.pop(); // remove newline from pressing enter
    let int_guess = guess.parse::<i32>().unwrap();
    println!("You guessed: {int_guess}");
    println!("the number was {secret_number}");

    if secret_number == int_guess {
        println!("You guessed correctly!")
    } else {
        println!("You got it wrong :(")
    }

    println!("");

    let x = 5;
    let y = 10;
    println!("x = {x} and y + 2 = {}", y + 2);
}
