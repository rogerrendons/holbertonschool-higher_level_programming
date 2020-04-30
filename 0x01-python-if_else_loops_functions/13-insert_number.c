/**
 * insert_node - insert number in linked list
 * @head: node head
 * @number: number from main
 *
 * Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pointer = NULL, *NewN = NULL;

	if (head == NULL)
		return (NULL);
	NewN = malloc(sizeof(listint_t));
	if (NewN)
	{
		NewN->n = number;
		NewN->next = *head;
		if (!*head || NewN->n <= (*head)->n)
			*head = NewN;
		else
		{
			pointer = NewN->next;
			NewN->next = pointer->next;
			while (NewN->next && NewN->n >= NewN->next->n)
            {
				pointer = NewN->next;
				NewN->next = pointer->next;
			}
			pointer->next = NewN;
		}
	}
	return (NewN);
}
