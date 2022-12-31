/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let length = nums1.length + nums2.length;
    let mid = Math.floor(length / 2);
    if(length % 2 !== 0){
        mid += 1;
    }
    let next = null
    let i = 0;
    while(i < mid){
        next = getNext();
        i += 1;
    }

    function getNext(){
        if(nums1.length === 0){
            return nums2.shift()
        }else if(nums2.length === 0){
            return nums1.shift()
        }else{
            return nums1[0] <= nums2[0] ? nums1.shift() : nums2.shift();
        }
    }
    if(length % 2 === 0){
        return (next + getNext()) / 2
    }

    return next;
};