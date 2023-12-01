import java.nio.file.Files
import java.nio.file.Path

fun main() {
    val lines = Files.readAllLines(Path.of("src/main/resources/in.txt"))

    var sumP1 = 0
    var sumP2 = 0

    val pattern = Regex("(?=(\\d|one|two|three|four|five|six|seven|eight|nine))")

    for (line in lines) {
        val matches = pattern.findAll(line).map { it.groupValues[1] }.toList()

        val matchesP1 = matches.filter { it.toIntOrNull() != null }
        sumP1 += (matchesP1.first() + matchesP1.last()).toInt()

        val matchesP2 = matches.map {
            it.replace("one", "1")
                .replace("two", "2")
                .replace("three", "3")
                .replace("four", "4")
                .replace("five", "5")
                .replace("six", "6")
                .replace("seven", "7")
                .replace("eight", "8")
                .replace("nine", "9")
        }
        sumP2 += (matchesP2.first() + matchesP2.last()).toInt()
    }

    println("Part 1: $sumP1")
    println("Part 2: $sumP2")
}
