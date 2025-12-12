defmodule Day6 do
  def part1 do
    "input.txt"
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.zip_reduce(0, &do_cephalopod_math/2)
    |> IO.inspect(label: "Sum of all answers")
  end

  def do_cephalopod_math([num1, num2, num3, num4, operator], acc) do
    numbers = Enum.map([num1, num2, num3, num4], &String.to_integer/1)
    answer = case operator do
      "+" -> Enum.sum(numbers)
      "*" -> Enum.product(numbers)
    end

    acc + answer
  end

  def part2() do
    "input.txt"
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> parse_numbers()
    |> Enum.zip_reduce(0, &do_cephalopod_math/2)
    |> IO.inspect(label: "Sum of all answers (part2)")
  end

  def parse_numbers([str1, str2, str3, str4, operator]) do
    # Cephalopod math is column oriented and read right-to-left. Oh boy...
    # Numbers are at most 4 digits

    # 1. assert length of number is < 5
    # 2. String.split() to get digits. Or maybe cast to int and use `div(num, 1000)` and ignore zeros
    # 3. assemble into 1 - 4 distinct values
    # 4. return array of numbers + operator
  end
end


Day6.part1()
Day6.part2()
