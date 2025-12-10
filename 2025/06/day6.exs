defmodule Day6 do
  def part1 do
    # [nums1, nums2, nums3, nums4, operators] =
      "input.txt"
      |> File.read!()
      |> String.split("\n", trim: true)
      |> Enum.map(&String.split/1)
      # [nums1, nums2, nums3, nums4, operators]
      |> Enum.zip_reduce(0, &do_cephalopod_math/2)
      |> IO.inspect(label: "Sum of all answers")
  end

  def do_cephalopod_math([num1, num2, num3, num4, operator], acc) do
    numbers = Enum.map([num1, num2, num3, num4], &String.to_integer/1)
    answer = case operator do
      "+" -> Enum.sum(numbers)
      "*" -> Enum.product(numbers)
    end

    acc + answer
  end
end


Day6.part1()
