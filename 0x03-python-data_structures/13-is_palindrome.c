#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
int is_palindrome(Node** head)
{
	if (*head == NULL || (*head)->next == NULL) {
		            return 1; // An empty list or a list with a single node is considered a palindrome
			        }

	        // Find the length of the linked list
	        int length = 0;
		    Node* current = *head;
		        while (current != NULL) {
				        length++;
					        current = current->next;
						    }
			linked list
				    Node* prev = NULL;
			    current = *head;
			        int count = 0;
				    while (count < length / 2) {
					            Node* next = current->next;
						            current->next = prev;
							            prev = current;
								            current = next;
									            count++;
										        }
				    if (length % 2 != 0) {
					            current = current->next;
						        }

				        // Compare the reversed first half with the second half of the linked list
				        while (current != NULL) {
						        if (current->data != prev->data) {
								            return 0; // Not a palindrome
									            }
							        current = current->next;
								        prev = prev->next;
									    }

					    return 1; // Palindrome
}

