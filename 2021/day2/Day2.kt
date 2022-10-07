import java.nio.file.Files
import java.nio.file.Path

fun main() {
    val lines = Files.readAllLines(Path.of("src/main/resources/in.txt"))

    val instructions = lines.map { line ->
        line.split(Regex("\\s+")).let {
            Pair(it[0], Integer.parseInt(it[1]))
        }
    }

    part1(instructions)
    part2(instructions)
}

fun part1(instructions: List<Pair<String, Int>>) {
    val pos = intArrayOf(0, 0)

    instructions.forEach { instr ->
        when (instr.first) {
            "forward" -> pos[0] += instr.second
            "down" -> pos[1] += instr.second
            "up" -> pos[1] -= instr.second
        }
    }

    println("Part 1: ${pos[0] * pos[1]}")
}

fun part2(instructions: List<Pair<String, Int>>) {
    val pos = intArrayOf(0, 0, 0)

    instructions.forEach { instr ->
        when (instr.first) {
            "forward" -> {
                pos[0] += instr.second
                pos[1] += pos[2] * instr.second
            }

            "down" -> pos[2] += instr.second
            "up" -> pos[2] -= instr.second
        }
    }

    println("Part 2: ${pos[0] * pos[1]}")
}
