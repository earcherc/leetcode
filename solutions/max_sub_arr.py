function maxSubArray(nums: number[]): number {
    // It would be good to try and solve this with the two pointer technique we originally tried but failed... now that we know the solution we should have a better picture

    // Auto increment right pointer
    // If the new sum is negative, we should incrememnet the left pointer to r + 1
        // because if the right pointer on the current iteration resulted in a negative, that basically means it was a bunk number
        // this also means we need access to the current window sum to compare against 'previous' value... 
        // so what I got wrong in my initial attempt was that it didn't matter if it decreased from the 'previous' window... it only mattered that we did go negtive =

    let l = 0 
    let max = nums[0]
    let current = 0
    for (let r = 0; r < nums.length; r++) {
        current += nums[r]

        max = Math.max(max, current)

        if (current < 0) {
            current = 0
            l = r + 1
        }
    }
    return max
};
