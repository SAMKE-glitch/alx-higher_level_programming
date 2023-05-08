#include "lists.h"

/**
 * check_cycle - function that checks if a list contains a cycl;e
 * @lisr: linked list to look upto
 *
 * Return: 1 if the list has a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return(0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return(1);
	}
	return (0);
}
