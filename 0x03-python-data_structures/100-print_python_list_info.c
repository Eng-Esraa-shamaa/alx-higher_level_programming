#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 *print_python_list_info - print python list
 *@p: python object
 *Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int list_size = PyList_Size(p);
	int j;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (j = 0; j < list_size; j++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}
