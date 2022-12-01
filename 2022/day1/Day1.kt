import java.nio.file.Files
import java.nio.file.Path

fun main() = Files.readString(Path.of("src/main/resources/in.txt"))
    .split("\r\n\r\n")
    .map { it.split("\r\n").map(Integer::parseInt) }
    .map { it.sum() }
    .sortedDescending()
    .take(3)
    .let {
        println("Part 1: ${it.first()}")
        println("Part 2: ${it.sum()}")
    }
