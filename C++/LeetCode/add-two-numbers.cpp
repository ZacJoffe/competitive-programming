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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = 0;
        ListNode *list = NULL;
        ListNode **i = &list;
        
        while (sum > 0 || l1 != NULL || l2 != NULL) {
            if (l1 != NULL) {
                sum += l1->val;
                l1 = l1->next;
            }
            
            if (l2 != NULL) {
                sum += l2->val;
                l2 = l2->next;    
            }
            
            if (sum >= 10) {
                *i = new ListNode(sum % 10);
            } else {
                *i = new ListNode(sum);
            }
            
            sum /= 10;
            i = &((*i)->next);
        }
        
        return list;
    }
};
