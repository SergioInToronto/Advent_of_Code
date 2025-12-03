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
    # |> elem(1)
    |> IO.inspect(label: "Password to open door")
    # 8847 is too high.
    # 6707 is too high.
    # 6546 is wrong :'(
    # 6165 is too low.
  end

  def spin_and_count(move, {pos, count}) do
    new_pos = pos + move
    full_rotations = new_pos |> div(100) |> abs()
    new_count = count + full_rotations

    fixed_new_pos = fix_pos(new_pos)

    # if count ends on zero, +1 count
    new_count = if fixed_new_pos == 0, do: new_count + 1, else: new_count

    {fixed_new_pos, new_count}
  end

  def fix_pos(pos) when pos > 100, do: fix_pos(pos - 100)
  def fix_pos(pos) when pos < 0, do: fix_pos(pos + 100)
  def fix_pos(100), do: 0
  def fix_pos(pos), do: pos

end

Main.run()
