// Develop a program to convert currency X to currency Y and visa versa.

use std::io;

fn input_to_int(&mut input: String) {
    
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read from stdin");

    let mut num = input.trim().parse::<i32>().unwrap();

    return num;
}

fn main() {

    println!("Currency conversion program!")

    let mut num_to_input = String::new();
    let mut num_from_input = String::new();

    let mut num_to = input_to_int(num_to_input);
    let mut num_from = input_to_int(num_from_input);

    println!("Converting £{} to ${}", num_to, num_from)
}
