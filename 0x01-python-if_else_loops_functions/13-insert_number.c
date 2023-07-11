#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 *insert_node - function inserts number into a sorted singly linked list
 *@head: head of node
 *@number: the number to be inserted
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	while ((node != NULL) && (node->next != NULL) && (node->next->n < number))
	{
		node = node->next;
	}
	new_node->next = node->next;
	node->next = new_node;
	return (new_node);
}
