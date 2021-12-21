#include "lists.h"

/**
 * insert_node - sort
 * @head: pointer
 * @number: nb
 *
 * Return: NULL or Pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n = *head, *newest;

	newest = malloc(sizeof(listint_t));
	if (newest == NULL)
		return (NULL);
	newest->n = number;

	if (n == NULL || n->n >= number)
	{
		newest->next = n;
		*head = newest;
		return (newest);
	}

	while (n && n->next && n->next->n < number)
		n = n->next;

	newest->next = n->next;
	n->next = newest;

	return (newest);
}
