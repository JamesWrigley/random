CC = g++
CFLAGS = -Wall -g -std=c++11
LDFLAGS = -lboost_system -lboost_filesystem

stats_functions.o: stats_functions.cpp stats_functions.h
	${CC} ${CFLAGS} -c stats_functions.cpp

stats.o: stats.cpp stats_functions.h
	${CC} ${CFLAGS} -c stats.cpp

stats: stats.o stats_functions.o
	${CC} ${CFLAGS} stats_functions.o stats.o ${LDFLAGS} -o stats

# Unit tests
stats_functions_tests.o:
	${CC} ${CFLAGS} -c stats_functions_tests.cpp

stats_tests: stats_functions_tests.o stats_functions.o
	${CC} ${CFLAGS} stats_functions_tests.o stats_functions.o ${LDFLAGS} -lgtest -o stats_tests


clean:
	rm stats_functions.o stats.o stats stats_functions_tests.o stats_tests
