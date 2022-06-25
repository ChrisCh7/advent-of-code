use std::fs;

fn main() {
    let instructions = fs::read_to_string("../in.txt")
        .expect("Error reading file")
        .lines()
        .map(|line| line.split_whitespace().collect::<Vec<_>>())
        .map(|parts| (parts[0].to_string(), parts[1].parse::<i32>().expect("Error parsing int")))
        .collect::<Vec<_>>();

    part1(&instructions);
    part2(&instructions);
}

fn part1(instructions: &[(String, i32)]) {
    let mut pos = [0, 0];

    for (d, x) in instructions {
        match (d.as_str(), x) {
            ("forward", x) => pos[0] += x,
            ("down", x) => pos[1] += x,
            ("up", x) => pos[1] -= x,
            _ => {}
        }
    }

    println!("Part 1: {}", pos[0] * pos[1]);
}

fn part2(instructions: &[(String, i32)]) {
    let mut pos = [0, 0, 0];

    for (d, x) in instructions {
        match (d.as_str(), x) {
            ("forward", x) => {
                pos[0] += x;
                pos[1] += pos[2] * x;
            }
            ("down", x) => pos[2] += x,
            ("up", x) => pos[2] -= x,
            _ => {}
        }
    }

    println!("Part 2: {}", pos[0] * pos[1]);
}