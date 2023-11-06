#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - hgffxx
 * @head: jgfc
 * Return: bvvccx
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL;
	listint_t *current = slow;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	listint_t *first = *head;
	listint_t *second = prev;

	while (second != NULL)
	{
		if (first->n != second->n)
		{
			return (0);
		}
		first = first->next;
		second = second->next;
	}
	return (1);
}

