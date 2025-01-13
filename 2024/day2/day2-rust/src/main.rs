use std::fs;

fn main() {
    let reports: Vec<Vec<i32>> = fs::read_to_string("../in.txt")
        .unwrap()
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|n| n.parse().unwrap())
                .collect()
        })
        .collect();

    println!(
        "Part 1: {}",
        reports.iter().filter(|&report| is_safe(report)).count()
    );

    println!(
        "Part 2: {}",
        reports.iter().filter(|&report| is_safe_p2(report)).count()
    );
}

fn is_safe(report: &[i32]) -> bool {
    levels_all_increasing_or_all_decreasing(report)
        && any_two_adjacent_levels_differ_by_at_least_one_and_at_most_three(report)
}

fn levels_all_increasing_or_all_decreasing(report: &[i32]) -> bool {
    let mut sorted_report = report.to_vec();
    sorted_report.sort();
    let mut sorted_report_reverse = report.to_vec();
    sorted_report_reverse.sort();
    sorted_report_reverse.reverse();
    report == sorted_report || report == sorted_report_reverse
}

fn any_two_adjacent_levels_differ_by_at_least_one_and_at_most_three(report: &[i32]) -> bool {
    for i in 0..report.len() - 1 {
        let diff = (report[i] - report[i + 1]).abs();
        if !(diff >= 1 && diff <= 3) {
            return false;
        }
    }

    true
}

fn is_safe_p2(report: &[i32]) -> bool {
    if is_safe(report) {
        return true;
    }

    for i in 0..report.len() {
        let report_with_a_level_removed = [report[..i].to_vec(), report[i + 1..].to_vec()].concat();
        if is_safe(&report_with_a_level_removed) {
            return true;
        }
    }

    false
}
