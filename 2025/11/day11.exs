defmodule Day11 do
  @device_connections_regex ~r/([[:alpha:]]{3}): (.*)/

  def part1 do
    device_connections =
      "experiments.txt"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&parse_device_connections/1)
      |> Enum.reduce(%{}, fn {node, neighbours}, acc -> Map.put(acc, node, neighbours) end)
      |> dbg(printable_limit: :infinity, limit: :infinity)

    # TODO: breadth-first search, adding paths to a MapSet.
    # Put whole path into MapSet
    # We can't ignore longer paths leading to a node, because that's still a valid path ??
    # Don't explore any paths that lead back to "you"


    # nodes_from_you = device_connections["you"]
    # nodes_from_you = Map.take(device_connections, ["you"]) |> dbg()

    # initial_stack = [nodes_from_you]
    initial_stack = ["you"]
    initial_known_paths = [["you"]]
    # Sanity check - limit path length to 1000 steps
    iter = 0..1_000
    Enum.reduce_while(iter, {initial_stack, initial_known_paths}, & process(&1, &2, device_connections))
  end

  def parse_device_connections(text) do
    [_, device, neighbours] = Regex.run(@device_connections_regex, text)
    neighbours = neighbours |> String.split(" ") |> Enum.map(&String.trim/1)

    dbg({device, neighbours})
  end

  def process(step, {[node | stack], known_paths}, device_connections) do
    relevant_paths = known_paths
    |> Enum.filter(& Enum.at(&1, -1) == node) # paths where last node is `node`

    neighbours = device_connections[node]

    dbg(step)
    # dbg(stack)
    dbg(known_paths)
    dbg(relevant_paths)
    # dbg(device_connections)
    dbg(node)
    dbg(neighbours)

    raise "WIP"
  end

  def append_nodes(items_to_add, stack) do
    # Reverse, prepend, and reverse again.
    # This tested twice as fast on a stack of 1000 adding 20 nodes
    # ...would be nice if the VM or compiler handled this so I didn't have to think about it...
    items_to_add
    |> Enum.reduce(Enum.reverse(stack), & [&1 | &2])
    |> Enum.reverse()
  end
end

Day11.part1()
