#include "lists.h"
/**
 *reverse_list - function reverse  a list
 *@head: head of list
 *Return : nothing
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;
	listint_t *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 *is_palindrome - checks if a list is a plaindrome or no
 *@head: head of list
 *Return: 1 if palindrome , 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = *head;
	listint_t *mid = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (fast == NULL)
		{
			mid = slow->next;
			break;
		}
		if (!fast->next)
		{
			mid = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_list(&mid);
	while (prev && mid)
	{
		if (prev->n == mid->n)
		{
			mid = mid->next;
			prev = prev->next;
		}
		else
			return (0);
	}
	if (mid == NULL)
		return (1);

	return (0);
}
