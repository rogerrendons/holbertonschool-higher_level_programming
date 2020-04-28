#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 if is not loop and 1 if is loop.
 */

int check_cycle(listint_t *list)
{
	listint_t *a = NULL;
	listint_t *b = NULL;

	a, b = list;

	while (b && a && a->next)
	{
		b = b->next;
		a = a->next->next;
		if (b == a)
		{
			return (1);
		}
	}
	return (0);
}
