#include "lists.h"

/**
 * is_palindrome - checks if slingly linked list is a palindrome or not
 * @head: Pointer to the slingly linked list
 * Return: 1 for a palindrome or 0 for none palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node_moving_right = *head;
	listint_t *node_moving_left;
	listint_t *node_used_to_count = *head;
	int no_of_node = 0, first_value = 1, last_value;
	int flag = 1, loop_counter;

	if (*head == NULL)
		return (1);
	/* count the number of nodes in the singly linked list*/
	while (node_used_to_count != NULL)
	{
		no_of_node++;
		node_used_to_count = node_used_to_count ->next;
	}
	/* loop from the start*/
	while (node_moving_right != NULL)
	{
		node_moving_left = *head;
		last_value = no_of_node + 1 - first_value;
		loop_counter = 1;
		/* loop until you reach the value of last_value*/
		while (loop_counter < last_value)
		{
			node_moving_left = node_moving_left->next;
			loop_counter++;
		}
		if (node_moving_right->n != node_moving_left->n)
		{
			flag = 0;
			break;
		}
		if (first_value == last_value)
		{
			flag = 1;
			break;
		}
		first_value++;
		node_moving_right = node_moving_right->next;
	}
	if (flag)
		return (1);
	return(0);
}
