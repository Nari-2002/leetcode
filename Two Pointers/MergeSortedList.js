var merge = function(nums1, m, nums2, n) {
    nums1.splice(m)
    nums2.splice(n)
    for (let num of nums2) {
        nums1.push(num)
    }
    nums1.sort((a, b) => a - b)
};
