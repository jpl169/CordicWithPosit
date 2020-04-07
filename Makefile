CC=g++

analysisExec =  bin/posit_cordic_default \
		bin/posit_cordic_quirez \
		bin/posit_cordic_start_late \
		bin/posit_cordic_quirez_start_late \
		bin/float_cordic \
		bin/posit_vector_default \
		bin/posit_vector_quirez \
		bin/posit_vector_start_late \
		bin/posit_vector_quirez_start_late \
		bin/float_vector \
		bin/posit_cordic_default_1kstep \
		bin/posit_cordic_quirez_1kstep \
		bin/posit_cordic_start_late_1kstep \
		bin/posit_cordic_quirez_start_late_1kstep \
		bin/float_cordic_1kstep \
		bin/posit_vector_default_1kstep \
		bin/posit_vector_quirez_1kstep \
		bin/posit_vector_start_late_1kstep \
		bin/posit_vector_quirez_start_late_1kstep \
		bin/float_vector_1kstep \
		bin/atanpow2 \
		bin/sinpow2 \
		bin/cosnearpi

all: lib/lib_cordic.a $(analysisExec)

obj/lib_cordic.o: source/cordic.cpp
	@ mkdir -p obj
	$(CC) -std=gnu++11 -c -I$(SOFTPOSITPATH)/source/include -I./include source/cordic.cpp -o obj/lib_cordic.o

lib/lib_cordic.a: obj/lib_cordic.o
	@ mkdir -p lib
	ar rcs lib/lib_cordic.a obj/lib_cordic.o

bin/%: analysis/%.cpp
	@ mkdir -p bin
	$(CC) -std=gnu++11 $< -o $@ -I$(SOFTPOSITPATH)/source/include -I./include $(SOFTPOSITPATH)/build/Linux-x86_64-GCC/softposit.a lib/lib_cordic.a -lmpfr -lgmp 



clean:
	rm -rf obj/ lib/ bin/