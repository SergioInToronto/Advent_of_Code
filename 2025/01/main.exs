defmodule Main do
  @dial_start_position 50

  def run do
    "input.txt"
    |> File.read!()
    |> String.split()
    |> Enum.map(fn
      "R" <> x -> String.to_integer(x)
      "L" <> x -> String.to_integer(x) * -1
    end)
    |> Enum.reduce({@dial_start_position, 0}, &spin_and_count/2)
    |> elem(1)
    |> IO.inspect(label: "Password to open door")
  end

  def spin_and_count(move, {pos, count}) do
    move_without_full_rotations = rem(move, 100)
    pos_raw = (pos + move_without_full_rotations)
    {new_pos, passed_or_landed_on_zero_addr} = fix_pos(pos_raw)
    full_rotations = move |> div(100) |> abs()
    # Prevent double-counting the zero
    edge_case_fix_addr = if pos == 0 and move < 0, do: -1, else: 0
    new_count = count + full_rotations + passed_or_landed_on_zero_addr + edge_case_fix_addr

    {new_pos, new_count}
  end

  def fix_pos(0), do: {0, 1}
  def fix_pos(100), do: {0, 1}
  def fix_pos(x) when x > 100, do: {x - 100, 1}
  def fix_pos(x) when x < 0, do: {x + 100, 1}
  def fix_pos(x), do: {x, 0}
end

Main.run()
