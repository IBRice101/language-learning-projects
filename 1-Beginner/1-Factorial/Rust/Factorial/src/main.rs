use std::io;

fn main() {
    // enter number
    println!("Enter a number to be factorialised!");

    let mut num_in = String::new(); // string initially

    // standard input
    io::stdin()
        .read_line(&mut num_in)
        .expect("Failed to read from stdin");

    // trim
    let mut num = num_in.trim().parse::<i32>().unwrap();

    // factorial
    let num_original = num;

    for i in 1..num {
        num *= i;
    }

    println!("{} factorial is: {}", num_original, num);
}
