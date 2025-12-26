defmodule Day7 do
  def part1 do
    input = File.read!("input.txt")

    input
    |> String.graphemes()
    |> Enum.count(&(&1 == "^"))
    |> IO.inspect(label: "Total splitters")

    [first_line | lines] = input |> String.split("\n", trim: true)

    source_beam_col = first_line |> String.graphemes() |> Enum.find_index(&(&1 == "S"))

    lines
    |> count_splitting_tachyon_beams(source_beam_col)
    |> IO.inspect(label: "Tachyon beam splits")
  end

  def count_splitting_tachyon_beams(lines, source_beam_col) do
    starting_beams = [source_beam_col]
    starting_split_count = 0

    lines
    # Start at 2 because we handled the first line already
    |> Enum.with_index(2)
    |> Enum.reduce({starting_beams, starting_split_count}, fn {line, line_no}, {beams, count} ->
      splitter_cols =
        line
        |> String.graphemes()
        |> Enum.with_index()
        |> Enum.filter(fn {char, _col} -> char == "^" end)
        |> Enum.map(fn {_char, col} -> col end)

      touched_splitter_cols = splitter_cols |> Enum.filter(fn val -> val in beams end)

      if length(touched_splitter_cols) != length(splitter_cols) do
        unused_count = length(splitter_cols) - length(touched_splitter_cols)
        IO.puts("#{unused_count} untouched splitter(s) on line #{line_no}")
      end

      new_beams =
        beams
        |> turn_off_split_beams(touched_splitter_cols)
        |> turn_on_beams_after_split(touched_splitter_cols)

      {new_beams, count + length(touched_splitter_cols)}
    end)
    |> elem(1)
  end

  def turn_off_split_beams(beams, splitter_cols) do
    beams |> Enum.filter(&(&1 not in splitter_cols))
  end

  def turn_on_beams_after_split(beams, splitter_cols) do
    enable_for_cols = Enum.flat_map(splitter_cols, fn col -> [col - 1, col + 1] end)

    beams ++ enable_for_cols
  end

  #############################################################################

  def part2() do
    [first_line | lines] = File.read!("input.txt") |> String.split("\n", trim: true)
    source_beam_col = first_line |> String.graphemes() |> Enum.find_index(&(&1 == "S"))

    lines
    |> count_tachyon_beam_paths(source_beam_col)
    |> IO.inspect(label: "Tachyon beam possible paths (part2)")
  end

  def count_tachyon_beam_paths(lines, source_beam_col) do
    starting_beam_cols = MapSet.new([source_beam_col])
    starting_path_count = 1

    lines
    # Start at 2 because we handled the first line already
    |> Enum.with_index(2)
    |> Enum.reduce({starting_beam_cols, starting_path_count}, fn {line, line_no}, {beams, path_count} ->
      splitter_cols =
        line
        |> String.graphemes()
        |> Enum.with_index()
        |> Enum.filter(fn {char, _col} -> char == "^" end)
        |> Enum.map(fn {_char, col} -> col end)

      if splitter_cols == [] do
        # no splitters on this line
        {beams, path_count}
      else
        touched_splitter_cols = splitter_cols |> Enum.filter(fn val -> val in beams end)

        # new_beam_cols = turn_on_beams_after_split(beams |> MapSet.to_list(), touched_splitter_cols) |> MapSet.new()
        new_beam_cols = touched_splitter_cols |> Enum.flat_map(fn col -> [col - 1, col + 1] end) |> MapSet.new()
        disabled_beam_cols = beams |> Enum.filter(&(&1 in splitter_cols)) |> MapSet.new()
        merged_paths_count = new_beam_cols |> MapSet.intersection(beams) |> MapSet.size()

        resulting_beams = beams |> MapSet.difference(disabled_beam_cols) |> MapSet.union(new_beam_cols)
        new_path_count = path_count + (2 ** length(touched_splitter_cols)) - MapSet.size(disabled_beam_cols)
        new_path_count = if merged_paths_count != 0, do: new_path_count - (2 ** merged_paths_count), else: new_path_count

        IO.puts("Line #{line_no} beams: #{inspect(resulting_beams)}")
        IO.puts("\tNEW: #{inspect(new_beam_cols)}\n\tDISABLED: #{inspect(disabled_beam_cols)}")
        IO.puts("\t#{merged_paths_count} merge(s)")
        if length(touched_splitter_cols) != length(splitter_cols) do
          unused_count = length(splitter_cols) - length(touched_splitter_cols)
          IO.puts("\t#{unused_count} untouched splitter(s) on line #{line_no}")
        end
        IO.puts("\tPATHS: #{new_path_count}")

        if line_no == 9, do: raise "DEBUGGING"

        {resulting_beams, new_path_count}
      end
    end)
    |> elem(1)

    # 1
    # 2
    # 4
    # 10
    # 16 (some prev beams aren't split)
    # 22 (some prev beams aren't split)
    # 34 (some prev beams aren't split, some previously unsplit beams are split here)
    # line 15 splits beams from line 13 and also line 9. Two possible input paths!

    # for each line:
    # 1. Find splitters. Ignore unused (same as before)
  end
end

# Day7.part1()
Day7.part2()
