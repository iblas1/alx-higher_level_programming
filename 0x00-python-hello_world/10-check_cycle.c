#include "lists.h"

/**
 * check_cycle - adds a new node at the beginning of a listint_t list
 * @list: pointer to a pointer of the start of the list
 * Return: address of the new element or NULL if it fails
 */

int check_cycle(listint_t *list)
{
	listint_t *backward, *forward;

	if (list == NULL)
		return (0);

	backward = forward = list;

	while (forward != NULL && forward->next != NULL)
	{
		backward = backward->next;
		forward = forward->next->next;

		if (backward == forward)
			return (1);
	}

	return (0);
}
