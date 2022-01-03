#include "lists.h"

/**
 * is_palindrome - palindrome
 * @head: list
 *
 * Return: palidrome or not
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL && *head == NULL)
		return (1);
	else
		return (palindrome(head, *head));
}

/**
 * palindrome - check equal
 * @head: list
 * @end: list
 * 
 * Return:
 */

int palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (palindrome(head, end->next))
	{
		if ((*head)->n == end->n)
		{
			*head = (*head)->next;
			return (1);
		}
	}

	return (0);
}