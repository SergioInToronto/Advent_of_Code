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
    col_count = String.length(Enum.at(lines, 0))
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
end

Day7.part1()
