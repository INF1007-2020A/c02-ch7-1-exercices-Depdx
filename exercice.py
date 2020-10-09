#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(nb):
	# if TODO==0:
	# 	return 0
	# if TODO == 1:
	# 	return 1
	# return get_fibonacci_number(TODO-1) + get_fibonacci_number(TODO-2)

	return (
		0 if nb==0 else
		1 if nb==1 else
		get_fibonacci_number(nb-1)+get_fibonacci_number(nb-2)
	)
def get_fibonacci_sequence(lenght, seq=[0,1]):
	return (
		seq[0:lenght] if lenght <= 2 else
		get_fibonacci_sequence(lenght, seq=seq+[seq[-1]+seq[-2]]) if len(seq)<lenght else
		seq
	)
def get_sorted_dict_by_decimals(dict_):
	return dict(sorted(dict_.items(),key= lambda item : item[1]%1))

def fibonacci_numbers(lenght):
	INIT_VALUES = [0,1]
	for i, elem in enumerate(INIT_VALUES):
		if i >=lenght:
			break
		yield elem
	last_elems = deque(INIT_VALUES)
	for i in range(len(INIT_VALUES),lenght):
		fibo_number=last_elems[-1] +last_elems[-2]
		last_elems.append(fibo_number)
		last_elems.popleft()
		yield fibo_number

def build_recursive_sequence_generator(valeur_initiales, def_function, lenght, is_memory_kept =False):
	for i, valeur in enumerate(valeur_initiales):
		if i > lenght:
			break
		yield valeur
	last_elem = deque(valeur_initiales)
	for i in range(len(valeur_initiales), lenght):
		number = def_function(last_elem)
		last_elem.append(number)
		last_elem.popleft()
		yield number

if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(15):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def,30)
	for fi in fibo:
		print(fi, end=" ")
	print("\n")


def nombre_holstadter_Q(n):
	if n[1] == 1 or n[0] == 0:
		return 1
	return nombre_holstadter_Q(n[0]-nombre_holstadter_Q(n[:-1])) + nombre_holstadter_Q(n[0]-nombre_holstadter_Q(n[-2]))


lucas = build_recursive_sequence_generator([2,1], lambda x : x[-1]+x[-2],10)
print(f"Lucas : {[elem for elem in lucas]}")
perrin = build_recursive_sequence_generator([3,0,2],lambda x: x[-2]+x[-3] ,10)
print(f"Perrin : {[elem for elem in perrin]}")
hofstadter_q = build_recursive_sequence_generator([1,1,2], nombre_holstadter_Q,10)
print(f"Hofstadter-Q : {[elem for elem in hofstadter_q]}")