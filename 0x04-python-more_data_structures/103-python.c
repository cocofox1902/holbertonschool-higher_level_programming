#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	long int size;
	int i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf(" first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
	printf("\n");
}

void print_python(PyObject *p)
{
	int i;
	long int lenght = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", lenght);
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < lenght; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(((PyListObject *)p)->ob_item[i])->tp_name);
		if (!strcmp((((PyListObject *)p)->ob_item[i])->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}
