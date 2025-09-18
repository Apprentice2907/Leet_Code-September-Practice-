// # My logic 

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* slow=head,*fast=head;
        while(fast&&fast->next){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* prev=nullptr;
        while(slow){
            ListNode* nxt=slow->next;
            slow->next=prev;
            prev=slow;
            slow=nxt;
        }
        ListNode* left=head,*right=prev;
        while(right){
            if(left->val!=right->val) return false;
            left=left->next;
            right=right->next;
        }
        return true;
    }
};





//  Leetcode best solution

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
ListNode* getmid(ListNode* head){
    ListNode* fast=head->next;
    ListNode* slow=head;

    while(fast!=NULL && fast->next!=NULL){
        fast=fast->next->next;
        slow=slow->next;
    }

    return slow;
}

ListNode* reverse(ListNode* head){
    ListNode* curr=head;
    ListNode* prev=NULL;
    ListNode* forward=NULL;

    while(curr!=NULL){
        forward=curr->next;
        curr->next=prev;
        prev=curr;
        curr=forward;
    }
    return prev;

}

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return true;
        }

        if(head->next->next==NULL){
            if(head->val==head->next->val){
                return true;
            }
            else{
                return false;
            }
        }

        ListNode* middle=getmid(head);

        ListNode* temp=middle->next;
        middle->next=reverse(temp);

        ListNode* head1=head;
        ListNode* head2=middle->next;

        while(head2!=NULL){
            if(head1->val != head2->val){
                return false;
            }
            head1=head1->next;
            head2=head2->next;
        }

        temp=middle->next;
        middle->next=reverse(temp);

        return true;

    }
};
