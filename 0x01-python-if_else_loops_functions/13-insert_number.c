#include "lists.h"
/**
 * insert_node - inserts a node into a linked list
 * @head: Address of pointer to pointer to head of list
 * @number: An integer value of the node to be added
 * Return: A pointer to linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ahead = *head, *prev = *head;
	listint_t *new_node;
	int flag = 1;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	while (ahead->next != NULL)
	{
		if (ahead->n >= number)
		{
			flag = 0;
			new_node->next = ahead;
			prev->next = new_node;
			break;
		}
		prev = ahead;
		ahead = ahead ->next;
	}
	if (flag)
		ahead->next = new_node;
	return (*head);
}
