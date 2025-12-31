defmodule Day9 do
  def part1 do
    coords =
      "input.txt"
      # "experiments"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&parse_coordinates/1)

    pairs = for x <- coords, y <- coords, x != y, do: {x, y}

    pairs
    |> Enum.map(&calculate_area/1)
    # |> dbg(charlists: :as_lists, printable_limit: :infinity, limit: :infinity)
    |> Enum.max()
    |> IO.inspect(label: "Part 1: largest area")
  end

  def parse_coordinates(text) do
    text
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
  end

  def calculate_area({[x1, y1], [x2, y2]}) do
    # +1 to include both start & end points
    x = abs(x1 - x2) + 1
    y = abs(y1 - y2) + 1
    x * y

    # {x * y, [x1, y1], [x2, y2]}
  end
end

Day9.part1()
