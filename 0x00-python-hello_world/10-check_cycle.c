#include "lists.h"

/**
 * checK-cycle - checks if there is a cycle in the struct node
 * @list: pointer to a struct
 * Return: 0 for no cycles and 1 for cycles present
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
