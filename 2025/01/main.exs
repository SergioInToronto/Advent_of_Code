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
    |> Enum.reduce({0, @dial_start_position}, &handle_instruction/2)
    |> elem(0)
    |> IO.inspect(label: "Password to open door:")
  end

  def handle_instruction(instruction, {zero_acc, dial_pos}) do
    dbg({instruction, dial_pos})
    new_dial_pos = new_pos(dial_pos + instruction)
    new_zero_acc = zero_acc + zero_incr(new_dial_pos)

    {new_zero_acc, new_dial_pos}
  end

  def new_pos(value) when value < 0, do: new_pos(value + 100)
  def new_pos(value) when value > 0, do: rem(value, 100)
  def new_pos(value) when value == 0, do: 0

  def zero_incr(0), do: 1
  def zero_incr(_), do: 0
end

Main.run()
