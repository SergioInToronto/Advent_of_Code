defmodule Day8 do
  def part1 do
    junction_boxes =
      File.read!("input.txt")
      |> String.split("\n", trim: true)
      |> Enum.map(&String.split(&1, ","))
      |> Enum.map(fn parts -> Enum.map(parts, &String.to_integer/1) end)
      |> Enum.map(&List.to_tuple/1)
      |> dbg()

    # First shortest distances
    # TODO: actual puzzle solution
    junction_boxes
    |> Enum.with_index(1)
    |> Enum.map(&nearest_neighbour(&1, junction_boxes))
    |> IO.inspect(label: "First nearest neighbour", printable_limit: :infinity, limit: :infinity)
  end

  def nearest_neighbour({box, line_no}, boxes) do
    {box, line_no}
    |> neighbour_distances(boxes)
    |> Enum.min_by(fn {box, distance} -> distance end)
    |> elem(0)
  end

  # TODO: YOU ARE HERE: use this function to achieve success
  def nearest_neighbour_excluding({box, line_no}, boxes, excluded_boxes) do
    valid_boxes = boxes |> Enum.reject(fn b -> b in excluded_boxes end)

    {box, line_no}
    |> neighbour_distances(valid_boxes)
    |> Enum.min_by(fn {box, distance} -> distance end)
    |> elem(0)
  end

  def neighbour_distances({box, line_no}, boxes) do
    {x, y, z} = box

    boxes
    |> Enum.map(fn current_box ->
      distance = compute_distance(box, current_box)
      {current_box, distance}
    end)

    # |> dbg()
  end

  def compute_distance(box1, box2) when box1 == box2, do: :inf

  def compute_distance(box1, box2) do
    {x, y, z} = box1
    {bx, by, bz} = box2
    :math.sqrt((bx - x) ** 2 + (by - y) ** 2 + (bz - z) ** 2)
  end
end

Day8.part1()
