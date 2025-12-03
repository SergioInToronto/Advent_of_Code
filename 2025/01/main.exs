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
    |> Enum.reduce({@dial_start_position, 0}, &handle_instruction/2)
    # |> elem(1)
    |> IO.inspect(label: "Password to open door")
    # 8847 is too high.
    # 6707 is too high.
    # 6165 is too low.
  end

  def handle_instruction(instruction, {dial_pos, zero_acc}) do
    # {new_dial_pos, zero_passes} = Enum.reduce(instruction, {dial_pos, 0}, &spin_and_count/2)
    {new_dial_pos, zero_passes} = spin_and_count(instruction, {dial_pos, 0})

    # dbg("#{dial_pos} -- #{instruction} --> #{new_dial_pos}.  Passes: #{zero_passes}")
    # if instruction == 11, do: raise "DEBUGGING"

    {new_dial_pos, zero_acc + zero_passes}
  end

  def spin_and_count(0, {0, count}), do: {0, count+1}

  def spin_and_count(move, {pos, count}) when move > 100 or move < -100 do
    zero_passes = div(move, 100)

    spin_and_count(move - (100 * zero_passes), {pos, count + abs(zero_passes)})
  end

  def spin_and_count(move, {pos, count}) do
    new_pos = pos + move
    new_count = if passed_zero?(pos, new_pos), do: count + 1, else: count

    {cleanup_pos(new_pos), new_count}
  end

  # don't double-count movements FROM zero
  def passed_zero?(0, _to), do: false
  def passed_zero?(_from, to) when to > 100 or to < -100, do: true
  # position always starts positive. If negative, it must have passed zero.
  def passed_zero?(_from, to) when to < 0, do: true
  def passed_zero?(_from, 100), do: true
  def passed_zero?(_from, _to), do: false

  def cleanup_pos(pos) when pos > 100, do: pos - 100
  def cleanup_pos(pos) when pos < 0, do: pos + 100
  def cleanup_pos(100), do: 0
  def cleanup_pos(pos), do: pos

end

Main.run()
