#include "InterCode.h"
#include "Assist.h"
#include <fstream>

InterCode::InterCode() {

}

void InterCode::addCode(string str) {
	codeList.push_back(str);
}

void InterCode::printCode() {

	ofstream out("InterCode.txt",fstream::out);

	cout << "\n===============INTERCODE===============" << endl;
	for (string s : codeList) {
		cout << s << endl;
		out << s << "\n";
	}
}

string InterCode::createCodeforVar(string tempname, string op, varNode node1, varNode node2) {
	string result = tempname + " := ";
	if (node1.useAddress) {
		result += "*" + node1.name;
	}
	else {
		if (node1.num < 0) {
			result += node1.name;
		}
		else result += "var" + inttostr(node1.num);
	}
	
	result += " " + op + " ";

	if (node2.useAddress) {
		result += "*" + node2.name;
	}
	else {
		if (node2.num < 0) {
			result += node2.name;
		}
		else result += "var" + inttostr(node2.num);
	}

	return result;

}

string InterCode::createCodeforAssign(varNode node1, varNode node2) {
	string result;
	if (node1.useAddress) {
		result = "*" + node1.name + " := ";
	}
	else {
		result = "var" + inttostr(node1.num);
		result += " := ";
	}

	if (node2.useAddress) {
		result += "*" + node2.name;
	}
	else {
		if (node2.num < 0) {
			result += node2.name;
		}
		else result += "var" + inttostr(node2.num);
	}
	

	return result;
}

string InterCode::createCodeforParameter(varNode node) {
	string result = "PARAM ";
	result += "var" + inttostr(node.num);
	return result;
}

string InterCode::createCodeforReturn(varNode node) {
	string result = "RETURN ";
	if (node.useAddress) {
		result += "*" + node.name;
	}
	else {
		if (node.num < 0) {
			result += node.name;
		}
		else result += "var" + inttostr(node.num);
	}
	
	return result;
}

string InterCode::createCodeforArgument(varNode node) {
	string result = "ARG ";
	if (node.useAddress) {
		result += "*" + node.name;
	} 
	else {
		if (node.num < 0) {
			result += node.name;
		}
		else result += "var" + inttostr(node.num);
	}
	
	return result;
}

string InterCode::getNodeName(varNode node) {
	if (node.useAddress) {
		return "*" + node.name;
	}
	else {
		if (node.num < 0) {
			return node.name;
		}
		else return ("var" + inttostr(node.num));
	}

}

string InterCode::getarrayNodeName(arrayNode node) {
	return ("array" + inttostr(node.num));
}

string InterCode::getLabelName() {
	return "label" + inttostr(labelNum++);
}