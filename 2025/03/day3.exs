defmodule Day3 do
  def part1 do
    "input.txt"
    |> File.read!()
    |> String.split()
    |> Enum.map(&find_max_joltage/1)
    |> Enum.sum()
    |> IO.inspect(label: "Total Joltage")

    # 16791 is too low
  end

  def find_max_joltage(battery_bank) do
    digits = battery_bank |> String.graphemes() |> Enum.map(&String.to_integer/1)
    # max_first = digits |> Enum.slice(0..-2) |> Enum.max()
    {first_digit, index} =
      digits |> Enum.slice(0..-2//1) |> Enum.with_index() |> Enum.max_by(&elem(&1, 0))

    sceond_digit = digits |> Enum.slice((index + 1)..-1//1) |> Enum.max()

    String.to_integer("#{first_digit}#{sceond_digit}") |> dbg()
  end

  ################################################

  def part2() do
    "input.txt"
    |> File.read!()
    |> String.split()
    |> Enum.map(&find_max_joltage_part2/1)

    # |> Enum.with_index(1)
    # |> IO.inspect(printable_limit: :infinity, limit: :infinity)

    |> Enum.sum()
    |> IO.inspect(label: "Total Joltage part2")
    # 168651765173330 is too high
  end

  def find_max_joltage_part2(battery_bank) do
    digits = String.length(battery_bank)

    (digits - 11)..(digits)
    |> Enum.reduce({0, ""}, &accumulate_largest_joltage(&1, &2, battery_bank))
    |> elem(1)
    |> String.to_integer()
    # |> IO.inspect()
  end

  def accumulate_largest_joltage(last_col, {first_col, acc}, battery_bank) do
    dbg({first_col, last_col})
    search_length = last_col - first_col
    digits_in_consideration = battery_bank |> String.slice(first_col, search_length) |> String.graphemes()
    next_digit = Enum.max(digits_in_consideration)
    col = (digits_in_consideration |> Enum.find_index(& &1 == next_digit)) + first_col

    {col + 1, acc <> next_digit}
  end
end

# Day3.part1()
Day3.part2()
