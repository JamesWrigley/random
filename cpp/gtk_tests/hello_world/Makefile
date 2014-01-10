hello:
	main.o helloworld.o
	g++ -o hello main.o helloworld.o

main.o:
	main.cpp helloworld.h
	g++ -c main.cpp

helloworld:
	helloworld.cpp helloworld.h
	g++ -c helloworld.cpp

clean:
	rm -f *.o hello
