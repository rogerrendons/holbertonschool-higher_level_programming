#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * get_dnodeint_at_index - get determinate node.
 * @head: Head of linked list.
 * @index: Item of node
 * Return: Always 0.
*/

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *new;
	unsigned int cont = 0;

	new = head;

	if (head == NULL)
		return (NULL);

	for (cont = 0; cont < index; cont++)
	{
		if (new->next == NULL)
		{
			return (NULL);
		}
		new = new->next;
	}
	return (new);
}
