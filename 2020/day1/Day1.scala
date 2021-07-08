package adventofcode.year2020

import scala.io.Source

object Day1 {
  def main(args: Array[String]): Unit = {
    val numbers = getNumbers
    part1(numbers)
    part2(numbers)
  }

  def getNumbers: Seq[Int] = {
    val source = Source.fromFile("src/main/resources/in.txt")
    val lines = try source.getLines.toList finally source.close()
    val numbers = lines.map(x => x.toInt)
    numbers
  }

  def part1(numbers: Seq[Int]): Unit = {
    for (nr <- numbers) {
      for (nr2 <- numbers) {
        if (nr + nr2 == 2020) {
          println(s"the numbers: $nr, $nr2")
          println(s"result: ${nr * nr2}")
          return
        }
      }
    }
  }

  def part2(numbers: Seq[Int]): Unit = {
    for (nr <- numbers) {
      for (nr2 <- numbers) {
        for (nr3 <- numbers) {
          if (nr + nr2 + nr3 == 2020) {
            println(s"the numbers: $nr, $nr2, $nr3")
            println(s"result: ${nr * nr2 * nr3}")
            return
          }
        }
      }
    }
  }
}
