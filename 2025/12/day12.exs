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
      # TODO: need this?
      index: 0,
      shape: [true, false, true, true, true, true, true, false, true],
      # TODO: will bother using this optimization?
      flip: false,
      rotations: 2
    },
    %{
      # - ###
      # - ###
      # - #..
      index: 1,
      shape: [true, true, true, true, true, true, true, false, false],
      flip: true,
      rotations: 4
    },
    %{
      # - ###
      # - .##
      # - ##.
      index: 2,
      shape: [true, true, true, false, true, true, true, true, false],
      flip: true,
      rotations: 4
    },
    %{
      # - ###
      # - .##
      # - ..#
      index: 3,
      shape: [true, true, true, false, true, true, false, false, true],
      flip: true,
      rotations: 4
    },
    %{
      # - ###
      # - ..#
      # - ###
      index: 4,
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

  def part1 do
    # "input.txt"
    "experiments.txt"
    |> File.read!()
    |> String.split("\n\n")
    |> Enum.at(-1)
    |> String.split("\n", trim: true)
    |> Enum.with_index(31)
    |> Enum.map(&can_fix_all_presents?/1)
    |> dbg()
  end

  def can_fix_all_presents?({entry, line_no}) do
    # TODO: YOU ARE HERE

    false
  end

end

Day12.part1()
