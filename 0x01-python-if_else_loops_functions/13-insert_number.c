
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)

{

    int i = 0;
    int l = 0;
    listint_t *new;
    listint_t *current;
    listint_t *back;


    current = *head;
    new = malloc(sizeof(listint_t));

    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
     back = malloc(sizeof(listint_t));
     back->n = 0;
     back->next = NULL;

        while (current->next != NULL)
	   {
           current = current->next;
	   l++;
           if (current->n > number)
              i++;
           }

	current->next = back;

	while (l > i)
        {
         current[l] = current[l-1];
         l--;
	}
        current[i] = number;

    }
    return (back);
}
