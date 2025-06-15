use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    // parse() return Result
    let n: i32 = input.trim().parse().unwrap();

    for _ in 0..n {
        println!("SciComLove");
    }
}
