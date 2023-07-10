#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle on it.
 * @list: pointer to beginning of node
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *listed;
	listed_t *check;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	listed = list;
	check = listed->next;
	while (listed != NULL && check->next != NULL && check->next->next != NULL)
	{
		if (listed == check)
		{
			return (1);
		}
		listed = listed->next;
		check = check->next->next;
	}
	return (0);
}
