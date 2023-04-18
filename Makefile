stderr:
	python3 -m file_descriptor.example_1 2> /dev/null

#Redirecting the stream of errors from stderr that has file descriptor <2. to a file
stderr_2:
	python3 -m file_descriptor.example_1 2> file_descriptor/errors.txt

read_err:
	cat file_descriptor/errors.txt