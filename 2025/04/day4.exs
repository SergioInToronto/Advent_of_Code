defmodule Day4.Part1 do
  def run do
    lines =
      "input.txt"
      |> File.read!()
      |> String.split()

    width = lines |> hd() |> String.length()
    height = length(lines)
    bounds = {width, height}

    world = load_world(lines)

    world
    |> Enum.filter(fn {{_x, _y}, value} -> value end)
    |> Enum.filter(& fewer_than_four_neighbors?(&1, world, bounds))
    |> Enum.count()
    |> IO.inspect(label: "Rolls with fewer than 4 neighbours")
  end

  def load_world(lines) do
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


end

Day4.Part1.run()
