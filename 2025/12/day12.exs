defmodule Region do
  @enforce_keys [:width, :height]
  @allowed_keys [:width, :height, :shapes]
  @type t :: %__MODULE__{width: non_neg_integer, height: non_neg_integer, grid: nil, shapes: []}

  defstruct [:width, :height, :grid, shapes: []]

end

defmodule Day12 do
  # Hard-code my 6 shapes for this puzzle.
  # While I normally try to make everything dynamic, I feel a little
  # hard-coding is appropriate for day12 (the hardest puzzle)
  # maybe: consider using structs for each shape. Worth it? Maybe not.
  @shapes [
    %{
      # - #.#
      # - ###
      # - #.#
      shape: [true, false, true, true, true, true, true, false, true],
      # TODO: will bother using this optimization?
      flip: false,
      rotations: 2
    },
    %{
      # - ###
      # - ###
      # - #..
      shape: [true, true, true, true, true, true, true, false, false],
      flip: true,
      rotations: 4
    },
    %{
      # - ###
      # - .##
      # - ##.
      shape: [true, true, true, false, true, true, true, true, false],
      flip: true,
      rotations: 4
    },
    %{
      # - ###
      # - .##
      # - ..#
      shape: [true, true, true, false, true, true, false, false, true],
      flip: true,
      rotations: 4
    },
    %{
      # - ###
      # - ..#
      # - ###
      shape: [true, true, true, false, false, true, true, true, true],
      flip: false,
      rotations: 4
    },
    %{
      # - ##.
      # - .##
      # - ..#
      index: 5,
      shape: [true, true, false, false, true, true, false, false, true],
      flip: true,
      rotations: 4
    },
  ]

  @region_regex ~r/([0-9]{1,2})x([0-9]{1,2}): ([0-9 ]+)/

  def part1 do
    # "input.txt"
    "experiments.txt"
    |> File.read!()
    |> String.split("\n\n")
    |> Enum.at(-1)
    |> String.split("\n", trim: true)
    |> Enum.with_index(31)
    |> Enum.map(&can_fix_all_presents?/1)
    |> Enum.count(& &1)
    |> IO.inspect(label: "Regions that fit all presents")
  end

  def can_fix_all_presents?({entry, line_no}) do
    {width, height, required_presents} = parse_region(entry)

    initial_region = for x <- 0..(width - 1), y <- 0..(height - 1), do: false

    fit_shapes(initial_region)

    line = line_no |> Integer.to_string() |> String.pad_leading(4)
    IO.puts("#{line_no}: #{entry}  -->  #{inspect(initial_region)}")

    false
  end

  def parse_region(text) do
    [_, width, height, required_presents] = Regex.run(@region_regex, text)
    width = String.to_integer(width)
    height = String.to_integer(height)
    required_presents = required_presents |> String.split() |> Enum.map(&String.to_integer/1)

    {width, height, required_presents}
  end

  def new_region()

  # TODO: figure out recursive function signature

  def add_shape_to_region(region, shape) do
    # TODO: YOU ARE HERE kinda...
  end

end

Day12.part1()
