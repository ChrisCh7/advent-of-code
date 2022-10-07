import java.nio.file.Files
import java.nio.file.Path

fun main() {
    val depths = Files.readAllLines(Path.of("src/main/resources/in.txt")).map(Integer::parseInt)
    part1(depths)
    part2(depths)
}

fun part1(depths: List<Int>) {
    var nrIncreases = 0

    for (n in 1 until depths.size) {
        if (depths[n] > depths[n - 1]) {
            nrIncreases += 1
        }
    }

    println("Part 1: $nrIncreases")
}

fun part2(depths: List<Int>) {
    var nrIncreases = 0
    var prevSum = 0

    for (n in 0 until depths.size - 2) {
        if (prevSum == 0) {
            prevSum = depths[n] + depths[n + 1] + depths[n + 2]
            continue
        }

        val currentSum = depths[n] + depths[n + 1] + depths[n + 2]

        if (currentSum > prevSum) {
            nrIncreases += 1
        }

        prevSum = currentSum
    }

    println("Part 2: $nrIncreases")
}
