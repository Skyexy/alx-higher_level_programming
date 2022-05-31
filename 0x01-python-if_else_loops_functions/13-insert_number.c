#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds node to linked list
 * @head: pointer to address of head
 * @number: number to be added
 * Return: pointer if added NULL if not
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *prev, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	current = prev = *head;
	while (number > current->n && current->next != NULL)
	{
		prev = current;
		current = current->next;
	}
	if (current->next == NULL)
	{
		if (number > current->n)
			add_nodeint_end(head, number);
		else
		{
			new->next = current;
			prev->next = new;
		}
		return (new);
	}
	if (prev == *head)
	{
		*head = new;
		new->next = current;
		return (new);
	}
	current = prev;
	new->next = current->next;
	current->next = new;
	return (new);
}
