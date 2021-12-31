#ifndef _INTERCODE_H_
#define _INTERCODE_H_

#include <iostream>
#include "Tree.h"
#include "Block.h"
#include<string>
extern struct gramTree* root;

using namespace std;

class InterCode {
private:
	vector<string> codeList;

public:
	int tempNum = 0;
	int varNum = 0;
	int labelNum = 0;
	int arrayNum = 0;

	InterCode();
	void addCode(string);
	void printCode();
	string createCodeforVar(string tempname, string op, varNode node1, varNode node2);
	string createCodeforAssign(varNode node1,varNode node2);
	string createCodeforParameter(varNode node);
	string createCodeforReturn(varNode node);
	string createCodeforArgument(varNode node);

	string getNodeName(varNode node);
	string getarrayNodeName(arrayNode node);
	string getLabelName();
};

#endif 
