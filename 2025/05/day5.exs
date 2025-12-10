defmodule Day5 do
  def part1 do
    [section1, section2] = "input.txt" |> File.read!() |> String.split("\n\n")
    fresh_ranges = parse_fresh_ranges(section1)
    available_ingredients = parse_available_ingredients(section2)

    available_ingredients
      |> Enum.map(&fresh?(&1, fresh_ranges))
      |> Enum.filter(& &1)
      |> length()
      |> IO.inspect(label: "Available fresh ingredients")
  end

  def parse_fresh_ranges(text) do
    text
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_range/1)
  end

  def parse_range(range) do
    # destructure to assert the shape is correct
    [lower, upper] = range |> String.split("-") |> Enum.map(&String.to_integer/1)

    {lower, upper}
  end

  def parse_available_ingredients(text) do
    text
    |> String.split()
    |> Enum.map(&String.to_integer/1)
    |> MapSet.new()
  end

  def fresh?(ingredient_id, fresh_ranges) do
    Enum.any?(fresh_ranges, fn {lower, upper} ->
      lower <= ingredient_id and ingredient_id <= upper
    end) |> IO.inspect(label: "#{ingredient_id} fresh")
  end
end


Day5.part1()
