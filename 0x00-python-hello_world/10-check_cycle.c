#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)

{

listint_t *head = list;
listint_t *foot = list;

if(head)
{
	while (foot && foot->next)
	{
	head = head->next;
	foot = foot->next;
	foot = foot->next;

	if (foot == head)
	{
	return(1);
	}
	}
}
return(0);
}
