#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * desc- Technical interview practice
 * @head: a listint_t list
 *
 * Return: 1 if @head is a plaindrome, else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *temp2 = *head;
	int len = 0, i = 0, eq = 0, *int_array, j = 0;

	while (temp != NULL)
	{
		temp = (temp)->next;
		len++;
	}
	int_array = malloc(sizeof(int) * len);
	while (temp2 != NULL)
	{
		int_array[i] = temp2->n;
		temp2 = temp2->next;
		i++;
	}
	for (j = 0; j < len; j++)
	{
		if (int_array[j] == int_array[len - j - 1])
		{
			eq++;
		}
	}
	if (eq == len)
		return (1);
	return (0);
}
