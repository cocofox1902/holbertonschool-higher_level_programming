#include <Python.h>

/**
 * print_python_list_info - print list in python
 * @p: python object
 *
 * Return: none
 */

void print_python_list_info(PyObject *p)
{
	int i;
	long int lenght = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", lenght);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < lenght; i++)
		printf("Element %i: %s\n", i, Py_TYPE(((PyListObject *)p)->ob_item[i])->tp_name);
}