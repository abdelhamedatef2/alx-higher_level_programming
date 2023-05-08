#include "lists.h"

/**
 * check_cycle - checks for loop in ll
 * @list: linkedlist's head
 *
 * Description - checks for loop in ll
 * Return: 1 when cycled, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
