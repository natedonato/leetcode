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
    if(!list1){
        return list2;
    }else if(!list2){
        return list1;
    }

    let currentNode, head;


    while(list1 && list2){
        let next;
        if(list1.val < list2.val){
            next = list1
            list1 = list1.next;
        } else{
            next = list2;
            list2 = list2.next;
        }
        if(!currentNode){
            currentNode = next;
            head = currentNode;
        }else{
            currentNode.next = next;
            currentNode = next;
        }
    }

    if(list1){currentNode.next = list1}
    else if(list2){currentNode.next = list2}


    return head;
};