defmodule Day11 do
  @device_connections_regex ~r/([[:alpha:]]{3}): (.*)/

  @step_limit 10_000

  def part1 do
    # "experiments.txt"
    device_connections =
      "input.txt"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&parse_device_connections/1)
      |> Enum.reduce(%{}, fn {node, neighbours}, acc -> Map.put(acc, node, neighbours) end)

    initial_stack = ["you"]
    initial_known_paths = MapSet.new([["you"]])
    # Sanity check - limit path length to 1000 steps
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

  def process(step, {[node | stack], known_paths}, device_connections) do
    relevant_paths =
      known_paths
      # paths where last node is `node`. Last is first for performance reasons
      |> Enum.filter(&(Enum.at(&1, 0) == node))

    neighbours = device_connections[node]

    case neighbours do
      nil when node == "out" ->
        dbg("Found exit path: #{inspect(relevant_paths)}")
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

  def append_nodes(items_to_add, stack) do
    # Reverse, prepend, and reverse again.
    # This tested twice as fast on a stack of 1000 adding 20 nodes
    # ...would be nice if the VM or compiler handled this so I didn't have to think about it...
    items_to_add
    |> Enum.reduce(Enum.reverse(stack), &[&1 | &2])
    |> Enum.reverse()
  end
end

Day11.part1()
