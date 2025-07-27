use std::io;

fn main() {
    let mut numbers: [i8; 9] = [0;9];

    for i in 0..9{
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        numbers[i] = input.trim().parse().unwrap();
    }
    
    // 가변 변수 
    let mut max = numbers[0];
    let mut max_idx = 0;
    // enumerate는 value를 포인터로 받는다. 
    for (i, v) in numbers.iter().enumerate() {
        if max < *v {
            max = *v;
            max_idx = i;
        }
    }

    println!("{}", max);
    println!("{}", max_idx+1);
}
