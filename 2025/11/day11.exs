defmodule Day11 do
  @device_connections_regex ~r/([[:alpha:]]{3}): (.*)/

  @step_limit 1_000_000
  @start_node_part1 "you"
  @start_node_part2 "svr"

  def part1 do
    # "experiments.txt"
    device_connections =
      "input.txt"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&parse_device_connections/1)
      |> Enum.reduce(%{}, fn {node, neighbours}, acc -> Map.put(acc, node, neighbours) end)

    initial_stack = [@start_node_part1]
    initial_known_paths = MapSet.new([[@start_node_part1]])
    # Sanity check - limit path length
    iter = 0..@step_limit

    iter
    |> Enum.reduce_while(
      {initial_stack, initial_known_paths},
      &process(&1, &2, device_connections)
    )
    |> Enum.filter(&(&1 |> hd() == "out"))
    # |> dbg()
    |> Enum.count()
    |> IO.inspect(label: "Exit path count")
  end

  def parse_device_connections(text) do
    [_, device, neighbours] = Regex.run(@device_connections_regex, text)
    neighbours = neighbours |> String.split(" ") |> Enum.map(&String.trim/1)

    {device, neighbours}
  end

  def process(_, {[], known_paths}, _), do: {:halt, known_paths}
  def process(@step_limit, _, _), do: {:halt, "Step limit exceeded!"}
  def process(_, {["out" | stack], known_paths}, _) do
    IO.write(".")

    {:cont, {stack, known_paths}}
  end

  def process(step, {[node | stack], known_paths}, device_connections) do
    relevant_paths =
      known_paths
      # paths where last node is `node`. Last is first for performance reasons
      |> Enum.filter(&(Enum.at(&1, 0) == node))

    neighbours = device_connections[node]

    case neighbours do
      nil when node == "out" ->
        # dbg("Found exit path: #{inspect(relevant_paths)}")
        IO.puts("Found exit path with #{step} steps")
        dbg(stack)
        if step > 5, do: known_paths |> Enum.filter(& &1 |> hd() == "out") |> IO.inspect(printable_limit: :infinity, limit: :infinity)
        if step > 500, do: raise "WIP"
        {:cont, {stack, known_paths}}

      nil ->
        dbg(node)
        raise "BUG: neighbours is nil"

      _ ->
        new_paths =
          for path <- relevant_paths,
              neighbour <- neighbours,
              neighbour not in path,
              do: [neighbour | path]

        new_stack = Enum.reduce(neighbours, stack, &[&1 | &2])
        new_known_paths = new_paths |> MapSet.new() |> MapSet.union(known_paths)

        {:cont, {new_stack, new_known_paths}}
    end
  end

  ####################################################

  def part2 do
    device_connections =
      "input.txt"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&parse_device_connections/1)
      |> Enum.reduce(%{}, fn {node, neighbours}, acc -> Map.put(acc, node, neighbours) end)

    initial_stack = [@start_node_part2]
    initial_known_paths = MapSet.new([[@start_node_part2]])
    # Sanity check - limit path length
    iter = 0..@step_limit

    iter
    |> Enum.reduce_while(
      {initial_stack, initial_known_paths},
      &process(&1, &2, device_connections)
    )
    |> Enum.filter(&(&1 |> hd() == "out"))
    |> Enum.filter(&("dac" in &1 and "fft" in &1))
    # |> dbg()
    |> Enum.count()
    |> IO.inspect(label: "Exit path count")
  end
end

# Day11.part1()
Day11.part2()
