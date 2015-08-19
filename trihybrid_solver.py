#!/usr/bin/python2.7

# Newbi3
# 2/3/14
#
# This program will calculate the possibilities for different traits

import os
import time
import sys

# A list of traits from each parrent
parent1 = []
parent2 = []

def main():
	''' This function will launch the program '''
	while 1:
		getParentsTraits()
		if checkTraitLengths():
			print "Calculating results..."
			break
		else:
			print "You need an equal amount of traits for each parent!"
			print "Try again!"
	offSpringTraits = calculateResults()
	for i in range(0, len(offSpringTraits)):
		sys.stdout.write(offSpringTraits[i])
	saveToFile(offSpringTraits)	

def getParentsTraits():
	''' This function will get a list of traits for each parent from the user '''
	global parent1, parent2
	print "Enter the allele of parent 1 seperated by spaces below"
	parent1 = raw_input("Parent 1 traits> ").split(" ")
	print "Enter the allele of parent 2 seperated by spaces below"
	parent2 = raw_input("Parent 2 traits> ").split(" ")

def checkTraitLengths():
	''' This function will check to make sure there are an equal amount of traits for each parent '''
	if len(parent1) == len(parent2):
		return True
	else:
		return False

def calculateResults():
	''' This function will calculate the results '''
	offSpringTraits = []

	for i in range(0, len(parent1)):
		offSpringTraits.append("\t[ " + parent1[i] + " ]")

	for a in range(0, len(parent1)):
		offSpringTraits.append("\n")
		offSpringTraits.append("\n[" + parent2[a] + "]\t")

		for b in range(0, len(parent1)):
			offSpringTraits.append(" " + formatAlleles(list(parent1[b] + parent2[a])) + " |\t")

	return offSpringTraits

def formatAlleles(traits):
	''' This function will format the alleles '''
	formatted = []

	for a in range(0, len(traits)):
		if traits[a] != "":
			t1 = traits[a]
			for b in range(0, len(traits)):
				t2 = traits[b]
				if a != b and t2.lower() == t1.lower():
					formatted.append(t1)
					formatted.append(t2)
					traits[a] = ""

	return ''.join(formatted)

def saveToFile(results):
	''' This function will save the results to a text file '''
	save = False
	while 1:
		toSave = raw_input("\n\nWould you like to save this table? (yes/no): ")
		if toSave.split(" ") == "":
			print "Please say yes or no"
			continue
		else:
			if toSave == "yes":
				save = True
			break
	if save:
		while 1:
			name = raw_input("Please type the name of the file: ")
			if name.split(" ") == "":
				print "The name can not be empty!"
				continue
			else:
				break

		f = open(name, "w")
		for i in range(0, len(results)):
			f.write(results[i])
		f.close()
		print "Saved file as " + name
	print "Good Bye."

main()
