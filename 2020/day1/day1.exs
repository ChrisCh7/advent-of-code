defmodule Day1 do
  def day1(n) do
    numbers = File.read!("in.txt")
      |> String.split("\r\n")
      |> Enum.map(&String.to_integer/1)

    if n == 3 do
      combinations = cartesian(numbers, numbers, numbers)
      IO.puts "Part 2:"
      get_product(combinations) |> IO.inspect
    else
      combinations = cartesian(numbers, numbers)
      IO.puts "Part 1:"
      get_product(combinations) |> IO.inspect
    end
  end

  def get_product(combinations) do
    combinations
    |> Enum.map(fn nr -> [nr, Enum.sum(nr)] end)
    |> Enum.find(fn nr -> Enum.at(nr, 1) == 2020 end)
    |> Enum.at(0)
    |> Enum.reduce(fn x, acc -> x * acc end)
  end

  def cartesian(a, b) do
    for x <- a, y <- b, do: [x, y]
  end

  def cartesian(a, b, c) do
    for x <- a, y <- b, z <- c, do: [x, y, z]
  end
end

Day1.day1(2)
Day1.day1(3)
