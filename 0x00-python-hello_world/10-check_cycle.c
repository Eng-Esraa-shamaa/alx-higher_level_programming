#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle on it.
 * @list: pointer to beginning of node
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *a;
	listint_t *b;

	a = list;
	b = list;
	if (list == NULL)
	{
		return (0);
	}
	while (a != NULL && b != NULL && b->next != NULL)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
		{
			return (1);
		}
	}
	return (0);
}
