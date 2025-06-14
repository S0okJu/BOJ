use std::io;

fn add(i: i32, j: i32) -> i32 {
    i + j
}

fn subtract(i: i32, j: i32) -> i32 {
    i - j
}

fn multiple(i: i32, j: i32) -> i32 {
    i * j
}

fn div(i: i32, j: i32) -> (i32, i32) {
    (i / j, i % j)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let mut iter = input.trim().split_whitespace();
    let a: i32 = iter.next().unwrap().parse().unwrap();
    let b: i32 = iter.next().unwrap().parse().unwrap();

    println!("{}", add(a, b));
    println!("{}", subtract(a, b));
    println!("{}", multiple(a, b));

    let (quotient, remainder) = div(a, b);
    println!("{}", quotient);
    println!("{}", remainder);
}
