import java.nio.file.Files
import java.nio.file.Path

fun main() {
    val lines = Files.readAllLines(Path.of("src/main/resources/in.txt"))
    val rows = lines[0].length
    part1(lines, rows)
    part2(lines, rows)
}

fun part1(lines: List<String>, rows: Int) {
    val zeros = IntArray(rows)
    val ones = IntArray(rows)

    for (line in lines) {
        line.forEachIndexed { i, digit ->
            if (digit.digitToInt() == 0) {
                zeros[i] += 1
            } else {
                ones[i] += 1
            }
        }
    }

    var gammaRate = ""

    for (pos in 0 until rows) {
        if (zeros[pos] > ones[pos]) {
            gammaRate += "0"
        } else {
            gammaRate += "1"
        }
    }

    val gammaRateDecimal = gammaRate.toInt(2)

    val epsilonRate = gammaRate.map { if (it == '0') '1' else '0' }.joinToString("")

    val epsilonRateDecimal = epsilonRate.toInt(2)

    println("Part 1: ${gammaRateDecimal * epsilonRateDecimal}")
}

enum class BitCriteria {
    MOST, LEAST
}

fun part2(lines: List<String>, rows: Int) {
    var nrs = lines

    for (pos in 0 until rows) {
        nrs = filterNrs(nrs, pos, BitCriteria.MOST)
        if (nrs.size == 1) {
            break
        }
    }

    val oxygenGeneratorRatingDecimal = nrs[0].toInt(2)

    nrs = lines

    for (pos in 0 until rows) {
        nrs = filterNrs(nrs, pos, BitCriteria.LEAST)
        if (nrs.size == 1) {
            break
        }
    }

    val co2ScrubberRatingDecimal = nrs[0].toInt(2)

    println("Part 2: ${oxygenGeneratorRatingDecimal * co2ScrubberRatingDecimal}")
}

fun getCommonBit(nrs: List<String>, pos: Int, bitCriteria: BitCriteria): Int {
    var zeros = 0
    var ones = 0

    for (nr in nrs) {
        if (nr[pos].digitToInt() == 0) {
            zeros += 1
        } else {
            ones += 1
        }
    }

    return when {
        zeros == ones -> if (bitCriteria == BitCriteria.MOST) 1 else 0
        zeros > ones -> if (bitCriteria == BitCriteria.MOST) 0 else 1
        else -> if (bitCriteria == BitCriteria.MOST) 1 else 0
    }
}

fun filterNrs(nrs: List<String>, pos: Int, bitCriteria: BitCriteria): List<String> {
    val bit = getCommonBit(nrs, pos, bitCriteria)

    return when (bit) {
        1 -> nrs.filter { it[pos] == '1' }
        else -> nrs.filter { it[pos] == '0' }
    }
}
