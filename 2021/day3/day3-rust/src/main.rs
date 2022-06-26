use std::fs;

fn main() {
    let lines = fs::read_to_string("../in.txt")
        .expect("Error reading file")
        .lines()
        .map(|line| line.to_string())
        .collect::<Vec<_>>();

    let rows = lines[0].chars().count();

    part1(&lines, rows);
    part2(&lines, rows);
}

fn part1(lines: &Vec<String>, rows: usize) {
    let mut zeros = vec![0; rows];
    let mut ones = vec![0; rows];

    for line in lines {
        for (i, digit) in line.chars().enumerate() {
            if digit.to_digit(10).unwrap() == 0 {
                zeros[i] += 1;
            } else {
                ones[i] += 1;
            }
        }
    }

    let mut gamma_rate = "".to_string();

    for pos in 0..rows {
        if zeros[pos] > ones[pos] {
            gamma_rate += "0";
        } else {
            gamma_rate += "1";
        }
    }

    let gamma_rate_decimal = isize::from_str_radix(&gamma_rate, 2).unwrap();

    let epsilon_rate = gamma_rate.chars().map(|c| match c {
        '1' => '0',
        '0' => '1',
        _ => panic!("Invalid character found in binary string")
    }).collect::<String>();

    let epsilon_rate_decimal = isize::from_str_radix(&epsilon_rate, 2).unwrap();

    println!("Part 1: {}", gamma_rate_decimal * epsilon_rate_decimal);
}

fn part2(lines: &Vec<String>, rows: usize) {
    let mut nrs = lines.to_vec();

    for pos in 0..rows {
        nrs = filter_nrs(&nrs, pos, BitCriteria::MOST);
        if nrs.len() == 1 {
            break;
        }
    }

    let oxygen_generator_rating_decimal = isize::from_str_radix(&nrs[0], 2).unwrap();

    nrs = lines.to_vec();

    for pos in 0..rows {
        nrs = filter_nrs(&nrs, pos, BitCriteria::LEAST);
        if nrs.len() == 1 {
            break;
        }
    }

    let co2_scrubber_rating_decimal = isize::from_str_radix(&nrs[0], 2).unwrap();

    println!("Part 2: {}", oxygen_generator_rating_decimal * co2_scrubber_rating_decimal);
}

enum BitCriteria {
    MOST = 1,
    LEAST = 2,
}

fn get_common_bit(nrs: &Vec<String>, pos: usize, bit_criteria: BitCriteria) -> u8 {
    let mut zeros = 0;
    let mut ones = 0;

    for nr in nrs {
        if nr.chars().nth(pos).unwrap().to_digit(10).unwrap() == 0 {
            zeros += 1;
        } else {
            ones += 1;
        }
    }

    if zeros == ones {
        if matches!(bit_criteria, BitCriteria::MOST) { 1 } else { 0 }
    } else if zeros > ones {
        if matches!(bit_criteria, BitCriteria::MOST) { 0 } else { 1 }
    } else {
        if matches!(bit_criteria, BitCriteria::MOST) { 1 } else { 0 }
    }
}

fn filter_nrs(nrs: &Vec<String>, pos: usize, bit_criteria: BitCriteria) -> Vec<String> {
    let bit = get_common_bit(nrs, pos, bit_criteria);

    nrs.iter().filter(|&nr| nr.chars().nth(pos).unwrap() == char::from_digit(bit as u32, 10).unwrap())
        .map(|s| s.to_owned())
        .collect::<Vec<String>>()
}