/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let root = null;
    
    if(list1 === null && list2 !== null || (list2 !== null && list1.val >= list2.val)){
        root = list2;
        list2 = list2.next;
    }else if(list1 !== null){
        root = list1;
        list1 = list1.next;
    }

    let current = root;
    while(list1 !== null && list2 !== null){
        if(list1.val >= list2.val){
            current.next = list2;
            current = current.next;
            list2 = list2.next;
        }else{
            current.next = list1;
            current = current.next;
            list1 = list1.next;
        }
    }
    if(list1 !== null){
        current.next = list1;
    }else if (list2 !== null){
        current.next = list2
    }

    return root;
};