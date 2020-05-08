#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: header list
 * Return: 1 if is or 0 if is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *cmp = (*head);
	int temp[1024];
	int i = 0, j;

	if (head == NULL || *head == NULL)
		return (1);
	while (cmp)
	{
		temp[i] = cmp->n;
		cmp = cmp->next;
		i++;
	}
	i = i - 1;
	for (j = 0; j <= i ; j++)
	{
		if (temp[i] != temp[j])
			return (0);
		 i--;
	}
	return (1);
}
