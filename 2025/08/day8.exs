defmodule Day8 do
  def part1 do
    junction_boxes =
      File.read!("input.txt")
      |> String.split("\n", trim: true)
      |> Enum.map(&String.split(&1, ","))
      |> Enum.map(fn parts -> Enum.map(parts, &String.to_integer/1) end)
      |> Enum.map(&List.to_tuple/1)

    IO.inspect("Computing 1000 * 999 neighbour distances...")

    nearest_box_pairs =
      junction_boxes
      |> Enum.flat_map(fn box ->
        junction_boxes
        |> Enum.reject(&(&1 == box))
        |> Enum.map(fn neighbour ->
          distance = compute_distance(box, neighbour)
          {distance, MapSet.new([box, neighbour])}
        end)
      end)
      # uniq_by to remove duplicates in different order, like {A, B} and {B, A}
      |> Enum.uniq_by(&elem(&1, 1))
      |> Enum.sort_by(&elem(&1, 0))
      |> Enum.slice(0..999)
      |> IO.inspect(printable_limit: :infinity, limit: :infinity)
      |> Enum.map(fn {_distance, pair} -> MapSet.to_list(pair) end)

    circuits = connect_all_junction_boxes(nearest_box_pairs)

    circuits
    |> Enum.map(&MapSet.size(&1))
    |> Enum.sort()
    |> Enum.reverse()
    |> Enum.slice(0..2)
    |> Enum.product()
    |> dbg(printable_limit: :infinity, limit: :infinity)
    |> IO.inspect(label: "Result of part1")

    # 480 is too low (10 * 8 * 6)
    # 2366 is too low (14 * 13 * 13)
    # 2904 is wrong :(
    # 11830 is too low (random guess)
    # 59150 is wrong (random guess)
  end

  def compute_distance(box1, box2) when box1 == box2, do: :inf

  def compute_distance(box1, box2) do
    {x, y, z} = box1
    {bx, by, bz} = box2
    :math.sqrt(((bx - x) ** 2) + ((by - y) ** 2) + ((bz - z) ** 2))
  end

  def connect_all_junction_boxes(pairs) do
    pairs
    |> Enum.reduce([], fn [box1, box2], circuits ->
      box1_circuit = Enum.find_index(circuits, fn c -> box1 in c end)
      box2_circuit = Enum.find_index(circuits, fn c -> box2 in c end)
      case {box1_circuit, box2_circuit} do
        {nil, nil} -> new_circuit(circuits, box1, box2)
        {index, nil} -> add_boxes_to_circuits(circuits, index, box1, box2)
        {nil, index} -> add_boxes_to_circuits(circuits, index, box1, box2)
        {index1, index2} when index1 == index2 -> circuits
        {index1, index2} -> merge_circuits(circuits, index1, index2)
      end
    end)
  end

  def new_circuit(circuits, box1, box2) do
    new_circuit = MapSet.new([box1, box2])

    [new_circuit | circuits]
  end

  def merge_circuits(circuits, index1, index2) do
    circuit2 = Enum.at(circuits, index2)

    circuits
    |> update_in([Access.at(index1)], & MapSet.union(&1, circuit2))
    |> List.delete_at(index2)
  end

  def add_boxes_to_circuits(circuits, index, box1, box2) do
    update_in(circuits, [Access.at(index)], &add_boxes_to_circuit(&1, box1, box2))
  end

  def add_boxes_to_circuit(circuit, box1, box2) do
    # Caught an early mistake
    if box1 in circuit and box2 in circuit and MapSet.size(circuit) == 2 do
      raise("Somehow adding the same two boxes to existing circuit")
    end

    MapSet.union(circuit, MapSet.new([box1, box2]))
  end
end

# Day8.part1()
Day8.part2()
