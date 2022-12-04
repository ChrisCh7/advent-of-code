import java.nio.file.Files
import java.nio.file.Path

fun main() = Files.readAllLines(Path.of("src/main/resources/in.txt"))
    .map { pair ->
        pair.split(",")
            .map { range ->
                range.split("-")
                    .map { it.toInt() }
            }
    }
    .let {
        println("Part 1: ${part1(it)}")
        println("Part 2: ${part2(it)}")
    }

fun part1(pairs: List<List<List<Int>>>): Int {
    return pairs.count { rangesOverlap(it) { range1, range2 -> range1.all { it in range2 } } }
}

fun part2(pairs: List<List<List<Int>>>): Int {
    return pairs.count { rangesOverlap(it) { range1, range2 -> range1.any { it in range2 } } }
}

fun rangesOverlap(pair: List<List<Int>>, how: (IntRange, IntRange) -> Boolean): Boolean {
    val range1 = pair[0][0]..pair[0][1]
    val range2 = pair[1][0]..pair[1][1]

    return how(range1, range2) || how(range2, range1)
}
