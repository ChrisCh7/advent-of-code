use std::fs;

fn main() {
    let depths = fs::read_to_string("../in.txt")
        .expect("Error reading file")
        .lines()
        .map(|x| x.parse::<i32>().expect("Error converting to int"))
        .collect::<Vec<_>>();

    part1(&depths);
    part2(&depths);
}

fn part1(depths: &[i32]) {
    let mut nr_increases = 0;

    for n in 1..depths.len() {
        if depths[n] > depths[n - 1] {
            nr_increases += 1;
        }
    }

    println!("Part 1: {nr_increases}");
}

fn part2(depths: &[i32]) {
    let mut nr_increases = 0;
    let mut prev_sum = 0;

    for n in 0..depths.len() - 2 {
        if prev_sum == 0 {
            prev_sum = depths[n] + depths[n + 1] + depths[n + 2];
            continue;
        }

        let current_sum = depths[n] + depths[n + 1] + depths[n + 2];

        if current_sum > prev_sum {
            nr_increases += 1;
        }

        prev_sum = current_sum;
    }

    println!("Part 2: {nr_increases}");
}