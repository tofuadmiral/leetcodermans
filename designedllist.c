typedef struct {
    int val;
    struct MyLinkedList* next; // pointer to next item
    int size;  // size of list
} MyLinkedList;

/** Initialize your data structure here. returns a pointer to the linkedlist object that we create  */
MyLinkedList* myLinkedListCreate() {
    // initialize the size of the list
    // we want to return a pointer so create that, and make sure right size i.e.
    // make sure to allocate enough for MyLinkedList pointers
    MyLinkedList* obj = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    // arrow notation bc obj is a pointer
    obj->val=0;
    obj->next=NULL;
    obj->length=-1; // -1 bc just head, we start at zero
    return obj;
    // this obj has enough memory for a list, and also has ONLY the head pointer
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
int myLinkedListGet(MyLinkedList* obj, int index) {
    if(index > obj->size()) return -1; // bc we're above the size
    if (index < 0) return -1; // invalid question bc starts at 0
    // obj is just a pointer to the list, so we can re-reference that pointer to
    // another pointer i.e. the "next", and doing that won't actually change anything
    // in the actual list, since obj is just pointing to that existing list.
    int counter =-1;
    while(counter <= size && != index){
        obj = obj->next;
        counter++;
    }
    // now, we should be at the index that the element is actually at, so just
    // return the value that we're at
    return obj->val;
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    
}

/** Append a node of value val to the last element of the linked list. */
void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    
}

/** Delete the index-th node in the linked list, if the index is valid. */
void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    
}

void myLinkedListFree(MyLinkedList* obj) {
    
}

/**
 * Your MyLinkedList struct will be instantiated and called as such:
 * struct MyLinkedList* obj = myLinkedListCreate();
 * int param_1 = myLinkedListGet(obj, index);
 * myLinkedListAddAtHead(obj, val);
 * myLinkedListAddAtTail(obj, val);
 * myLinkedListAddAtIndex(obj, index, val);
 * myLinkedListDeleteAtIndex(obj, index);
 * myLinkedListFree(obj);
 */
