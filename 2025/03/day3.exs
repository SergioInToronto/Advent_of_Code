defmodule Day3.Part1 do
  def run do
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
    {first_digit, index} = digits |> Enum.slice(0..-2//1) |> Enum.with_index() |> Enum.max_by(& elem(&1, 0))
    sceond_digit = digits |> Enum.slice((index + 1)..-1//1) |> Enum.max()

    String.to_integer("#{first_digit}#{sceond_digit}") |> dbg()
  end
end

Day3.Part1.run()
