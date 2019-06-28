/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *reversed = NULL;
        ListNode *current = head;
        while (current != NULL) {
            // swap next to previous, iterate current to next node
            ListNode *next = current->next;
            current->next = reversed;
            reversed = current;
            current = next;
        }
        return reversed;
    }
};