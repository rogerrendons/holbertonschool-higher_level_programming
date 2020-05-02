#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * dlistint_len - for managment of a list
 * @h: poniter
 * Return: forward Value Counter.
*/

size_t dlistint_len(const dlistint_t *h)
{
	int forward;

	if (h == '\0')
		return (0);

	for (forward = 1; h->next != '\0'; forward++)
	{
		h = h->next;
	}
	return (forward);
}
