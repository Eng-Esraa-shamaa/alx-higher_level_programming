#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle on it.
 * @list: pointer to beginning of node
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *slowly;
	listint_t *faster;

	slowly = list;
	faster = list;
	if (list == NULL)
	{
		return (0);
	}
	while (slowly != NULL && faster != NULL && faster->next != NULL)
	{
		slowly = slowly->next;
		faster = faster->next->next;
		if (slowly == faster)
		{
			return (1);
		}
	}
	return (0);
}
