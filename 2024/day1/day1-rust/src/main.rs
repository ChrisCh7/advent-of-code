use std::collections::HashMap;
use std::error::Error;
use std::fs;

fn main() -> Result<(), Box<dyn Error>> {
    let lines: Vec<Vec<i32>> = fs::read_to_string("../in.txt")?
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|n| n.parse().unwrap())
                .collect()
        })
        .collect();

    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();

    for line in lines {
        list1.push(line[0]);
        list2.push(line[1]);
    }

    list1.sort();
    list2.sort();

    println!(
        "Part 1: {}",
        list1
            .iter()
            .zip(list2.iter())
            .map(|(a, b)| (a - b).abs())
            .sum::<i32>()
    );

    let mut counts_list2: HashMap<i32, i32> = HashMap::new();
    for &num in &list2 {
        *counts_list2.entry(num).or_insert(0) += 1;
    }

    println!(
        "Part 2: {}",
        list1
            .iter()
            .map(|&n| n * counts_list2.get(&n).unwrap_or(&0))
            .sum::<i32>()
    );

    Ok(())
}
