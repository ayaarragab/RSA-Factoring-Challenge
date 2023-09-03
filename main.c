#include "factoring.h"
/**
 * main - main function
 * @argv: vector array
 * @argc: length of argv
 * Return: 0
*/
int main(int argc, char **argv)
{
	char *buffer = malloc(1024);
	size_t n = 1024;
	long long int number;
	FILE *stream;

	if (argc != 2)
		return (0);
	stream = fopen(argv[1], "r+");
	while (getline(&buffer, &n, stream) != -1)
	{
		number = strtoll(buffer, NULL, 10);
		if (sizeof(number) > __SIZEOF_LONG_LONG__)
		{
			/* code */
		}
		
		factor(number);
	}
	free(buffer);
	fclose(stream);
	return (0);
}
