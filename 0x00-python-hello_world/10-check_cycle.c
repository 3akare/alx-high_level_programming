#include "lists.h"
/**
 * check_cycle  - checks if a singly linked list has a cycle in it
 * @head:  a linked list
 * using the Floyd's Cycle-finging Algorithm
 * Return: (1) if True and (0) if false
 */

int check_cycle(listint_t *head)
{
	listint_t *fast = head, *slow = head;

	if (!head)
		return (0);

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}

