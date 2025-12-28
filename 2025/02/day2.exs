defmodule Day2 do
  def part1 do
    "input.txt"
    |> File.read!()
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&procecss_range/1)
    |> List.flatten()
    |> Enum.sum()
    |> IO.inspect(label: "Sum")
  end

  def procecss_range(range_str) do
    [min, max] = range_str |> String.split("-") |> Enum.map(&String.to_integer/1)
    IO.puts("Count: #{inspect(max - min)}")

    Enum.reduce(min..max, [], &keep_if_invalid/2)
  end

  def keep_if_invalid(num, acc) do
    digit_count = num |> Integer.to_string() |> String.length()

    if digit_count |> rem(2) == 0 and valid?(num, digit_count) do
      [num | acc]
    else
      acc
    end
  end

  def valid?(num, digit_count) do
    exponent = div(digit_count, 2)
    factor = 10 |> :math.pow(exponent) |> trunc()
    first_half = num |> div(factor)
    second_half = num |> rem(factor)

    first_half == second_half
  end

  def part2 do
    "input.txt"
    |> File.read!()
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&procecss_range_part2/1)
    |> List.flatten()
    |> Enum.sum()
    |> IO.inspect(label: "Sum Part 2")
    # 1067619439706031 is too high
    # 20077273032 is too high
    # 20077272987
  end

  def procecss_range_part2(range_str) do
    [min, max] = range_str |> String.split("-") |> Enum.map(&String.to_integer/1)
    IO.inspect(min..max)
    IO.puts("\tCount: #{inspect(max - min)}")

    Enum.reduce(min..max, [], &keep_if_invalid_part2/2)
  end

  def keep_if_invalid_part2(num, acc) do
    num_str = Integer.to_string(num)
    digit_count = String.length(num_str)

    if part2_invalid?(num_str, digit_count) do
      [num | acc]
    else
      acc
    end
  end

  # single-digit numbers do not count as repeating patterns
  def part2_invalid?(_, 1), do: false
  def part2_invalid?(num_str, digit_count) do
    max_pattern_length = max(1, div(digit_count, 2))
    # Check for patterns of 1 digit up to half the length of the number (eg: length 5 -> max 2-digit patterns)
    1..max_pattern_length
    |> Enum.find(false, fn length ->
      repeating_groups_of_n(num_str, length)
    end)
  end

  def repeating_groups_of_n(num_str, length) do
    pattern = String.slice(num_str, 0, length) |> String.graphemes()
    num_str |> String.graphemes() |> Enum.chunk_every(length, length, []) |> Enum.all?(&(&1 == pattern))
  end
end

# Day2.part1()
Day2.part2()
