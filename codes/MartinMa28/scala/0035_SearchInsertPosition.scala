package week3

object Solution {
  def searchInsert(nums: Array[Int], target: Int): Int = {
    for (i <- 0 until nums.length) {
      if (nums(i) >= target) return i
    }

    return nums.length
  }
}

object SearchInsertPosition {
  def main(args: Array[String]): Unit = {
    var i = Solution.searchInsert(Array(1, 3, 5, 6), 2)
    println(i)
  }

}
