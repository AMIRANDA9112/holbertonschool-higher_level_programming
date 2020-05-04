#include "lists.h"

/**
 * print_dlistint - print all elements to a double linked list
 * description - follow de flow of a list to print all positions.
 *@h : pointer of list to print
 * return -  size of list to print
/**

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	const dlistint_t *lector;

	lector = h;

	while (node)
	{
		printf("%d\n", node->n);
		count++;
		lector = lector->next;
	}
	return (count);
}
