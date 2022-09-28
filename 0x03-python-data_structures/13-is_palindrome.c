#include "lists.h"
/**
 * reverse_listint - reverses a linked list
 * @head: address of a linked lint
 *
 * Return: always succesful
 */

listint_t *reverse_listint(listint_t **head)
{

	listint_t *prev = NULL, *next = NULL, *current;

	if (head == NULL || *head == NULL)
		return (NULL);

	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * desc- Technical interview practice
 * @head: a listint_t list
 *
 * Return: 1 if @head is a plaindrome, else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2;

	temp2 = reverse_listint(head);
	while (temp != NULL && temp2 != NULL)
	{
		if (temp->n != temp2->n)
			return (0);
		temp = temp->next;
		temp2 = temp2->next;
	}
	return (1);
}
