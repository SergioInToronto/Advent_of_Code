defmodule Day4 do
  def part1() do
    {world, bounds} = load()

    world
    |> Enum.filter(&has_roll?/1)
    |> Enum.filter(& fewer_than_four_neighbors?(&1, world, bounds))
    |> Enum.count()
    |> IO.inspect(label: "Rolls with fewer than 4 neighbours")
  end

  def load() do
    lines =
      "input.txt"
      |> File.read!()
      |> String.split()

    width = lines |> hd() |> String.length()
    height = length(lines)
    bounds = {width, height}
    world = to_map(lines)

    {world, bounds}
  end

  def to_map(lines) do
    lines
    |> Enum.with_index()
    |> Enum.reduce(%{}, fn {line, y}, acc ->
      line
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce(acc, fn {char, x}, acc2 ->
        has_roll = char == "@"
        Map.put(acc2, {x, y}, has_roll)
      end)
    end)
  end

  def has_roll?({{_x, _y}, value}), do: value

  def fewer_than_four_neighbors?({{x, y}, _value}, world, bounds) do
    valid_neighbour_coords(x, y, bounds)
    |> Enum.map(& Map.get(world, &1))
    |> Enum.filter(& &1)
    |> length()
    |> Kernel.<(4)
  end

  def valid_neighbour_coords(x, y, bounds) do
    {width, height} = bounds

    [
      {x - 1, y},
      {x + 1, y},
      {x, y - 1},
      {x, y + 1},
      {x - 1, y - 1},
      {x + 1, y - 1},
      {x - 1, y + 1},
      {x + 1, y + 1},
    ]
    |> Enum.filter(fn {nx, ny} ->
      nx >= 0 and ny >= 0 and nx < width and ny < height
    end)
  end


  def part2() do
    {world, bounds} = load()

    world
    |> remove_rolls_until_zero(bounds, 0)
    |> IO.inspect(label: "Total rolls recursively")
  end

  def remove_rolls_until_zero(world, bounds, count) do
    coords = coords_of_accessable_rolls(world, bounds)

    if coords == [] do
      count
    else
      new_world = Enum.reduce(coords, world, fn coord, acc ->
        Map.put(acc, coord, false)
      end)

      remove_rolls_until_zero(new_world, bounds, count + length(coords))
    end
  end

  def coords_of_accessable_rolls(world, bounds) do
    world
    |> Enum.filter(&has_roll?/1)
    |> Enum.filter(& fewer_than_four_neighbors?(&1, world, bounds))
    |> Enum.map(fn {{x, y}, _value} -> {x, y} end)
  end
end

Day4.part1()
Day4.part2()
