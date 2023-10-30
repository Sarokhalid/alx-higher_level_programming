#include <stdio.h>
#include <stdlib.h>
#include "list.h"
/**
 * check_cycle - bvcx
 * @list: hggccc
 * Return: jbvvvc
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
