#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} node;

// Creating a new element
node* createNode(int data) {
    node* newNode = (node*) malloc(sizeof(node));           // allocating space for an element
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;                                        // appointing variables of the element
    newNode->next = NULL;
    return newNode;
}

// Inserting an element in the end of the list
void insert(node** headRef, int data) {
    node* newNode = createNode(data);                           // creating an element with function
    if (*headRef == NULL) {                                     // appointing element's address if list is empty
        *headRef = newNode;
    } else {                                                    // adding element's address if list is not empty
        node* current = *headRef;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

// Rearranging elements inside a list
void rearrange(node** headRef) {
    node* negativeHead = NULL;
    node* positiveHead = NULL;
    node* current = *headRef;

    // Dividing into two groups
    while (current != NULL) {
        if (current->data < 0) {
            insert(&negativeHead, current->data);
        } else {
            insert(&positiveHead, current->data);
        }
        current = current->next;
    }

    // Mixing groups together
    node* mergedHead = NULL;
    node* mergedTail = NULL;

    current = negativeHead;
    while (current != NULL) {
        if (mergedHead == NULL) {
            mergedHead = current;
            mergedTail = current;
        } else {
            mergedTail->next = current;
            mergedTail = current;
        }
        current = current->next;
    }

    current = positiveHead;
    while (current != NULL) {
        if (mergedHead == NULL) {
            mergedHead = current;
            mergedTail = current;
        } else {
            mergedTail->next = current;
            mergedTail = current;
        }
        current = current->next;
    }

    *headRef = mergedHead;
}

// Printing elements of the list
void printElements(node* head) {
    node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

// Freeing memory after finishing
void freeMemory(node* head) {
    node* current = head;
    node* next;
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
}

int main() {
    node* head = NULL;                              // creating an empty list

    int n;
    printf("Enter the number that is a multiple of 20:");
    scanf("%d", &n);

    if (n % 20 != 0) {
        printf("Your number is not a multiple of 20\n");
        return -1;
    }

    printf("Enter %d elements for the list:\n", n);
    for (int i = 0; i < n; ++i) {
        int value;
        scanf("%d", &value);
        insert(&head, value);       // inserting elements inside the list
    }

    printf("Initial list:\n");
    printElements(head);

    rearrange(&head);                   // rearranging list

    printf("New list:\n");
    printElements(head);

    freeMemory(head);                           // freeing memory after operations

    return 0;
}
