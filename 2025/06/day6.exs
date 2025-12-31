defmodule Day6 do
  def part1 do
    "input.txt"
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.zip_reduce(0, &do_cephalopod_math/2)
    |> IO.inspect(label: "Sum of all answers")
  end

  def do_cephalopod_math([num1, num2, num3, num4, operator], acc) do
    numbers = Enum.map([num1, num2, num3, num4], &String.to_integer/1)

    answer =
      case operator do
        "+" -> Enum.sum(numbers)
        "*" -> Enum.product(numbers)
      end

    acc + answer
  end

  ###########################################

  def part2() do
      "input.txt"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&String.graphemes/1)
      |> Enum.zip()
      |> Enum.chunk_while([], &parse_column/2, &last_chunk_handler/1)
      |> Enum.map(&do_part2_math/1)
      |> Enum.sum()
      |> IO.inspect(label: "Part 2 cephalopod math result")
      # 10956759080756 is too low - I see I'm not parsing the last chunk! Oh no!
      # 11136895955912 - I had misunderstood the last arg to Enum.chunk_while. It's for leftovers!
  end

  def parse_column(column, acc) do
    if column |> Tuple.to_list() |> Enum.all?(&(&1 == " ")) do
      # column is empty - it separates this math problem from the next. Emit a chunk
      {:cont, acc, []}
    else
      # column is not empty - parse numbers and maybe operator then add to accumulator
      {:cont, add_to_acc(column, acc)}
    end
  end

  def last_chunk_handler(x), do: {:cont, x, []}

  def add_to_acc(col_tup, acc) do
    {d1, d2, d3, d4, op} = col_tup
    number = (d1 <> d2 <> d3 <> d4) |> String.trim() |> String.to_integer()

    case {op, acc} do
      # the operator is always in the first cephalopod number
      {op, []} -> [number, op]
      {" ", acc} -> [number | acc]
    end
  end

  def do_part2_math(entries) do
    [operator | numbers] = Enum.reverse(entries)

    case operator do
      "+" -> Enum.sum(numbers)
      "*" -> Enum.product(numbers)
    end
  end
end

# Day6.part1()
Day6.part2()
