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


  def part2 do
    [section1, _] = "input.txt" |> File.read!() |> String.split("\n\n")
    section1
    |> parse_fresh_ranges()
    |> sort_by_lower_bound()
    |> merge_ranges()
    |> total_count_in_ranges()
    |> IO.inspect(label: "Total fresh ingredients count")
    # 338189277144383 is too low :(
  end

  def sort_by_lower_bound(ranges) do
    # Enum.sort(ranges, & elem(&1, 0))
    Enum.sort_by(ranges, & elem(&1, 0))
  end

  def merge_ranges(ranges) do
    Enum.reduce(ranges, [], &maybe_merge_range/2)
  end

  def maybe_merge_range(range, []), do: [range]
  def maybe_merge_range({lower, upper}, acc) do
    {prev_lower, prev_upper} = acc |> Enum.at(-1)
    cond do
      lower <= prev_upper and upper > prev_upper ->
        # increase existing upper bounds
        List.replace_at(acc, -1, {prev_lower, upper})

      lower <= prev_upper and upper <= prev_upper ->
        # range is entirely within previous. ignore
        acc

      lower > prev_upper ->
        # new non-overlapping range
        acc ++ [{lower, upper}]

      true ->
        dbg([{lower, upper}, {prev_lower, prev_upper}])
        raise "This is impossible"
    end
  end

  def total_count_in_ranges(non_overlapping_ranges) do
    Enum.reduce(non_overlapping_ranges, 0, fn {lower, upper}, acc ->
      acc + (upper - lower + 1)
    end)
  end
end


Day5.part1()
Day5.part2()
