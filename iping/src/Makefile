BUILDDIR=../build
GCC=g++
INC=-I/usr/include/irods/ -I/usr/include/irods/boost/
LINK=-L/usr/lib/irods/externals -lirods_client_core -lirods_client_api -lirods_client -lboost_regex -lboost_system -lboost_thread -lboost_chrono -lboost_date_time -lboost_filesystem -lboost_iostreams -lboost_program_options /usr/lib/irods/externals/libjansson.a -lcrypto -lssl -ldl -lm -lcurl -lpthread

install: $(BUILDDIR) iping move

$(BUILDDIR):
	mkdir -p $@

iping:
	${GCC} ${INC} -fPIC -o iping iping.cpp ${LINK}

move:
	mv iping $(BUILDDIR)/iping
