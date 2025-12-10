defmodule Day5 do
  def part1 do
    [section1, section2] = "input.txt" |> File.read!() |> String.split("\n\n")
    fresh_ingredients = parse_fresh_ingredients(section1)
    available_ingredients = parse_available_ingredients(section2)

    available_ingredients
      |> MapSet.intersection(fresh_ingredients)
      |> MapSet.size()
      |> IO.inspect(label: "Available fresh ingredients")
  end

  def parse_fresh_ingredients(text) do
    text
    |> String.split("\n", trim: true)
    |> IO.inspect()
    |> Enum.reduce(MapSet.new(), fn range, acc ->
      IO.inspect({range, acc})
      new_range = parse_range(range)

      MapSet.union(acc, new_range)
    end)
  end

  def parse_range(range) do
    [lower, upper] = range |> String.split("-") |> Enum.map(&String.to_integer/1)

    MapSet.new(lower..upper)
  end

  def parse_available_ingredients(text) do
    text
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> MapSet.new()
  end
end


Day5.part1()
