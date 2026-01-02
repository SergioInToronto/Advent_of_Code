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
  end

  ###########################################################

  def part2 do
    # "input.txt"
    coords =
      "experiments"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&parse_coordinates/1)
      |> draw_and_save()

    # pairs = for x <- coords, y <- coords, x != y, do: {x, y}
  end

  def draw_and_save(coords) do
    file = File.open!("display.txt", [:write])

    # for x <- 0..100_000, y <- 0..100_000 do
    for x <- 1..14, y <- 1..14 do
      if rem(x, 2000) == 1 and y == 1, do: IO.puts("Line #{x}...")
      if y == 1, do: IO.write(file, "\n")

      if [x, y] in coords do
        IO.inspect([x,y], charlists: :as_lists)
        IO.write(file, "#")
      else
        IO.write(file, ".")
      end
    end
  end
end

# Day9.part1()
Day9.part2()
