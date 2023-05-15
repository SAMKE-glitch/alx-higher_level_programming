#include "lists.h"

/**
 * rev_listint - reverses a singly linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void rev_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *present = *head;
	listint_t *next = NULL;

	while (present)
	{
		next = present->next;
		present->next = previous;
		previous = present;
		present = next;
	}

	*head = previous;
}
/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: double pointer to the singly linked list
 *
 * Return: 1 if it is, and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	rev_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dup)
		return (1);

	return (0);
}
