defmodule Day10 do
  @machine_regex ~r/^\[(?<lights>.*)\] (?<buttons>.*) {(?<joltage>.*)}$/

  def part1 do
    machines = load_machines()
    buttons_to_start_machines = Enum.map(machines, &find_buttons_to_start_machine/1)

    buttons_to_start_machines
    |> Enum.with_index()
    |> Enum.each(fn {result, index} ->
      btn_count =
        case result do
          :inf -> "--"
          result -> length(result) |> Integer.to_string() |> String.pad_trailing(2)
        end

      IO.puts("Machine #{index + 1} requires #{btn_count} buttons: #{inspect(result)}")
    end)

    buttons_to_start_machines
    |> Enum.map(&Enum.count/1)
    |> Enum.sum()
    |> IO.inspect(label: "Total button presses to start all machines")
  end

  def load_machines() do
    "input.txt" |> File.read!() |> String.split("\n", trim: true) |> Enum.map(&parse_machine/1)
  end

  def parse_machine(text) do
    [_, lights_str, buttons_str, joltage_str] = Regex.run(@machine_regex, text)

    desired_lights =
      lights_str
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce([], &light_index_if_desired/2)

    buttons = buttons_str |> String.split() |> Enum.map(&parse_button/1)
    joltage_requirements = joltage_str |> String.split(",") |> Enum.map(&String.to_integer/1)

    {desired_lights, buttons, joltage_requirements}
  end

  def light_index_if_desired({".", _index}, acc), do: acc
  def light_index_if_desired({"#", index}, acc), do: acc ++ [index]

  def parse_button(text) do
    text
    |> String.replace(["(", ")"], "")
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
  end

  def find_buttons_to_start_machine(machine) do
    {desired_lights, buttons, _joltage_requirements} = machine

    buttons
    # Quick optimization: ~25% of machines require only 1 button press
    |> Enum.find(fn btn_lights -> btn_lights == desired_lights end)
    |> case do
      nil -> do_find_buttons_to_start_machine(desired_lights, buttons)
      btn_lights -> [btn_lights]
    end
  end

  def do_find_buttons_to_start_machine(desired_lights, buttons) do
    # Skip n=1 because it's already handled

    # Note: max button count is 13
    group_sizes = 2..length(buttons)

    button_presses =
      Enum.find_value(group_sizes, fn group_size ->
        buttons
        |> combo_and_lights(group_size)
        |> Enum.find(fn {_button_presses, lights} -> lights == desired_lights end)
        |> case do
          nil -> false
          {button_presses, _lights} -> button_presses
        end

        # |> dbg(printable_limit: :infinity, limit: :infinity)
      end)

    if is_nil(button_presses), do: raise "TODO"

    button_presses
  end

  def combo_and_lights(buttons, group_size) do
    button_press_combinations = combinations(group_size, buttons) # |> dbg()
    resulting_lights = button_press_combinations |> Enum.map(&determine_lights/1)

    Enum.zip(button_press_combinations, resulting_lights)
  end

  def combinations(0, _), do: [[]]
  def combinations(_, []), do: []

  def combinations(size, [head | tail]) do
    for(elem <- combinations(size - 1, tail), do: [head | elem]) ++ combinations(size, tail)
  end

  def determine_lights(lights) do
    # remove lights which are triggered an even number of times (they'd be turned off again)
    # then sort and de-dup

    lights = List.flatten(lights)

    lights
    |> Enum.filter(fn light -> rem(Enum.count(lights, &(&1 == light)), 2) == 1 end)
    |> Enum.sort()
    |> MapSet.new()
    |> MapSet.to_list()
  end
end

Day10.part1()
