use regex::Regex;
use std::fs;

fn main() {
    let program = fs::read_to_string("../in.txt").unwrap();

    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let pairs: Vec<(i32, i32)> = re
        .captures_iter(&program)
        .map(|pair| (pair[1].parse().unwrap(), pair[2].parse().unwrap()))
        .collect();

    println!(
        "Part 1: {}",
        pairs.iter().map(|pair| pair.0 * pair.1).sum::<i32>()
    );

    let re = Regex::new(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))").unwrap();

    let mut result = 0;
    let mut is_do = true;

    for m in re.captures_iter(&program) {
        match (m.get(1), m.get(2), m.get(3), m.get(4)) {
            (Some(a), Some(b), None, None) => {
                if is_do {
                    result +=
                        a.as_str().parse::<i32>().unwrap() * b.as_str().parse::<i32>().unwrap();
                }
            }
            (None, None, Some(val), None) if val.as_str() == "do()" => is_do = true,
            (None, None, None, Some(val)) if val.as_str() == "don't()" => is_do = false,
            _ => {}
        }
    }

    println!("Part 2: {result}");
}
