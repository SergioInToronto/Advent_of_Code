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
end

defmodule Day2part2 do
  def run do
    "input.txt"
    |> File.read!()
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&procecss_range/1)
    |> List.flatten()
    |> Enum.sum()
    |> IO.inspect(label: "Sum Part 2")
  end

  def procecss_range(range_str) do
    [min, max] = range_str |> String.split("-") |> Enum.map(&String.to_integer/1)
    IO.puts("Count: #{inspect(max - min)}")

    Enum.reduce(min..max, [], &keep_if_invalid/2)
  end

  def keep_if_invalid(num, acc) do
    digit_count = num |> Integer.to_string() |> String.length()
    if valid?(num, digit_count) do
      [num | acc]
    else
      acc
    end
  end

  def valid?(num, digit_count) do
    factors

    exponent = div(digit_count, 2)
    factor = 10 |> :math.pow(exponent) |> trunc()
    first_half = num |> div(factor)
    second_half = num |> rem(factor)

    first_half == second_half
  end

  def factors(1, _), do: [1]
  def factors(_, 1), do: [1]
  def factors(n, i) do
    if rem(n, i) == 0 do
      [ i | factors(n, i-1) ]
    else
      factors(n, i-1)
    end
  end

  def is_prime?(n) do
    factors(n, div(n, 2)) == [1]
  end
end


# Day2.part1()
# I'm still figuring out naming and don't care about consistency right now
Day2part2.run()
